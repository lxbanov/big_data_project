# TESLA Option Prediction Pipeline

This repository contains a pipeline developed to build regressor models and predict strike prices of options. The pipeline consists of data preprocessing, data loading, model construction and visualization. We used a Hadoop ecosystem: SparkML, HIVE, Sqoop, PostgreSQL, Streamlit to create this pipeline. 

## Dataset

The dataset used comprises of several millions options published on the market in the period from 2019 to 2022. The description of the dataset can be found here: https://www.optionsdx.com/option-chain-field-definitions/. And the source dataset is available here: https://www.optionsdx.com/option-chain-field-definitions/.

## Pipeline

To run pipeline you might run the following script:

```
bash main.sh
```

That will run the whole pipeline stage by stage. Intermediate outputs will be available in the folder `output`. After running the whole pipeline a Streamlit application would be run and available for you to explore insights and results

