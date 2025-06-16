import pyodbc
import threading
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from .models import ChargerTankCurrent, ChargerTankHistory, ChargerTankHistory5Min
from dbconfig.models import MSSQLConfig
from django.forms.models import model_to_dict


logger = logging.getLogger(__name__)

def process_value(val):
    return 0 if val == 999 else int(round(val / 10))


def async_upsert_to_mssql(instance):
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

        s_values = [
            instance.s01, instance.s02, instance.s03, instance.s04,
            instance.s05, instance.s06, instance.s07, instance.s08,
            instance.s09, instance.s10, instance.s11, instance.s12,
            instance.s13, instance.s14, instance.s15, instance.s16,
            instance.s17, instance.s18,
        ]

        with pyodbc.connect(conn_str, timeout=5) as conn:
            cursor = conn.cursor()

            sql = f"""
            MERGE INTO {full_table_name} AS target
            USING (VALUES (?, ?, ?)) AS source (Location, TempType, RecDT)
            ON (target.Location = source.Location AND target.TempType = source.TempType AND target.RecDT = source.RecDT)
            WHEN MATCHED THEN
                UPDATE SET
                    S01 = ?, S02 = ?, S03 = ?, S04 = ?, S05 = ?, S06 = ?, S07 = ?, S08 = ?, S09 = ?, S10 = ?,
                    S11 = ?, S12 = ?, S13 = ?, S14 = ?, S15 = ?, S16 = ?, S17 = ?, S18 = ?
            WHEN NOT MATCHED THEN
                INSERT (Location, TempType, RecDT, S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11, S12, S13, S14, S15, S16, S17, S18)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """

            params = (
                instance.location,
                instance.temp_type,
                instance.record_datetime,
                *s_values,
                instance.location,
                instance.temp_type,
                instance.record_datetime,
                *s_values,
            )

            cursor.execute(sql, params)
            conn.commit()
            logger.info(f"[MSSQL upsert success] {instance.record_datetime} @ {instance.location}")

    except MSSQLConfig.DoesNotExist:
        print(f"[MSSQL upsert error] no MSSQL config found")
        logger.error("[MSSQL upsert error] No MSSQL config found.")
    except Exception as e:
        print(f"[MSSQL upsert error] {e}")
        logger.error(
            f"[MSSQL upsert error] Failed to upsert record "
            f"(Location={instance.location}, TempType={instance.temp_type}, RecDT={instance.record_datetime}): {e}",
            exc_info=True
        )

@receiver(post_save, sender=ChargerTankCurrent)
def copy_to_history(sender, instance, created, **kwargs):
    processed_values = {
        's01': process_value(instance.s01),
        's02': process_value(instance.s02),
        's03': process_value(instance.s03),
        's04': process_value(instance.s04),
        's05': process_value(instance.s05),
        's06': process_value(instance.s06),
        's07': process_value(instance.s07),
        's08': process_value(instance.s08),
        's09': process_value(instance.s09),
        's10': process_value(instance.s10),
        's11': process_value(instance.s11),
        's12': process_value(instance.s12),
        's13': process_value(instance.s13),
        's14': process_value(instance.s14),
        's15': process_value(instance.s15),
        's16': process_value(instance.s16),
        's17': process_value(instance.s17),
        's18': process_value(instance.s18),
    }

    ChargerTankHistory.objects.create(
        location=instance.location,
        temp_type=instance.temp_type,
        record_datetime=instance.record_datetime,
        **processed_values,
    )

@receiver(post_save, sender=ChargerTankHistory5Min)
def write_back_to_client_db(sender, instance, created, **kwargs):
    threading.Thread(target=async_upsert_to_mssql, args=(instance,)).start()
