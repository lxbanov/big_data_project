import argparse
import os
import logging
import pandas as pd
import numpy as np

from typing import Dict

def preprocess(data) -> Dict[str, pd.DataFrame]:
    """Preprocess data to be loaded to database

    Args:
        data (pd.DataFrame): Dataframe read from .csv source file

    Returns:
        Dict[str, pd.DataFrame]: 
            A dictionary that maps filenames to dataframes (provides a
            way to have multiple files as an output)
    """
    columns = [
        "q_unix_time",
        "q_read_time",
        "q_date",
        "q_time_h",
        "underlying_last",
        "expire_date",
        "expire_unix", 
        "dte",
        "c_delta",
        "c_gamma",
        "c_vega",
        "c_theta",
        "c_rho",
        "c_iv",
        "c_volume",
        "c_last",
	"c_size",
        "c_bid",
        "c_ask",
        "strike",
	"p_bid",
        "p_ask",
        "p_size",
        "p_last",
        "p_delta",
        "p_gamma",
	"p_vega",
        "p_theta",
        "p_rho",
        "p_iv",
        "p_volume",
        "strike_distance",
        "strike_distance_pct"
    ]
    full_data = pd.DataFrame(columns=columns)
    for chunk in data:
        chunk = chunk[chunk.notna()]
        chunk = chunk[chunk.notnull()]
        chunk.columns = columns
        full_data = pd.concat([full_data, chunk], axis=0, join='inner', copy=False)
    return {'data': full_data}


parser = argparse.ArgumentParser("Preprocess")
parser.add_argument("-i", help="Input .csv file to be preprocessed", required=True)
parser.add_argument("-o", help="Output directory for the results to be saved in", required=True)

logging.basicConfig()
logger = logging.getLogger()
    
if __name__ == '__main__':
    args = parser.parse_args()

    if not os.path.exists(args.i):
        os.makedirs(
            os.path.dirname(args.i),
            exist_ok=True
        )
    
    if not os.path.exists(args.o):
        os.makedirs(
            args.o,
            exist_ok=True
        )

    logger.info("Processing data...")
    files = preprocess(pd.read_csv(args.i, chunksize=10**5, low_memory=False, na_values=['', ' ']))
    for file_name, df in files.items():
        logger.info(f"Saving {file_name}...")
        df.to_csv(f'{os.path.join(args.o, file_name)}.csv', chunksize=10**5)
    logger.info("Done.")
    
    
