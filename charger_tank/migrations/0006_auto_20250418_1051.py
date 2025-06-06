# Generated by Django 3.2.12 on 2025-04-18 10:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('charger_tank', '0005_auto_20250418_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='RecDT',
            new_name='record_datetime',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S01',
            new_name='s01',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S02',
            new_name='s02',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S03',
            new_name='s03',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S04',
            new_name='s04',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S05',
            new_name='s05',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S06',
            new_name='s06',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S07',
            new_name='s07',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S08',
            new_name='s08',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S09',
            new_name='s09',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S10',
            new_name='s10',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S11',
            new_name='s11',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S12',
            new_name='s12',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S13',
            new_name='s13',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S14',
            new_name='s14',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S15',
            new_name='s15',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S16',
            new_name='s16',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S17',
            new_name='s17',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='S18',
            new_name='s18',
        ),
        migrations.RenameField(
            model_name='chargertankcurrent',
            old_name='Temptype',
            new_name='temp_type',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='RecDT',
            new_name='record_datetime',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S01',
            new_name='s01',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S02',
            new_name='s02',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S03',
            new_name='s03',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S04',
            new_name='s04',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S05',
            new_name='s05',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S06',
            new_name='s06',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S07',
            new_name='s07',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S08',
            new_name='s08',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S09',
            new_name='s09',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S10',
            new_name='s10',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S11',
            new_name='s11',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S12',
            new_name='s12',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S13',
            new_name='s13',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S14',
            new_name='s14',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S15',
            new_name='s15',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S16',
            new_name='s16',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S17',
            new_name='s17',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='S18',
            new_name='s18',
        ),
        migrations.RenameField(
            model_name='chargertankhistory',
            old_name='Temptype',
            new_name='temp_type',
        ),
        migrations.RenameField(
            model_name='chargertankstatus',
            old_name='EnvTemp',
            new_name='env_temp',
        ),
        migrations.RenameField(
            model_name='chargertankstatus',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='chargertankstatus',
            old_name='RecDT',
            new_name='record_datetime',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status01',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status02',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status03',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status04',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status05',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status06',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status07',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status08',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status09',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status10',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status11',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status12',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status13',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status14',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status15',
        ),
        migrations.RemoveField(
            model_name='chargertankstatus',
            name='Charger_Status16',
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status01',
            field=models.BooleanField(blank=True, db_column='ChargerStatus01', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status02',
            field=models.BooleanField(blank=True, db_column='ChargerStatus02', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status03',
            field=models.BooleanField(blank=True, db_column='ChargerStatus03', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status04',
            field=models.BooleanField(blank=True, db_column='ChargerStatus04', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status05',
            field=models.BooleanField(blank=True, db_column='ChargerStatus05', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status06',
            field=models.BooleanField(blank=True, db_column='ChargerStatus06', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status07',
            field=models.BooleanField(blank=True, db_column='ChargerStatus07', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status08',
            field=models.BooleanField(blank=True, db_column='ChargerStatus08', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status09',
            field=models.BooleanField(blank=True, db_column='ChargerStatus09', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status10',
            field=models.BooleanField(blank=True, db_column='ChargerStatus10', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status11',
            field=models.BooleanField(blank=True, db_column='ChargerStatus11', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status12',
            field=models.BooleanField(blank=True, db_column='ChargerStatus12', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status13',
            field=models.BooleanField(blank=True, db_column='ChargerStatus13', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status14',
            field=models.BooleanField(blank=True, db_column='ChargerStatus14', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status15',
            field=models.BooleanField(blank=True, db_column='ChargerStatus15', null=True),
        ),
        migrations.AddField(
            model_name='chargertankstatus',
            name='charger_status16',
            field=models.BooleanField(blank=True, db_column='ChargerStatus16', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='location',
            field=models.CharField(db_column='Location', max_length=10),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='record_datetime',
            field=models.DateTimeField(db_column='RecDT', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s01',
            field=models.IntegerField(blank=True, db_column='S01', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s02',
            field=models.IntegerField(blank=True, db_column='S02', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s03',
            field=models.IntegerField(blank=True, db_column='S03', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s04',
            field=models.IntegerField(blank=True, db_column='S04', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s05',
            field=models.IntegerField(blank=True, db_column='S05', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s06',
            field=models.IntegerField(blank=True, db_column='S06', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s07',
            field=models.IntegerField(blank=True, db_column='S07', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s08',
            field=models.IntegerField(blank=True, db_column='S08', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s09',
            field=models.IntegerField(blank=True, db_column='S09', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s10',
            field=models.IntegerField(blank=True, db_column='S10', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s11',
            field=models.IntegerField(blank=True, db_column='S11', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s12',
            field=models.IntegerField(blank=True, db_column='S12', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s13',
            field=models.IntegerField(blank=True, db_column='S13', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s14',
            field=models.IntegerField(blank=True, db_column='S14', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s15',
            field=models.IntegerField(blank=True, db_column='S15', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s16',
            field=models.IntegerField(blank=True, db_column='S16', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s17',
            field=models.IntegerField(blank=True, db_column='S17', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='s18',
            field=models.IntegerField(blank=True, db_column='S18', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankcurrent',
            name='temp_type',
            field=models.IntegerField(db_column='Temptype'),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='location',
            field=models.CharField(db_column='Location', max_length=10),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='record_datetime',
            field=models.DateTimeField(db_column='RecDT', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s01',
            field=models.IntegerField(blank=True, db_column='S01', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s02',
            field=models.IntegerField(blank=True, db_column='S02', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s03',
            field=models.IntegerField(blank=True, db_column='S03', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s04',
            field=models.IntegerField(blank=True, db_column='S04', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s05',
            field=models.IntegerField(blank=True, db_column='S05', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s06',
            field=models.IntegerField(blank=True, db_column='S06', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s07',
            field=models.IntegerField(blank=True, db_column='S07', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s08',
            field=models.IntegerField(blank=True, db_column='S08', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s09',
            field=models.IntegerField(blank=True, db_column='S09', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s10',
            field=models.IntegerField(blank=True, db_column='S10', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s11',
            field=models.IntegerField(blank=True, db_column='S11', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s12',
            field=models.IntegerField(blank=True, db_column='S12', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s13',
            field=models.IntegerField(blank=True, db_column='S13', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s14',
            field=models.IntegerField(blank=True, db_column='S14', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s15',
            field=models.IntegerField(blank=True, db_column='S15', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s16',
            field=models.IntegerField(blank=True, db_column='S16', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s17',
            field=models.IntegerField(blank=True, db_column='S17', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='s18',
            field=models.IntegerField(blank=True, db_column='S18', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankhistory',
            name='temp_type',
            field=models.IntegerField(db_column='Temptype'),
        ),
        migrations.AlterField(
            model_name='chargertankstatus',
            name='env_temp',
            field=models.IntegerField(blank=True, db_column='EnvTemp', null=True),
        ),
        migrations.AlterField(
            model_name='chargertankstatus',
            name='location',
            field=models.CharField(db_column='Location', max_length=10),
        ),
        migrations.AlterField(
            model_name='chargertankstatus',
            name='record_datetime',
            field=models.DateTimeField(db_column='RecDT', default=django.utils.timezone.now),
        ),
    ]
