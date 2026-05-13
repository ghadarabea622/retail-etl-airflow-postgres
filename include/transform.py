import pandas as pd
import json

def transform_sales(df_csv):
    df_csv.columns =[c.lower().strip() for c in df_csv.columns]
    df_csv = df_csv.drop_duplicates()
    df_csv = df_csv.dropna()

    df_csv['sale_id'] = df_csv['sale_id'].astype(int)
    df_csv['product_id'] = df_csv['product_id'].astype(int)
    df_csv['quantity'] = df_csv['quantity'].astype(int)
    df_csv['price'] = df_csv['price'].astype(float)

    return df_csv


def transform_products(df_api):
    df_api.columns =[c.lower().strip() for c in df_api.columns]

    for col in df_api.columns:
        df_api[col] = df_api[col].apply(
            lambda x: json.dumps(x) if isinstance(x, (dict, list)) else x
        )

    df_api.drop_duplicates(inplace=True)
    df_api.fillna('Unknown', inplace=True)

    return df_api