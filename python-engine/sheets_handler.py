from datetime import datetime, timedelta
import pandas as pd


def normalize_phone(phone: str) -> str:
    digits = "".join(ch for ch in str(phone) if ch.isdigit())
    # Si es un numero celular de Colombia (10 digitos iniciando en 3), antepone 57
    if len(digits) == 10 and digits.startswith("3"):
        return f"57{digits}"
    return digits


def load_appointments(file_path: str, sheet_name: str) -> pd.DataFrame:
    df = pd.read_excel(file_path, sheet_name=sheet_name, dtype={"telefono": str})
    for col in ["estado", "ultimo_envio"]:
        if col not in df.columns:
            df[col] = ""
    df["estado"] = df["estado"].fillna("").astype(str).str.strip()
    df["ultimo_envio"] = df["ultimo_envio"].fillna("").astype(str).str.strip()
    return df


def get_pending_reminders(df: pd.DataFrame, days_ahead: int = 1) -> pd.DataFrame:
    target_date = (datetime.now() + timedelta(days=days_ahead)).strftime("%Y-%m-%d")
    parsed_dates = pd.to_datetime(df["fecha_cita"], errors="coerce").dt.strftime("%Y-%m-%d")

    mask = (
        (parsed_dates == target_date)
        & (~df["estado"].str.lower().isin(["enviado", "confirmado", "cancelado"]))
    )
    return df[mask].copy()


def save_appointments(df: pd.DataFrame, file_path: str, sheet_name: str) -> None:
    with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)