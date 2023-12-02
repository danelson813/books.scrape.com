import pyarrow.feather as feather
import pyarrow.parquet as pq
import pyarrow as pa
import csv
import pandas as pd

import duckdb

df = pd.read_csv("data/results.csv")

feather.write_feather(df, "data/results.feather")

df.to_pickle("data/results.pkl")

df.to_parquet("data/results.parquet")

table = pa.Table.from_pandas(df)
pq.write_table(table, "data/results.arrow")

conn = duckdb.connect()
conn.execute(
    """
        DROP VIEW IF EXISTS binance_btc;
             """
)
conn.execute(
    """
        CREATE VIEW binance_btc AS
        SELECT * FROM  'data/results.parquet'
    """
)
