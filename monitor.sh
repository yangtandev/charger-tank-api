#!/bin/bash

# --- Configuration ---
CHECK_INTERVAL_SECONDS=60 # 1 minute
CONSECUTIVE_CHECKS_THRESHOLD=3 # 3 consecutive breaches to trigger reboot
LOG_FILE="/home/talei-2/monitor.log" # Log file in home directory
# --- End of Configuration ---

# --- Logging Function ---
log_message() {
    local level="$1"
    local message="$2"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $level - $message" | tee -a "$LOG_FILE"
}

# --- Helper Functions ---
get_cpu_cores() {
    nproc
}

get_load_average() {
    # Get the 15-minute load average
    awk '{print $3}' /proc/loadavg
}

get_memory_usage_percent() {
    local mem_total_kb=$(awk '/MemTotal:/ {print $2}' /proc/meminfo)
    local mem_available_kb=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)

    if [[ -z "$mem_total_kb" || -z "$mem_available_kb" ]]; then
        log_message "WARNING" "Could not determine memory usage: MemTotal or MemAvailable not found in /proc/meminfo."
        echo "0"
        return
    fi

    # Calculate used memory and percentage using bc for floating point arithmetic
    local mem_used_kb=$(echo "$mem_total_kb - $mem_available_kb" | bc)
    local usage_percent=$(echo "scale=2; ($mem_used_kb * 100) / $mem_total_kb" | bc)
    echo "$usage_percent"
}

reboot_system() {
    log_message "CRITICAL" "Thresholds breached for ${CONSECUTIVE_CHECKS_THRESHOLD} consecutive checks. Rebooting now."
    sudo reboot
}

# --- Main Logic ---
main() {
    local breach_counter=0

    # Check if monitor is already running
    if pgrep -f "monitor.sh" | grep -v "$$" > /dev/null; then
        log_message "INFO" "Monitoring service is already running. Exiting."
        exit 1
    fi

    local num_cpu_cores=$(get_cpu_cores)
    local total_mem_gb=$(echo "scale=2; $(awk '/MemTotal:/ {print $2}' /proc/meminfo) / (1024*1024)" | bc)

    # Dynamic Thresholds
    local dynamic_load_avg_threshold=$(echo "scale=2; $num_cpu_cores * 2.5" | bc)
    local dynamic_mem_usage_threshold=90.0 # Still 90%

    log_message "INFO" "System detected: ${num_cpu_cores} CPU cores, ${total_mem_gb} GB RAM."
    log_message "INFO" "System monitor started with dynamic thresholds: Load Avg > ${dynamic_load_avg_threshold}, Mem Usage > ${dynamic_mem_usage_threshold}%"

    while true; do
        local load_avg=$(get_load_average)
        local mem_usage=$(get_memory_usage_percent)

        log_message "INFO" "Current state: Load Avg (15min) = ${load_avg}, Memory Usage = ${mem_usage}%"

        # Compare floating point numbers using bc
        if (( $(echo "$load_avg > $dynamic_load_avg_threshold" | bc -l) )) || \
           (( $(echo "$mem_usage > $dynamic_mem_usage_threshold" | bc -l) )); then
            breach_counter=$((breach_counter + 1))
            log_message "WARNING" "Threshold breached. Breach count: ${breach_counter}/${CONSECUTIVE_CHECKS_THRESHOLD}. Current values: Load=${load_avg}, Mem=${mem_usage}%. Thresholds: Load>${dynamic_load_avg_threshold}, Mem>${dynamic_mem_usage_threshold}%"
        else
            if [[ "$breach_counter" -gt 0 ]]; then
                log_message "INFO" "System state returned to normal. Resetting breach counter."
            fi
            breach_counter=0 # Reset if system is back to normal
        fi

        if [[ "$breach_counter" -ge "$CONSECUTIVE_CHECKS_THRESHOLD" ]]; then
            reboot_system
            break # Exit script after issuing reboot command
        fi

        sleep "$CHECK_INTERVAL_SECONDS"
    done
}

# Call the main function
main "$@"
