# Seguridad de los datos 
Cifrado: Utilizarlo en todos los servicios que lo permitan. La mayoría de servicios incluyen integración con KMS.

Permisos: La mayor granularidad que se pueda implementar, garantizar el acceso a la data puntual que se requiera.

Servicios: Reducir la administración con serverless, esto aumenta la disponibilidad y el performance de nuestros servicios.

Monitoreo: Registrar todos los logs de ejecución nos permite identificar problemas.

Contingencia: Desplegar en múltiples regiones, replicar la data entre regiones.

Test: siempre verificar la data que está llegando antes de pasar a producción.

## AWS Macie
AWS Macie es un servicio de Amazon Web Services (AWS) diseñado para ayudar a las organizaciones a proteger sus datos confidenciales y personales almacenados en la nube de AWS. Macie utiliza técnicas de inteligencia artificial (IA) y aprendizaje automático para identificar y proteger automáticamente los datos sensibles, lo que puede ser especialmente importante en entornos en la nube donde los datos se almacenan y procesan a gran escala.

Las principales características y capacidades de AWS Macie incluyen:

Detección de datos confidenciales: Macie escanea continuamente los recursos de almacenamiento en la nube de AWS, como buckets de Amazon S3, en busca de datos sensibles o personales, como números de tarjetas de crédito, números de seguridad social y otros tipos de información confidencial.

Clasificación y etiquetado automático: El servicio clasifica automáticamente los datos detectados y aplica etiquetas para identificar el tipo de información que se encuentra en los archivos. Esto ayuda a las organizaciones a comprender qué datos están almacenados en sus entornos de AWS y a aplicar políticas de seguridad adecuadas.

Alertas y notificaciones: Macie puede generar alertas cuando detecta actividades inusuales o potencialmente sospechosas relacionadas con los datos sensibles. Esto permite a los administradores de seguridad tomar medidas rápidas en caso de una posible violación de datos.

Informes y auditorías: Proporciona informes detallados y registros de auditoría que pueden ayudar a las organizaciones a cumplir con los requisitos de cumplimiento y demostrar el cumplimiento de regulaciones como el Reglamento General de Protección de Datos (RGPD) de la Unión Europea.

Integración con otros servicios de seguridad de AWS: Macie se puede integrar con otros servicios de seguridad de AWS, como AWS Identity and Access Management (IAM) y AWS CloudTrail, para una protección y monitoreo más completos de los recursos en la nube.

Ransomware: Detecta si tenemos software potencialmente malintencionado en archivos o de cualquier otra manera

OJO: es un servicio muy costoso!

## EJemplo

Supongamos que una empresa almacena una gran cantidad de datos en Amazon S3, incluyendo archivos que contienen información sensible de los clientes, como números de tarjetas de crédito. La empresa desea asegurarse de que esta información se mantenga segura y cumpla con las regulaciones de privacidad de datos.

Configuración de AWS Macie: El primer paso sería configurar AWS Macie en la cuenta de AWS. Esto implica habilitar el servicio y configurar las reglas y políticas de detección según las necesidades de la empresa. Por ejemplo, se pueden definir reglas que busquen patrones específicos, como números de tarjetas de crédito, números de seguridad social o cualquier otro dato sensible.

Escaneo y detección automática: Una vez que Macie está configurado, comenzará a escanear continuamente los buckets de Amazon S3 en busca de datos sensibles. Cuando detecta archivos que coinciden con las reglas de detección configuradas, los clasifica y etiqueta automáticamente.

Alertas y notificaciones: Si Macie encuentra datos sensibles o detecta actividades inusuales, puede generar alertas y notificaciones. Por ejemplo, si alguien intenta acceder o descargar un archivo que contiene números de tarjetas de crédito, Macie puede enviar una alerta a los administradores de seguridad.

Auditoría y cumplimiento: Macie proporciona registros de auditoría detallados y reportes que pueden ser utilizados para demostrar el cumplimiento de las regulaciones de privacidad de datos. Esto puede ser útil en auditorías internas o externas.

Acciones de mitigación: En función de las políticas definidas, Macie puede tomar acciones automatizadas, como bloquear el acceso a archivos o restringir ciertas operaciones cuando se detecta una amenaza de seguridad.