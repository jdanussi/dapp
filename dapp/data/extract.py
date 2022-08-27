# extract.py
""" Docstring """

import pandas as pd
from sqlalchemy import create_engine


def get_data_from_database(params, csv_file):
    """Docstring"""

    user = params["user"]
    password = params["password"]
    host = params["host"]
    database = params["database"]

    engine = create_engine(f"mssql+pymssql://{user}:{password}@{host}/{database}")

    with engine.connect().execution_options(autocommit=True):
        stmt = "SELECT * FROM ct_clientes"
        records = engine.execute(stmt)
        cols = records.keys()
        dframe = pd.DataFrame(records, columns=cols)

    dframe.to_csv(csv_file, encoding="utf-8", index=False)
    return dframe
