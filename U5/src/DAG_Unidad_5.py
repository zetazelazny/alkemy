# Import the libraries
import logging
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
import pandas as pd

# Defining DAG arguments

default_args = {
 'owner': 'Alkemy_Prisma',
 'start_date': days_ago(0),
 'email': ['some@somemail.com'],
 'email_on_failure': False,
 'email_on_retry': False,
 'retries': 1,
 'retry_delay': timedelta(minutes=5),
}


dag = DAG(
 'DAG_Unidad_5',
 default_args=default_args,
 description='My first DAG',
 schedule_interval=timedelta(days=1),
)

# Tasks


@dag.task(task_id="read_top10")
def read_top10():
    # ----- Completar logging ------

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('U5.log')
    
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(levelno)s - %(message)s')
    c_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)
    
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    # -----Fin Completar logging ------

    # Read CSV from web
    url = "http://winterolympicsmedals.com/medals.csv"

    try:

        df = pd.read_csv(url)

        # Get top 10 countries with most medals
        top_countries = df.NOC.value_counts().sort_values(ascending=False).head(10)

        # Convert pandas series to data frame
        to_countries_df = top_countries.to_frame()

        # Save data frame in Excel format - Completar tu propia ubicación para guardar el archivo de salida
        to_countries_df.to_excel('D:/Desktop/Prisma Run/Proyectos/U5/src/files/top10_medals_by_country.xlsx')

        # Logging message INFO Success --- Completar
        logger.info('...Archivo procesado correctamente...')

    except:
        # Logging message ERROR Fail --- Completar
        logger.error('No se pudo procesar el archivo', exc_info=True)


# task pipeline
read_top10()