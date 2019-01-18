#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.subdag_operator import SubDagOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

PARENT_DAG_NAME = 'main_sub_dag_test'
#CHILD_DAG_NAME = 'child_dag'

default_args = {
    'owner': '测试',
    'depends_on_past': False,
}

main_dag = DAG(
    dag_id=PARENT_DAG_NAME,
    default_args=default_args,
    description='测试-内嵌SubDAG',
    start_date=datetime(2019,1,18,0,0,0),
    schedule_interval='*/30 * * * *'
)


# Dag is returned by a factory method
def sub_dag(parent_dag_name, child_dag_name, start_date, schedule_interval):
    dag = DAG(
        '%s.%s' % (parent_dag_name, child_dag_name),
        schedule_interval=schedule_interval,
        start_date=start_date,
        )

    t1 = BashOperator(
        task_id='print_{}'.format(child_dag_name),
        bash_command='echo sub key_{}  `date` >> /home/iyourcar_test/tools/airflow_rela/example/test_log/test.log'.format(child_dag_name),
        dag=dag)

    return dag

#
sub_dag_1 = SubDagOperator(
    subdag=sub_dag(PARENT_DAG_NAME, 'child_01', main_dag.start_date, main_dag.schedule_interval),
    task_id='child_01',
    dag=main_dag,
)

sub_dag_2 = SubDagOperator(
    subdag=sub_dag(PARENT_DAG_NAME, 'child_02', main_dag.start_date, main_dag.schedule_interval),
    task_id='child_02',
    dag=main_dag,
)

#
sub_dag_1 >> sub_dag_2
