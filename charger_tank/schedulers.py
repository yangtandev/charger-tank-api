from apscheduler.schedulers.background import BackgroundScheduler
from datetime import timedelta
from django.utils.timezone import now
from django.db.models import Avg
from charger_tank.models import ChargerTankStatus, ChargerTankHistory, ChargerTankHistory5Min

def update_charger_status():
    """原有的排程：更新超時的充電器狀態"""
    # 計算超時的時間
    timeout_threshold = now() - timedelta(minutes=1)

    # 查詢超時的資料
    expired_records = ChargerTankStatus.objects.filter(record_datetime__lt=timeout_threshold)

    # 更新 ChargerStatus01~ChargerStatus16 為 null
    for record in expired_records:
        record.charger_status01 = None
        record.charger_status02 = None
        record.charger_status03 = None
        record.charger_status04 = None
        record.charger_status05 = None
        record.charger_status06 = None
        record.charger_status07 = None
        record.charger_status08 = None
        record.charger_status09 = None
        record.charger_status10 = None
        record.charger_status11 = None
        record.charger_status12 = None
        record.charger_status13 = None
        record.charger_status14 = None
        record.charger_status15 = None
        record.charger_status16 = None
        record.save()

    print(f"Updated {expired_records.count()} records.")

def calculate_5min_averages():
    """每五分鐘計算一次歷史紀錄的平均值並存入5分鐘平均表"""
    try:
        # 獲取當前時間並調整到最近的5分鐘整點
        current_time = now()
        current_minutes = current_time.minute
        aligned_minutes = (current_minutes // 5) * 5

        # 計算上一個5分鐘區間的結束時間
        end_time = current_time.replace(minute=aligned_minutes, second=0, microsecond=0)
        # 計算上一個5分鐘區間的開始時間
        start_time = end_time - timedelta(minutes=5)

        print(f"Calculating 5-minute averages from {start_time} to {end_time}")

        # 獲取所有唯一的 location 和 temp_type 組合
        unique_combinations = ChargerTankHistory.objects.filter(
            record_datetime__gte=start_time,
            record_datetime__lt=end_time
        ).values('location', 'temp_type').distinct()

        records_created = 0

        for combo in unique_combinations:
            location = combo['location']
            temp_type = combo['temp_type']

            # 查詢該組合在指定5分鐘區間內的所有記錄
            records = ChargerTankHistory.objects.filter(
                location=location,
                temp_type=temp_type,
                record_datetime__gte=start_time,
                record_datetime__lt=end_time
            )

            print(f"Found {records.count()} records for location: {location}, temp_type: {temp_type} in time range {start_time} to {end_time}")

            if records.exists():
                # 計算各感測器的平均值
                averages = records.aggregate(
                    s01_avg=Avg('s01'),
                    s02_avg=Avg('s02'),
                    s03_avg=Avg('s03'),
                    s04_avg=Avg('s04'),
                    s05_avg=Avg('s05'),
                    s06_avg=Avg('s06'),
                    s07_avg=Avg('s07'),
                    s08_avg=Avg('s08'),
                    s09_avg=Avg('s09'),
                    s10_avg=Avg('s10'),
                    s11_avg=Avg('s11'),
                    s12_avg=Avg('s12'),
                    s13_avg=Avg('s13'),
                    s14_avg=Avg('s14'),
                    s15_avg=Avg('s15'),
                    s16_avg=Avg('s16'),
                    s17_avg=Avg('s17'),
                    s18_avg=Avg('s18'),
                )

                # 將 None 值轉換為 None，並將浮點數轉換為整數
                processed_averages = {}
                for key, value in averages.items():
                    if value is not None:
                        processed_averages[key.replace('_avg', '')] = round(value)
                    else:
                        processed_averages[key.replace('_avg', '')] = None

                # 檢查是否已存在相同時間區間的記錄（避免重複創建）
                # 使用5分鐘間隔的整點時間作為記錄時間
                record_time = current_time.replace(second=0, microsecond=0)
                # 調整到最近的5分鐘整點
                minutes = record_time.minute
                adjusted_minutes = (minutes // 5) * 5
                record_time = record_time.replace(minute=adjusted_minutes)

                existing_record = ChargerTankHistory5Min.objects.filter(
                    location=location,
                    temp_type=temp_type,
                    record_datetime=record_time
                ).first()

                if not existing_record:
                    # 創建新的5分鐘平均記錄
                    ChargerTankHistory5Min.objects.create(
                        location=location,
                        temp_type=temp_type,
                        record_datetime=record_time,
                        **processed_averages
                    )
                    records_created += 1
                    print(f"Created 5-min average for location: {location}, temp_type: {temp_type}")
                else:
                    print(f"5-min average already exists for location: {location}, temp_type: {temp_type} at {record_time}")

        print(f"5-minute averages calculation completed. Created {records_created} new records.")

    except Exception as e:
        print(f"Error calculating 5-minute averages: {e}")

def cleanup_old_history_records():
    """每小時清理超過一周的歷史紀錄"""
    try:
        # 計算一周前的時間點
        one_week_ago = now() - timedelta(weeks=1)

        print(f"Cleaning up history records older than {one_week_ago}")

        # 查詢並刪除超過一周的記錄
        old_records = ChargerTankHistory.objects.filter(record_datetime__lt=one_week_ago)
        deleted_count = old_records.count()

        if deleted_count > 0:
            old_records.delete()
            print(f"Deleted {deleted_count} old history records.")
        else:
            print("No old history records found to delete.")

    except Exception as e:
        print(f"Error cleaning up old history records: {e}")

def start_scheduler():
    """啟動所有排程任務"""
    scheduler = BackgroundScheduler()

    # 每30秒更新充電器狀態
    scheduler.add_job(
        update_charger_status,
        'interval',
        seconds=30,
        id='update_charger_status'
    )

    # 每分鐘計算歷史記錄平均值
    scheduler.add_job(
        calculate_5min_averages,
        'interval',
        minutes=1,
        id='calculate_5min_averages'
    )

    # 每小時清理舊的歷史記錄
    scheduler.add_job(
        cleanup_old_history_records,
        'interval',
        hours=1,
        id='cleanup_old_history_records'
    )

    scheduler.start()
