# Extraccion de informacion
Esta es el comienzo de un gran viaje hacia como es el proceso de extraccion de la data, lo primero
que debemos de hacer es usar la SDK de AWS para python y la SDK es llamda boto3, pero no te preocupes, si no eres muy afin a python puedes usar otro lenguaje de programacion como java,.NET entre otros.Ademas, hay algo llamado AWS CLI que es lo que nos permite conecternos a los servicios de AWS desde nuestra PC o si lo deseas puedes usar las shell que te provee AWS, pero para esto debes de configurar AWS IAM, y tambien algo llamado AWS MFA

## ¿Que es AWS cloud9
AWS Cloud9 es un entorno de desarrollo integrado (IDE) en la nube proporcionado por Amazon Web Services (AWS). Ofrece una plataforma basada en la web que permite a los desarrolladores escribir, depurar y ejecutar código en la nube sin necesidad de configurar ni mantener un entorno de desarrollo local. Algunas de las características clave de AWS Cloud9 incluyen:

Editor de código en línea: Cloud9 proporciona un editor de código en línea con resaltado de sintaxis, autocompletado y otras características de edición para varios lenguajes de programación, lo que facilita la escritura de código.

Entornos de desarrollo preconfigurados: Puedes crear entornos de desarrollo preconfigurados para diferentes lenguajes y plataformas. AWS Cloud9 incluye soporte para una variedad de lenguajes de programación, incluidos Python, JavaScript, Ruby, Java y más.

Integración con AWS: Cloud9 está integrado con otros servicios de AWS, lo que facilita la creación, el despliegue y la depuración de aplicaciones en la nube de AWS. Puedes acceder directamente a recursos de AWS, como instancias EC2 y bases de datos RDS, desde tu entorno de desarrollo.

Colaboración en tiempo real: Permite la colaboración en tiempo real, lo que significa que varios desarrolladores pueden trabajar juntos en el mismo proyecto de manera simultánea, lo que facilita la colaboración en equipos distribuidos.

Terminal integrada: Incluye una terminal integrada que te permite ejecutar comandos directamente en tu entorno de desarrollo.

Control de versiones: Soporta sistemas de control de versiones como Git, lo que facilita la gestión y colaboración en proyectos con control de versiones.

Personalización: Puedes personalizar tu entorno de desarrollo instalando herramientas y configuraciones adicionales según tus necesidades específicas.

AWS Cloud9 es especialmente útil para desarrolladores que desean trabajar en la nube, colaborar con otros desarrolladores de forma remota y utilizar los servicios de AWS de manera integrada en su flujo de trabajo de desarrollo. Puedes acceder a AWS Cloud9 a través del panel de control de AWS y comenzar a usarlo para desarrollar aplicaciones en la nube de AWS.

### Boto3
Boto3 es la biblioteca de software oficial de Python proporcionada por Amazon Web Services (AWS) para interactuar con los servicios de AWS a través de programación. Permite a los desarrolladores de Python acceder y administrar los recursos y servicios de AWS de manera programática, lo que facilita la automatización de tareas y la integración de servicios de AWS en aplicaciones y scripts Python.

Aquí hay algunas de las características y usos comunes de Boto3:

Acceso a servicios de AWS: Boto3 proporciona una API en Python para interactuar con una amplia variedad de servicios de AWS, como Amazon S3 (almacenamiento de objetos), Amazon EC2 (máquinas virtuales), Amazon RDS (bases de datos relacionales), Amazon DynamoDB (base de datos NoSQL), AWS Lambda (cómputo sin servidor), Amazon SQS (cola de mensajes), Amazon SNS (servicio de notificaciones), y muchos otros.

Gestión de recursos: Con Boto3, puedes crear, modificar y eliminar recursos en AWS, como instancias EC2, grupos de seguridad, buckets de S3, tablas de DynamoDB, entre otros.

Automatización: Boto3 es una herramienta poderosa para la automatización de tareas en AWS. Puedes escribir scripts que realicen acciones como la creación de instantáneas de copias de seguridad, la escalabilidad automática de recursos, la gestión de datos en la nube y más.

Integración: Boto3 es ampliamente utilizado para integrar servicios de AWS en aplicaciones y sistemas existentes. Puedes utilizarlo para crear aplicaciones web que interactúen con servicios de AWS, implementar flujos de trabajo de DevOps, o crear soluciones personalizadas en la nube de AWS.