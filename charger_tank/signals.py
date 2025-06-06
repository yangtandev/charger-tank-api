from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ChargerTankCurrent, ChargerTankHistory, ChargerTankStatus, ChargerTankStatusHistory

@receiver(post_save, sender=ChargerTankCurrent)
def copy_to_history(sender, instance, created, **kwargs):
    # 將 current 的 instance 資料複製到 history 中
    ChargerTankHistory.objects.create(
        location=instance.location,
        temp_type=instance.temp_type,
        record_datetime=instance.record_datetime,
        s01=instance.s01,
        s02=instance.s02,
        s03=instance.s03,
        s04=instance.s04,
        s05=instance.s05,
        s06=instance.s06,
        s07=instance.s07,
        s08=instance.s08,
        s09=instance.s09,
        s10=instance.s10,
        s11=instance.s11,
        s12=instance.s12,
        s13=instance.s13,
        s14=instance.s14,
        s15=instance.s15,
        s16=instance.s16,
        s17=instance.s17,
        s18=instance.s18,
    )

@receiver(post_save, sender=ChargerTankStatus)
def copy_to_status_history(sender, instance, created, **kwargs):
    # 將 status 的 instance 資料複製到 status_history 中
    ChargerTankStatusHistory.objects.create(
        location=instance.location,
        env_temp=instance.env_temp,
        record_datetime=instance.record_datetime,
        charger_status01=instance.charger_status01,
        charger_status02=instance.charger_status02,
        charger_status03=instance.charger_status03,
        charger_status04=instance.charger_status04,
        charger_status05=instance.charger_status05,
        charger_status06=instance.charger_status06,
        charger_status07=instance.charger_status07,
        charger_status08=instance.charger_status08,
        charger_status09=instance.charger_status09,
        charger_status10=instance.charger_status10,
        charger_status11=instance.charger_status11,
        charger_status12=instance.charger_status12,
        charger_status13=instance.charger_status13,
        charger_status14=instance.charger_status14,
        charger_status15=instance.charger_status15,
        charger_status16=instance.charger_status16
    )
