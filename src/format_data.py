import pandas as pd
import json

def format_data(csv_filepath: str, json_filepath: str):
    '''
    Formats the raw input CSV data into a JSON string, and
    writes the result into a file.
    '''
    df = clean_data(csv_filepath)
    with open(json_filepath, 'w') as f:
       f.write(csv_to_json(df))

def clean_data(csv_filepath: str) -> pd.DataFrame:
    '''
    Reads the raw input CSV File and returns a cleaned and trimmed-down
    version of the file.
    '''
    df = pd.read_csv(csv_filepath, encoding='ISO-8859-1')

    # Dropping irrelevant columns and rows with NaN values
    columns_to_drop = ['Full_Market_Price',
                       'Address',
                       'VAT_Exclusive',
                       'Description_of_Property',
                       'Property_Size_Description']
    df_cleaned = df.drop(columns_to_drop, axis=1).dropna()

    # Sort dataframe by date in ascending order
    df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], dayfirst=True)

    # Replace Date attribute with Year attribute
    df_cleaned['Year'] = (df_cleaned['Date'].dt.year)
    df_cleaned = df_cleaned.drop('Date', axis=1)

    return df_cleaned

def csv_to_json(df: pd.DataFrame) -> str:
    '''
    Takes in a Pandas Dataframe and outputs a JSON String representing
    the data as the means of the prices for every possible combinations
    of the year and county.
    '''
    grouped_df = df.groupby(['Year','County'])
    mean_prices_by_county = grouped_df.mean()
    
    mean_prices_by_county = mean_prices_by_county.applymap(
        lambda x: str('%.2f' % x)
    )

    # Ordering the data in a 2-layered Python dictionary, then converting the dictionary to
    # a JSON string
    dict_data = mean_prices_by_county.reset_index().groupby('Year').apply(
        lambda x: x.set_index('County').to_dict(orient='index')
        ).to_dict()
    json_str = str(json.dumps(dict_data))
    return json_str