# Arquitectura Kappa
La arquitectura Kappa es un patrón de diseño utilizado en sistemas de procesamiento de datos en tiempo real y aplicaciones de transmisión de eventos. Esta arquitectura se utiliza comúnmente en el contexto de la ingesta, procesamiento y análisis de flujos de datos en tiempo real, como los datos generados por sensores, aplicaciones de monitoreo en tiempo real, redes sociales y más.

A continuación, se describen los principales componentes y características de la arquitectura Kappa:

Ingesta de datos: En la arquitectura Kappa, los datos se ingieren continuamente a través de un sistema de flujo de eventos, como Apache Kafka. Kafka es una plataforma de transmisión de datos que permite la recopilación y el almacenamiento de eventos en tiempo real.

Procesamiento en tiempo real: Los datos ingresados se procesan en tiempo real utilizando herramientas de procesamiento de flujo de eventos, como Apache Flink, Apache Samza o Apache Storm. Estas herramientas permiten realizar cálculos y transformaciones en los datos en tiempo real a medida que fluyen a través del sistema.

Almacenamiento: En lugar de utilizar un sistema de almacenamiento tradicional, como bases de datos relacionales, la arquitectura Kappa a menudo utiliza sistemas de almacenamiento de eventos, como Apache Cassandra o bases de datos clave-valor distribuidas, para almacenar eventos procesados.

Re-procesamiento: Una característica clave de la arquitectura Kappa es la capacidad de volver a procesar los datos históricos en cualquier momento. Esto se logra

<img src="https://static.platzi.com/media/user_upload/kappa-2a1cfa55-e49f-4221-beed-be3331721d7b.jpg"
alt="arquitectira kappa" wight="300">

## Arquitectuta Batch
La arquitectura batch se refiere a un enfoque de procesamiento de datos en el que se recopilan, procesan y almacenan datos en lotes, en lugar de procesarlos en tiempo real como en las arquitecturas de flujo continuo. Este enfoque es comúnmente utilizado en sistemas que no requieren respuestas inmediatas y pueden tolerar cierto retraso en el procesamiento.

Aquí hay algunos aspectos clave de la arquitectura batch:

Recopilación de datos: En un sistema de arquitectura batch, los datos se recopilan y almacenan en lotes durante un período de tiempo específico o cuando se alcanza un cierto volumen. Esto puede incluir datos de diferentes fuentes, como bases de datos, registros de aplicaciones, archivos de registro, etc.

Procesamiento programado: En lugar de procesar los datos a medida que llegan, se programa un proceso de procesamiento por lotes para que se ejecute en intervalos regulares o según una programación predefinida. Durante este proceso, se aplican transformaciones y cálculos a los datos recopilados.

Almacenamiento de resultados: Una vez que se completa el procesamiento por lotes, los resultados se almacenan en un almacén de datos o se generan informes que pueden ser consultados posteriormente.

Tolerancia al retraso: La arquitectura batch se utiliza en situaciones donde no es crítico tener respuestas en tiempo real. Puede haber cierto retraso entre la recopilación de datos y la disponibilidad de resultados procesados.

Escalabilidad: La arquitectura batch es escalable y puede manejar grandes volúmenes de datos, pero a menudo requiere una planificación cuidadosa en términos de recursos y tiempos de ejecución.

Ejemplos de uso: La arquitectura batch se utiliza en una variedad de aplicaciones, como el procesamiento de nóminas, la generación de informes financieros, la agregación de datos para análisis empresariales y muchas otras tareas que no requieren una respuesta inmediata.

<img src="https://static.platzi.com/media/user_upload/batch-fc017463-8281-4421-bb8d-1aec61a8dfb6.jpg"
alt="arquitectira batch wight="300">

### Arquitectura Lambda
se refiere a un patrón de diseño que se utiliza comúnmente en sistemas de procesamiento de datos en tiempo real y aplicaciones de transmisión de eventos. No debe confundirse con la función de cómputo sin servidor de AWS Lambda, que es un servicio de cómputo en la nube de Amazon Web Services.

La arquitectura Lambda se basa en el principio de dividir el procesamiento de datos en dos vías separadas, una para el procesamiento en tiempo real y otra para el procesamiento a largo plazo o batch. Esta arquitectura se utiliza para resolver el desafío de combinar datos en tiempo real con datos históricos y realizar análisis avanzados en sistemas que generan flujos de eventos continuos. A continuación, se describen los componentes clave de la arquitectura Lambda:

Capa de procesamiento en tiempo real (Hot Path): En esta capa, los datos en tiempo real, como los eventos que llegan de sensores o aplicaciones en línea, se procesan de manera rápida y eficiente. Se utilizan tecnologías de procesamiento en tiempo real, como Apache Kafka, Apache Flink o Apache Storm, para procesar estos datos en función de las necesidades inmediatas.

Capa de procesamiento batch (Cold Path): En esta capa, los datos se almacenan a largo plazo y se procesan en lotes o de manera diferida. Los datos históricos y los datos en tiempo real se combinan y se almacenan en un sistema de almacenamiento duradero como un data lake o una base de datos. Luego, se pueden realizar análisis más profundos, como procesamiento de lote, agregación, generación de informes y entrenamiento de modelos de aprendizaje automático en estos datos.

Capa de coordinación: Esta capa se encarga de coordinar la interacción entre las capas de procesamiento en tiempo real y batch. Garantiza que los datos se integren adecuadamente y que los resultados de los análisis en tiempo real y en batch estén disponibles para su consulta y análisis.

Almacenamiento persistente: En la arquitectura Lambda, se utiliza un almacenamiento persistente para conservar tanto los datos en tiempo real como los históricos. Esto puede incluir sistemas de almacenamiento distribuido, bases de datos NoSQL, sistemas de archivos o data lakes.

La arquitectura Lambda permite a las organizaciones combinar el análisis en tiempo real con el análisis a largo plazo para obtener una comprensión completa de los datos y tomar decisiones informadas. Es especialmente útil en aplicaciones como el análisis de registros, la detección de anomalías, la monitorización en tiempo real, el análisis de redes sociales y muchas otras aplicaciones de Big Data en las que es esencial procesar y analizar datos en tiempo real y a largo plazo.

<img src="https://www.diegocalvo.es/wp-content/uploads/2017/11/arquitectura_lambda.png"
alt="arquitectira lambda" wight="300">