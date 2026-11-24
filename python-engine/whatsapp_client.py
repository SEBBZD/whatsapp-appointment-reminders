import requests


class WhatsAppCloudClient:
    def __init__(self, token: str, phone_number_id: str, dry_run: bool = True):
        self.token = token
        self.phone_number_id = phone_number_id
        self.dry_run = dry_run
        self.base_url = f"https://graph.facebook.com/v21.0/{phone_number_id}/messages"

    def send_reminder_template(
        self,
        to_phone: str,
        client_name: str,
        appointment_date: str,
        appointment_time: str,
        service_name: str,
        template_name: str,
        language_code: str = "es_CO",
    ) -> tuple[bool, str]:
        payload = {
            "messaging_product": "whatsapp",
            "to": to_phone,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {"code": language_code},
                "components": [
                    {
                        "type": "body",
                        "parameters": [
                            {"type": "text", "text": client_name},
                            {"type": "text", "text": service_name},
                            {"type": "text", "text": appointment_date},
                            {"type": "text", "text": appointment_time},
                        ],
                    }
                ],
            },
        }

        if self.dry_run or not self.token or not self.phone_number_id:
            return True, f"[SIMULACION] Mensaje preparado para {to_phone} ({client_name} - {service_name})"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.post(self.base_url, json=payload, headers=headers, timeout=15)
            if response.status_code in (200, 201):
                return True, f"Enviado correctamente a {to_phone}"
            return False, f"Error API ({response.status_code}): {response.text}"
        except requests.RequestException as exc:
            return False, f"Error de red: {exc}"