import pandas as pd

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(inputs={'measure1': float}, outputs={'measure3': float}, secrets={'delta': 'delta_in_letters'})
def tata(df: pd.DataFrame, delta):
    print(df)
    df['measure3'] = df['measure1'] + len(delta)
    print(df)
    return df
