import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN", "")
    WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
    WHATSAPP_TEMPLATE_NAME = os.getenv("WHATSAPP_TEMPLATE_NAME", "recordatorio_cita_general")
    WHATSAPP_TEMPLATE_LANG = os.getenv("WHATSAPP_TEMPLATE_LANG", "es_CO")
    EXCEL_FILE_PATH = os.getenv("EXCEL_FILE_PATH", "data/clientes_demo.xlsx")
    EXCEL_SHEET_NAME = os.getenv("EXCEL_SHEET_NAME", "Citas")
    DAYS_AHEAD = int(os.getenv("DAYS_AHEAD", "1"))