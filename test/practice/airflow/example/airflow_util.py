#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import pymysql
import subprocess
import time

#连接配置信息
config = {
     'host':'mysql-hadoop01-gz.lc',
     'port':3306,
     'user':'iyc_test',
     'password':'IYOURCAR88',
     'db':'airflow',
     'charset':'utf8',
     }

# 删除历史日志
def clear_log(num):
    print("Clear logs before {0} days ...".format(num))
    cmd = "find %s -maxdepth 1 -type d -mtime +%d | xargs -i rm -rf {}" 
    subprocess.call(cmd % ('./logs',num), shell=True)
    subprocess.call(cmd % ('./logs/scheduler',num), shell=True)

# 通过杀掉后台进程来关闭Airflow
def kill_airflow():
    print("Stoping Airflow ...")
    # exclude current file in case the file name contains keyword 'airflow'
    cmd = "ps -ef | grep -Ei 'airflow' | grep -v 'grep' | grep -v '%s' | awk '{print $2}' | xargs -i kill -9 {}" % (__file__.split('/')[-1])
    subprocess.call(cmd, shell=True)

# 启动Airflow 
def start_airflow():
    kill_airflow()
    time.sleep(3)

    print("Starting Airflow Webserver ...")
    subprocess.call("rm logs/webserver.log", shell=True)
    subprocess.call("nohup airflow webserver >>logs/webserver.log 2>&1 &", shell=True)
    
    print("Starting Airflow Scheduler ...")
    subprocess.call("rm logs/scheduler.log", shell=True)
    subprocess.call("nohup airflow scheduler >>logs/scheduler.log 2>&1 &", shell=True)

# 删除指定DAG ID在数据库中的全部信息。
# PS：因为SubDAG的命名方式为 parent_id.child_id ，所以也会把符合这种规则的SubDAG删除！
def delete_dag(dag_id):
    # 创建连接
    connection = pymysql.connect(**config)
    cursor = connection.cursor()

    sql="select dag_id from airflow.dag where (dag_id like '{}.%' and is_subdag=1) or dag_id='{}'".format(dag_id, dag_id)
    cursor.execute(sql)
    rs = cursor.fetchall()
    dags = [r[0] for r in rs ] 

    for dag in dags:
        for tab in ["xcom", "task_instance", "sla_miss", "log", "job", "dag_run", "dag_stats", "dag" ]:
            sql="delete from airflow.{} where dag_id='{}'".format(tab, dag)
            print(sql)
            cursor.execute(sql)

    connection.commit()
    connection.close()

#
def main_process():
    parser = argparse.ArgumentParser()

    parser.add_argument("-k", "--kill", help="关闭Airflow", action='store_true')
    parser.add_argument("-s", "--start", help="启动Airflow", action='store_true')
    parser.add_argument("--clear", help="删除历史日志", type=int)
    parser.add_argument("--delete", help="提供需要删除的DAG ID")

    args = parser.parse_args()

    if args.kill:
        kill_airflow()
    if args.start:
        start_airflow()
    if args.clear:
        clear_log(args.clear)
    if args.delete:
        delete_dag(args.delete)

if __name__ == '__main__':
    main_process()


