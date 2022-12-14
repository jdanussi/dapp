""" Docstring """

from sqlalchemy import create_engine, MetaData, Table, delete


def load_data_to_database(params, dframe):
    """Docstring"""

    user = params["user"]
    password = params["password"]
    host = params["host"]
    database = params["database"]

    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

    metadata = MetaData(bind=engine)

    with engine.connect().execution_options(autocommit=True) as conn:
        ost_list_items_table = Table("ost_list_items", metadata, autoload_with=engine)
        stmt = delete(ost_list_items_table).where(ost_list_items_table.c.list_id == 10)
        conn.execute(stmt)
        dframe.to_sql("ost_list_items", con=conn, if_exists="append", index=False)
