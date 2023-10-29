import os
import time
import pandas as pd

from typing import NoReturn, Callable


ROOT_DIR = os.path.abspath(os.pardir)
df_columns = ['date', 'title', 'url']


def start(update_method: Callable, fn: str) -> NoReturn:
    check_is_file(fn)
    while True:
        try:
            update_method()
        except Exception as e:  # это конечно плохо, но хотя бы падать не будет  # NOQA
            # logger.error(e)
            pass
        time.sleep(1)


def save_new_data(new_df: pd.DataFrame, fn: str) -> NoReturn:
    old_df = pd.read_csv(fn, index_col=0)
    df = pd.concat([old_df, new_df]).drop_duplicates(subset=['title', 'url']).reset_index(drop=True)
    df.to_csv(fn)


def check_is_file(fn: str) -> NoReturn:
    if not os.path.isfile(fn):
        pd.DataFrame(columns=df_columns).to_csv(fn)
