"""
todos los scripts que estan en este archivo fueron realizados en Apache zeppelin, todos funcionaron
espero que le saques mucho el provecho 
"""
#"%pyspark" Asi es como habilitas el interpreste en zeppelin
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate()) #se utiliza en el contexto de AWS Glue y Apache Spark para crear una instancia de GlueContext. 
