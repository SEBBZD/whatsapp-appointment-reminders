# WhatsApp Appointment & Renewal Reminders

Sistema automatizado para enviar recordatorios de citas, servicios o renovaciones por **WhatsApp Business Cloud API (Meta)** a partir de hojas de cálculo, evitando ausencias de última hora y reduciendo el seguimiento manual.

---

## Problema de Negocio que Resuelve

En negocios como clínicas odontológicas, centros estéticos, talleres mecánicos, veterinarias o agencias de servicios, una cita no asistida o una renovación olvidada representa pérdida directa de ingresos y horas operativas desperdiciadas.

Este sistema automatiza el ciclo diario de recordatorios:
1. Lee la agenda o base de clientes desde una hoja de cálculo (`clientes_demo.xlsx` / Google Sheets).
2. Filtra automáticamente los registros programados para la ventana configurada (por defecto, citas de mañana con `DAYS_AHEAD=1`).
3. Normaliza números telefónicos al formato internacional (incluyendo prefijo `57` para líneas móviles de Colombia).
4. Envía el mensaje mediante plantilla oficial de **WhatsApp Business Cloud API** (con soporte para modo simulación `dry_run=True` en pruebas).
5. Actualiza el estado (`Enviado`) y la marca de tiempo (`ultimo_envio`) para evitar envíos duplicados.

---

## Arquitectura del Proyecto

```text
whatsapp-appointment-reminders/
├── README.md
├── .env.example
├── data/
│   └── clientes_demo.xlsx
└── python-engine/
    ├── config.py           # Carga y validación de variables de entorno
    ├── sheets_handler.py   # Lectura, filtrado por fecha, normalización y guardado
    ├── whatsapp_client.py  # Cliente HTTP para Meta WhatsApp Cloud API + modo simulación
    ├── main.py             # Orquestador del flujo diario
    └── requirements.txt    # Dependencias del proyecto
```

---

## ⚙️ Instalación y Prueba Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/SEBBZD/whatsapp-appointment-reminders.git](https://github.com/SEBBZD/whatsapp-appointment-reminders.git)
   cd whatsapp-appointment-reminders
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r python-engine/requirements.txt
   ```

3. **Configurar variables de entorno:**
   Copia `.env.example` a un archivo `.env` en la raíz y ajusta los parámetros según tu entorno.

4. **Ejecutar en modo simulación (`dry_run=True`):**
   ```bash
   python python-engine/main.py
   ```

---

##  Escalabilidad y Enfoque Comercial

* **Producción con n8n:** Este mismo flujo puede orquestarse de forma visual en **n8n** conectando nodos de *Schedule Trigger*, *Google Sheets* y *WhatsApp Business Cloud*, ideal para clientes que requieren panel visual y monitoreo continuo.
* **Personalización por cliente:** Se adapta a recordatorios de citas médicas, mantenimientos preventivos, cobros preventivos o renovaciones de suscripciones/pólizas.

---

##  Autor

**Juan Sebastián García** — Backend & Automation Developer  
📍 Bogotá, Colombia  
✉️ sebastiangc301@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/juan-sebastian-garcia-dev)
