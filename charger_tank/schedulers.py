from apscheduler.schedulers.background import BackgroundScheduler
from datetime import timedelta
from django.utils.timezone import now
from charger_tank.models import ChargerTankStatus

def update_charger_status():
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

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_charger_status, 'interval', seconds=30)
    scheduler.start()
