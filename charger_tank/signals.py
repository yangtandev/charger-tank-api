import pyodbc
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ChargerTankCurrent, ChargerTankHistory
from dbconfig.models import MSSQLConfig

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

    try:
        config = MSSQLConfig.objects.latest('updated_at')
        schema = config.schema or 'dbo'
        full_table_name = f"[{schema}].[{config.table_name}]"
        conn_str = (
            f"DRIVER={{{config.driver}}};"
            f"SERVER={config.host},{config.port};"
            f"DATABASE={config.database};"
            f"UID={config.username};"
            f"PWD={config.password};"
            f"TrustServerCertificate=yes;"
        )

        with pyodbc.connect(conn_str, timeout=5) as conn:
            cursor = conn.cursor()

            # Upsert record by using MERGE
            sql = f"""
            MERGE INTO {full_table_name} AS target
            USING (VALUES (?, ?, ?)) AS source (Location, Temptype, RecDT)
            ON (target.Location = source.Location AND target.Temptype = source.Temptype AND target.RecDT = source.RecDT)
            WHEN MATCHED THEN
                UPDATE SET
                    S01 = ?, S02 = ?, S03 = ?, S04 = ?, S05 = ?, S06 = ?, S07 = ?, S08 = ?, S09 = ?, S10 = ?,
                    S11 = ?, S12 = ?, S13 = ?, S14 = ?, S15 = ?, S16 = ?, S17 = ?, S18 = ?
            WHEN NOT MATCHED THEN
                INSERT (Location, Temptype, RecDT, S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11, S12, S13, S14, S15, S16, S17, S18)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """

            params = (
                # source (Location, Temptype, RecDT)
                instance.location,
                instance.temp_type,
                instance.record_datetime,

                # update SET S01~S18
                instance.s01, instance.s02, instance.s03, instance.s04, instance.s05, instance.s06, instance.s07, instance.s08,
                instance.s09, instance.s10, instance.s11, instance.s12, instance.s13, instance.s14, instance.s15, instance.s16,
                instance.s17, instance.s18,

                # insert VALUES (Location, Temptype, RecDT, S01~S18)
                instance.location,
                instance.temp_type,
                instance.record_datetime,
                instance.s01, instance.s02, instance.s03, instance.s04, instance.s05, instance.s06, instance.s07, instance.s08,
                instance.s09, instance.s10, instance.s11, instance.s12, instance.s13, instance.s14, instance.s15, instance.s16,
                instance.s17, instance.s18,
            )

            cursor.execute(sql, params)
            conn.commit()

    except MSSQLConfig.DoesNotExist:
        pass
    except Exception as e:
        print(f"[MSSQL upsert error] {e}")

