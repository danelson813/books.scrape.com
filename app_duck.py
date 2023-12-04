import duckdb
import pandas as pd

def create_tables():
    duckdb.sql("CREATE TABLE t1(id INTEGER PRIMARY KEY, j VARCHAR)")
    results = duckdb.sql("select * from t1")
    return results

def populating_tables():
    duckdb.sql("insert into t1(id,j) values(1,2)")
    results = duckdb.sql("select * from t1")
    return results

def populating_tables2():
    my_df = pd.DataFrame.from_dict({'a': [1,2,3,4,5,6,7,8,9]})
    duckdb.sql("CREATE TABLE my_table AS SELECT * FROM my_df")
    results = duckdb.sql('select * from my_table')
    return results

def insert_from_existing_table():
    my_df2 = pd.DataFrame.from_dict({'a': [99,100,101,102,103]})
    duckdb.sql("INSERT INTO my_table SELECT * FROM my_df2")
    results = duckdb.sql("select * from my_table")
    return results


def deleting_data():
    duckdb.sql("delete from my_table where a in (1,2,3,4,5)")
    results = duckdb.sql("select * from my_table")
    return results


if __name__ == '__main__':
    create_tables()
    print(populating_tables())
    print('***'* 25)
    print(populating_tables2())
    print('***'* 25)
    print(insert_from_existing_table())
    print('***'* 25)
    print(deleting_data())
