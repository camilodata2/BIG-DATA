# Msk
Este servicio es Apache Kafka administrado en la nube de AWS.
MSK se despliega en un clúster, el cual está compuesto de broker nodes y zookeeper nodes para orquestar el procesamiento de información.

Conceptos importantes

Broker nodes: Al crear el clúster debemos especificar la cantidad de nodos por zona de disponibilidad. Con esto, el clúster se convierte en un multi-zona brindándonos una muy alta disponibilidad.
Zookeeper: Ayuda a mantener la configuración, datos de nombres, sincronización, rotación e integración con otros servicios.
Zookeeper nodes: Por defecto, al crear el clúster de MSK, se crea un nodo de Zookeeper.

Los conceptos que manejamos en esta arquitectura son muy parecidos a los que tenemos en Kinesis Data Stream (Producer, Clúster, Consumer).

MSK vs Kinesis
Lo que recomienda Amazon es:

Utiliza Kinesis si necesitas una fuerte integración con otros servicios dentro de AWS.
Utiliza MSK si necesitas una fuerte integración con sistemas de terceros con Open Source y mayor flexibilidad.

En conclusión, con Kinesis Data Stream tendremos un producto más administrado, coordinado y sincronizado con otros servicios de AWS, pero en MSK tendremos más flexibilidad la cual incluye consigo mayor carga de administración (porque básicamente lo que se despliega en MSK es un clúster).
