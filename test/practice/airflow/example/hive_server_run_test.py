#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.hive_operator import HiveOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 21),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    'hive_server_run_test', default_args=default_args,
    schedule_interval='*/10 * * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

hql_file = 'c_day_user.hql'

t2 = HiveOperator(
    hive_cli_conn_id='hiveserver2_default',  # 指定conn_id
    # hive_cli_default在web界面的admin/connections下面进行配置
    task_id='hive_server_run',
    # 通过 `-hiveconf "key"="value"`` 接收参数
    hql=hql_file,
    # 设置使用的数据库
    schema='iyourcar',
    hiveconfs={'day': '2019-01-14'},
    # 设置mr运行队列 default
    mapred_queue='dailyHour',
    mapred_job_name='count_day_user_20190114',
    dag=dag)

t2.set_upstream(t1)
