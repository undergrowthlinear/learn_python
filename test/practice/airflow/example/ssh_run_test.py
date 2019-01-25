#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 17),
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
    'ssh_run_test', default_args=default_args,
    schedule_interval='*/10 * * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

# 注意最后的空格 必须要保留 如果使用Jinja template,最后的空格则不用
# airflow机制如此,(空格其实是用于转义)
t2 = SSHOperator(
    ssh_conn_id='ssh_gzxhop03_lc', # 指定conn_id
    # ssh_gzxhop03_lc在web界面的admin/connections下面进行配置
    task_id='ssh_run_script',
    command='sh /home/iyourcar_test/tools/test/test_script/hello_world.sh ',
    # 远程机器上的脚本文件
    dag=dag)


t2.set_upstream(t1)
