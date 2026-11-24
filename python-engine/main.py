from datetime import datetime
from config import Config
from sheets_handler import get_pending_reminders, load_appointments, normalize_phone, save_appointments
from whatsapp_client import WhatsAppCloudClient


def run_job(dry_run: bool = True) -> None:
    df = load_appointments(Config.EXCEL_FILE_PATH, Config.EXCEL_SHEET_NAME)
    pending = get_pending_reminders(df, days_ahead=Config.DAYS_AHEAD)

    print(f"Registros pendientes para enviar recordatorio: {len(pending)}")
    if pending.empty:
        return

    client = WhatsAppCloudClient(
        token=Config.WHATSAPP_TOKEN,
        phone_number_id=Config.WHATSAPP_PHONE_NUMBER_ID,
        dry_run=dry_run,
    )

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    for idx, row in pending.iterrows():
        phone = normalize_phone(row.get("telefono", ""))
        name = str(row.get("cliente", "Cliente")).strip()
        service = str(row.get("servicio", "Servicio")).strip()
        date_str = str(row.get("fecha_cita", "")).strip()
        time_str = str(row.get("hora_cita", "")).strip()

        ok, detail = client.send_reminder_template(
            to_phone=phone,
            client_name=name,
            appointment_date=date_str,
            appointment_time=time_str,
            service_name=service,
            template_name=Config.WHATSAPP_TEMPLATE_NAME,
            language_code=Config.WHATSAPP_TEMPLATE_LANG,
        )

        print(f"Fila {idx + 2}: {detail}")
        if ok:
            df.at[idx, "estado"] = "Enviado"
            df.at[idx, "ultimo_envio"] = now_str

    save_appointments(df, Config.EXCEL_FILE_PATH, Config.EXCEL_SHEET_NAME)
    print("Proceso finalizado y hoja actualizada.")


if __name__ == "__main__":
    # Cambia dry_run=False cuando tengas credenciales reales de Meta configuradas
    run_job(dry_run=True)