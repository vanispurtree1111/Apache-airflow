from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDragOperator

def download_tasks():

    with DAG(f"{parent_dag_id}.{child_dag_id}",
             start_date = args['start_date'],
             schedule_interval= args['schedule_interval'],
             catchup=args['catchup']) as dag:
             
             download_a = BashOperator(
                    task_id='download_a',
                    bash_command ='sleep 10'
             )

             download_b = BashOperator(
                    task_id='download_a',
                    bash_command ='sleep 10'
             )

             download_c = BashOperator(
                    task_id='download_a',
                    bash_command ='sleep 10'
             )