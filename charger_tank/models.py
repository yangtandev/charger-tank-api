from django.db import models
from django.utils import timezone

# 1. 溫度實時表（只保留最新資料）
class ChargerTankCurrent(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=10, db_column='Location')
    temp_type = models.IntegerField(db_column='Temptype')
    record_datetime = models.DateTimeField(default=timezone.now, db_column='RecDT')
    s01 = models.IntegerField(null=True, blank=True, db_column='S01')
    s02 = models.IntegerField(null=True, blank=True, db_column='S02')
    s03 = models.IntegerField(null=True, blank=True, db_column='S03')
    s04 = models.IntegerField(null=True, blank=True, db_column='S04')
    s05 = models.IntegerField(null=True, blank=True, db_column='S05')
    s06 = models.IntegerField(null=True, blank=True, db_column='S06')
    s07 = models.IntegerField(null=True, blank=True, db_column='S07')
    s08 = models.IntegerField(null=True, blank=True, db_column='S08')
    s09 = models.IntegerField(null=True, blank=True, db_column='S09')
    s10 = models.IntegerField(null=True, blank=True, db_column='S10')
    s11 = models.IntegerField(null=True, blank=True, db_column='S11')
    s12 = models.IntegerField(null=True, blank=True, db_column='S12')
    s13 = models.IntegerField(null=True, blank=True, db_column='S13')
    s14 = models.IntegerField(null=True, blank=True, db_column='S14')
    s15 = models.IntegerField(null=True, blank=True, db_column='S15')
    s16 = models.IntegerField(null=True, blank=True, db_column='S16')
    s17 = models.IntegerField(null=True, blank=True, db_column='S17')
    s18 = models.IntegerField(null=True, blank=True, db_column='S18')

    class Meta:
        db_table = 'charger_tank_current'


# 2. 溫度歷史紀錄表（記錄所有資料）
class ChargerTankHistory(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=10, db_column='Location')
    temp_type = models.IntegerField(db_column='Temptype')
    record_datetime = models.DateTimeField(default=timezone.now, db_column='RecDT')
    s01 = models.IntegerField(null=True, blank=True, db_column='S01')
    s02 = models.IntegerField(null=True, blank=True, db_column='S02')
    s03 = models.IntegerField(null=True, blank=True, db_column='S03')
    s04 = models.IntegerField(null=True, blank=True, db_column='S04')
    s05 = models.IntegerField(null=True, blank=True, db_column='S05')
    s06 = models.IntegerField(null=True, blank=True, db_column='S06')
    s07 = models.IntegerField(null=True, blank=True, db_column='S07')
    s08 = models.IntegerField(null=True, blank=True, db_column='S08')
    s09 = models.IntegerField(null=True, blank=True, db_column='S09')
    s10 = models.IntegerField(null=True, blank=True, db_column='S10')
    s11 = models.IntegerField(null=True, blank=True, db_column='S11')
    s12 = models.IntegerField(null=True, blank=True, db_column='S12')
    s13 = models.IntegerField(null=True, blank=True, db_column='S13')
    s14 = models.IntegerField(null=True, blank=True, db_column='S14')
    s15 = models.IntegerField(null=True, blank=True, db_column='S15')
    s16 = models.IntegerField(null=True, blank=True, db_column='S16')
    s17 = models.IntegerField(null=True, blank=True, db_column='S17')
    s18 = models.IntegerField(null=True, blank=True, db_column='S18')

    class Meta:
        db_table = 'charger_tank_history'


# 3. 狀態實時表（記錄環境溫度與 16 台充電機狀態）
class ChargerTankStatus(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=10, db_column='Location')
    record_datetime = models.DateTimeField(default=timezone.now, db_column='RecDT')
    env_temp = models.IntegerField(null=True, blank=True, db_column='EnvTemp')
    charger_status01 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus01')
    charger_status02 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus02')
    charger_status03 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus03')
    charger_status04 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus04')
    charger_status05 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus05')
    charger_status06 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus06')
    charger_status07 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus07')
    charger_status08 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus08')
    charger_status09 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus09')
    charger_status10 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus10')
    charger_status11 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus11')
    charger_status12 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus12')
    charger_status13 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus13')
    charger_status14 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus14')
    charger_status15 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus15')
    charger_status16 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus16')

    class Meta:
        db_table = 'charger_tank_status'

# 4. 狀態歷史表（記錄環境溫度與 16 台充電機狀態）
class ChargerTankStatusHistory(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=10, db_column='Location')
    record_datetime = models.DateTimeField(default=timezone.now, db_column='RecDT')
    env_temp = models.IntegerField(null=True, blank=True, db_column='EnvTemp')
    charger_status01 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus01')
    charger_status02 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus02')
    charger_status03 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus03')
    charger_status04 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus04')
    charger_status05 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus05')
    charger_status06 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus06')
    charger_status07 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus07')
    charger_status08 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus08')
    charger_status09 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus09')
    charger_status10 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus10')
    charger_status11 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus11')
    charger_status12 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus12')
    charger_status13 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus13')
    charger_status14 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus14')
    charger_status15 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus15')
    charger_status16 = models.BooleanField(null=True, blank=True, db_column='ChargerStatus16')

    class Meta:
        db_table = 'charger_tank_status_history'
