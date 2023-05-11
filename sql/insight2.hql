USE project;
INSERT OVERWRITE LOCAL DIRECTORY './output/insight_2'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT q_unix_time,avg(strike),avg(c_bid),avg(c_last),avg(p_bid),avg(p_last)
FROM tesla_option_chain_opt
GROUP BY q_unix_time;
