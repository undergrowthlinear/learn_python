--dwd_abtest_day_user
SELECT count(uid) FROM dwd_abtest_day_user where d="${hiveconf:day}" ;