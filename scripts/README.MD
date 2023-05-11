# `scripts`
## Bash scripts
### `preprocess.sh`
Configures the environment, downloads the initial dataset
### `eda.sh`
Extracts necessary data for EDA. Used in *Stage 3*.
### `stage1.sh`
Constructs the Postgres database, uploads to HDFS via Sqoop
### `stage2.sh`
Builds the Hive database using AVSC schema, created earlier.
### `stage3.sh`
EDA and PDA. Constructs the CSV tables that are used in the dashboard.
### `stage4.sh`
Streamlit dashboard initialization.
## Python scripts
### `preprocess.py`
Filters unnecessary columns, `null` and malformed data. Uses `pandas`.
### `models.py`
Contains training and evaluation process for regression models.
### `slit.py`
Creates the Streamlit dashboard.
