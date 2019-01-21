# 常用命令说明
- airflow -h/version
- eg:操作
```
airflow list_dags
airflow list_tasks ssh_run_test
airflow test ssh_run_test print_date 20190121
airflow test ssh_run_test ssh_run_script 20190121
airflow backfill ssh_run_test -s 20190120 -e 20190121
```
