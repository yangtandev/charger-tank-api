from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ChargerTankCurrent, ChargerTankHistory

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
