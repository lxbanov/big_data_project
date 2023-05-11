import pyspark
from pyspark.sql import SparkSession
from pyspark import sql
from pyspark import ml
import os

spark = SparkSession.builder\
                    .appName('BDT Project')\
                    .config('spark.sql.catalogImplementation', 'hive')\
                    .config('hive.metastore.uris', 'thrift://sandbox-hdp.hortonworks.com:9083')\
                    .config('spark.sql.avro.compression.codec', 'snappy')\
                    .enableHiveSupport()\
                    .getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

tesla_option_chain = spark.read.format('avro').table('project.tesla_option_chain_opt')
tesla_option_chain.createOrReplaceTempView('option_chain')

features = ['underlying_last','c_last', 'c_bid', 'c_ask', 'p_bid', 'p_ask', 'p_last']
target = 'strike'

assembler = ml.feature.VectorAssembler(inputCols=features, outputCol='features', handleInvalid='skip')
# tesla_option_chain.show()
data = assembler.transform(tesla_option_chain)
# data.show()
data = data.select(['features', 'strike'])

(train, test) = data.randomSplit([0.7, 0.3])

lr = ml.regression.LinearRegression(labelCol='strike')
evaluator = ml.evaluation.RegressionEvaluator(labelCol='strike', metricName='rmse')

param_grid_lr = ml.tuning.ParamGridBuilder()\
                .addGrid(lr.regParam, [0.1, 0.01])\
                .addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0])\
                .addGrid(lr.fitIntercept, [False, True])\
                .build()

cv_lr = ml.tuning.CrossValidator(estimator=lr,
                                estimatorParamMaps=param_grid_lr,
                                evaluator=evaluator,
                                numFolds=3
                                )
# train.show()

model_lr = cv_lr.fit(train)

pred_lr = model_lr.transform(test)

pred_lr.coalesce(1)\
        .select('prediction', 'strike')\
        .write\
        .mode('overwrite')\
        .format('csv')\
        .option('sep',',')\
        .option('header','true')\
        .csv('%s/output/lr_pred'%os.getcwd())

print('RMSE (Linear Regression): %f'%evaluator.evaluate(pred_lr))

rf = ml.regression.RandomForestRegressor(labelCol='strike')

param_grid_rf = ml.tuning.ParamGridBuilder()\
                .addGrid(rf.maxDepth, [3, 5])\
                .addGrid(rf.numTrees, [4, 8, 16])\
                .build()
cv_rf = ml.tuning.CrossValidator(estimator=rf,
                                estimatorParamMaps=param_grid_rf,
                                evaluator=evaluator,
                                numFolds=3
                                )
model_rf = cv_rf.fit(train)

pred_rf = model_rf.transform(test)

pred_rf.coalesce(1)\
        .select('prediction', 'strike')\
        .write\
        .mode('overwrite')\
        .format('csv')\
        .option('sep', ',')\
        .option('header', 'true')\
        .csv('%s/output/rf_pred'%os.getcwd())

print('RMSE (Random Forest): %f'%evaluator.evaluate(pred_rf))
