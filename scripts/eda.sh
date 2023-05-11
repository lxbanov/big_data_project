rm -rf $(find ./output -name "*insight*")
hive -f "./sql/insight1.hql"
echo "x,y" > './output/insight_1.csv'
cat $(ls -v ./output/insight_1/*) >> ./output/insight_1.csv
hive -f "./sql/insight2.hql"
echo "x,strike,c_bid,c_last,p_bid,p_last" > './output/insight_2.csv'
cat $(ls -v ./output/insight_2/*) >> ./output/insight_2.csv
hive -f "./sql/insight3.hql"
echo "strike,underlying_last,expire_unix,dte,c_volume,c_last,c_size,c_bid,c_ask,p_volume,p_last,p_size,p_bid,p_ask" > './output/insight_3.csv'
cat $(ls -v ./output/insight_3/*) >> ./output/insight_3.csv
hive -f "./sql/insight4.hql"
echo "num_options,lifetime_days" > './output/insight_4.csv'
cat $(ls -v ./output/insight_4/*) >> ./output/insight_4.csv
