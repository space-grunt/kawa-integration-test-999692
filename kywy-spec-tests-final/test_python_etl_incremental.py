import pandas as pd
import logging
import datetime

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(outputs={'stock': str,
                    'price': float,
                    'trade_date_time': datetime.datetime,
                    'trade_date': datetime.date
                   })
def execute_new_decorator(data_preview=False, incremental=False):
    script_logger = logging.getLogger('script-logger')
    script_logger.info('Python ETL test 123456789')
    c = ['price', 'stock', 'trade_date', 'trade_date_time']
    if data_preview:
        d = [
            [60.01, 'BNP', datetime.date(2023, 1, 1), datetime.datetime(2023, 1, 1, 11, 11, 11)],
            [213.31, 'AAPL', None, None],
        ]
        return pd.DataFrame(data=d, columns=c)
    d = []
    if incremental:
      script_logger.info('Incremental load')
      d = [[60.01, 'INCREMENTAL', datetime.date(2023, 1, 1), datetime.datetime(2023, 1, 1, 11, 11, 11)]]
    else:
      script_logger.info('Full refresh')
      d = [[60.01, 'BNP', datetime.date(2023, 1, 1), datetime.datetime(2023, 1, 1, 11, 11, 11)],
           [213.31, 'AAPL', datetime.date(2024, 1, 1), datetime.datetime(2024, 1, 1, 11, 11, 11)]]
    return pd.DataFrame(data=d, columns=c)