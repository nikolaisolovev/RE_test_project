import pandas as pd
import openpyxl


rep_df = pd.read_excel('data.xlsx')
ozon_df = rep_df[rep_df.Источник == 'Ozon']


def calculate_kgt(row):
    length = max(row['Длина'], row['Ширина'])
    width = min(row['Длина'], row['Ширина'])
    height = row['Высота']
    weight = row['Вес']

    if pd.isna(length) or pd.isna(width) or pd.isna(height) or pd.isna(weight) or pd.isna(weight):
        return 'Габариты отсутствуют'

    ovh = (length * width * height) / 5000

    if ovh > weight:
        ovh = weight

    if length > 180 or width > 80 or ovh >= 25:
        return 'КГТ'
    else:
        return 'не КГТ'


ozon_df['признак КГТ'] = ozon_df.apply(calculate_kgt, axis=1)

rep_df.update(ozon_df)
rep_df.to_excel('data_with_kgt.xlsx', index=False)
