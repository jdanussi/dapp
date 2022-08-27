""" Docstring """

import os
from dapp import get_data_from_database, transform_data, load_data_to_database
from dapp import config
from dapp import RESOURCES_DIR, CONFIGURATION_FILE


def main():
    """Docstring"""
    params_src = config(filename=CONFIGURATION_FILE, section="Argensun-Prueba")
    params_dst = config(filename=CONFIGURATION_FILE, section="ost_reclamos_dev")
    csv_raw = os.path.join(RESOURCES_DIR, "csv_raw.csv")
    csv_tra = os.path.join(RESOURCES_DIR, "csv_tra.csv")

    load_data_to_database(
        params_dst, transform_data(get_data_from_database(params_src, csv_raw), csv_tra)
    )


if __name__ == "__main__":
    main()
