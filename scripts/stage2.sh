#!/bin/bash

hdfs dfs -test -d /project/avsc/ && hdfs dfs -rm -r /project/avsc/
hdfs dfs -rm -r -f /project/tesla_option_chain_opt 
hdfs dfs -mkdir	 /project/avsc
hdfs dfs -put ./avsc/*.avsc /project/avsc/

hive -f ./sql/db.hql > hive_results.txt
