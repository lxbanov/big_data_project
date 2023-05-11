USE project;
INSERT OVERWRITE LOCAL DIRECTORY './output/insight_1'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT q_unix_time, avg(strike) FROM tesla_option_chain_opt
GROUP BY q_unix_time
ORDER BY q_unix_time;
