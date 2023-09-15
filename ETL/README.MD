# :heart: AWS GLUE
AWS Glue es un servicio completamente administrado de extracción, transformación y carga (ETL) ofrecido por Amazon Web Services (AWS). Está diseñado para facilitar a las organizaciones la preparación y carga de sus datos para análisis y almacenamiento de datos. Aquí tienes algunos aspectos y características clave de AWS Glue:

Servicio de ETL: AWS Glue te ayuda a mover y transformar datos de diversas fuentes a un formato adecuado para análisis, informes y almacenamiento de datos. Esto incluye la limpieza, enriquecimiento y transformación de datos.

Sin servidor: AWS Glue es un servicio sin servidor, lo que significa que no necesitas aprovisionar ni administrar ninguna infraestructura. AWS se encarga de los recursos subyacentes, lo que te permite concentrarte en tus trabajos de ETL.

Catálogo de datos: Glue incluye un repositorio centralizado de metadatos llamado AWS Glue Data Catalog. Almacena metadatos sobre fuentes de datos, transformaciones y destinos. Este catálogo ayuda en la búsqueda y gestión de datos.

Crawling y descubrimiento: Glue puede descubrir y catalogar automáticamente metadatos sobre tus fuentes de datos, incluyendo bases de datos, data lakes y archivos planos. Utiliza rastreadores para analizar los datos y crear entradas de metadatos en el Data Catalog.
Creación de trabajos de ETL: Puedes utilizar la herramienta de creación de trabajos de ETL de AWS Glue, basada en Apache Spark, para crear trabajos de ETL visualmente o mediante código (Python o Scala). Esto te permite definir la lógica de transformación de tus datos.

Transformación de datos: Glue admite una amplia gama de tareas de transformación de datos, incluyendo limpieza de datos, filtrado, agregación y mapeo de esquemas. Puede manejar datos semiestructurados y estructurados.

Movimiento de datos: Glue puede mover datos entre diversos almacenes de datos, incluyendo Amazon S3, Amazon RDS, Amazon Redshift y más. También admite el movimiento de datos entre recursos locales y en AWS.

rabajos programados: Puedes programar trabajos de ETL para que se ejecuten en momentos específicos o en respuesta a eventos. Esto te permite automatizar tus flujos de trabajo de procesamiento de datos.

Monitoreo y registro: AWS Glue proporciona capacidades de monitoreo y registro, incluyendo integración con métricas de CloudWatch y registros de CloudWatch, para que puedas hacer un seguimiento del progreso y la salud de tus trabajos de ETL.

Seguridad: Glue ofrece funciones como cifrado de datos, control de acceso e integración con AWS Identity and Access Management (IAM) para garantizar la seguridad de tus datos y procesos de ETL.

Integración: Se integra perfectamente con otros servicios de AWS como AWS Lambda, Amazon Athena, Amazon QuickSight y más, convirtiéndose en parte de un ecosistema más amplio para análisis de datos e inteligencia empresarial