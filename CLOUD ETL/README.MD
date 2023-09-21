# ETL en AWS
Para realizar un proceso de ETL (Extraer, Transformar, Cargar) utilizando servicios de AWS y Apache Zeppelin, primero debemos configurar y utilizar AWS Glue, un servicio de AWS diseñado para facilitar este tipo de procesos. También utilizaremos AWS Athena para realizar consultas a la base de datos que crearemos durante el proceso. Antes de continuar, es importante tener conocimiento sobre qué es AWS Glue y cómo funciona. Puedes obtener más información sobre AWS Glue en la carpeta de ETL de este proyecto o mediante tus propias investigaciones.Ademas,en el repositorio encontraras un archivo docker-compose que te falitara la instalacion de Apache Zeppelin en tu computadora

A continuación, te guiaré a través de los pasos para realizar este proceso de ETL utilizando AWS Glue y Apache Zeppelin:

## :heart: Paso 1: Preparar tus Datos

Antes de comenzar, asegúrate de tener tus datos listos en un formato que AWS Glue pueda procesar. Pueden estar en S3, en una base de datos, o en otro lugar accesible desde AWS.
### :heart_eyes:Paso 2: Configurar AWS Glue

Inicia sesión en la consola de AWS y navega a la página de AWS Glue.
Crea un nuevo trabajo de Glue para definir cómo deseas extraer, transformar y cargar tus datos. Define las conexiones a las fuentes y destinos de datos.
Utiliza los scripts de transformación de Glue, que pueden estar escritos en Python o Scala, para realizar las transformaciones necesarias en tus datos.
Configura el destino de datos, que podría ser una base de datos en Amazon Redshift, Amazon RDS, Amazon S3 u otro servicio de AWS compatible.

#### :flushed: Paso 3: Ejecutar el Trabajo de Glue

Una vez que hayas configurado tu trabajo de Glue, puedes ejecutarlo para realizar el proceso de ETL. AWS Glue se encargará de la ejecución y monitorización de las tareas.

##### :dizzy_face: Conectar Apache Zeppelin a AWS
Inicia una instancia de Apache Zeppelin en AWS EC2 o en tu entorno local.
Configura las credenciales de AWS en Apache Zeppelin utilizando los roles IAM de EC2 o proporcionando tus credenciales de seguridad de AWS.
Importa o crea un notebook en Apache Zeppelin para escribir y ejecutar consultas.

###### :eyes: Consultas con AWS Athena
Para realizar un proceso de ETL (Extraer, Transformar, Cargar) utilizando servicios de AWS y Apache Zeppelin, primero debemos configurar y utilizar AWS Glue, un servicio de AWS diseñado para facilitar este tipo de procesos. También utilizaremos AWS Athena para realizar consultas a la base de datos que crearemos durante el proceso. Antes de continuar, es importante tener conocimiento sobre qué es AWS Glue y cómo funciona. Puedes obtener más información sobre AWS Glue en la carpeta de ETL de este proyecto o mediante tus propias investigaciones.

Recuerda siempre seguir las mejores prácticas de seguridad al configurar tus credenciales de AWS y mantener la privacidad y la integridad de tus datos.Tambien añado un link donde pueden consultar mas sobre AWS GLUE
job en aws glue es la que hace la tarea de transformacion

https://medium.com/@milton32sanabria/construyendo-un-etl-en-aws-glue-6601309be3cb

athena se conecta al glu catalo,esto le dice donde esta la data en s3,basado en sql, para hacer consultas sql,cuando se dice que es serveless quiere decir que no tiene carga de administarcion o crear servidores para usar este servicio de aws,

este servicio tiene integracion nativa con ,AWS GLUE,REDSHIT,S3,DYNAMODB

