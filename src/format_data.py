import pandas as pd
import json

def format_data(csv_filepath: str, json_filepath: str):
    '''
    Formats the raw input CSV data into a new CSV file,
    containing the average house prices for each county
    for each year represented by this program.
    '''
    df = clean_data(csv_filepath)
    create_new_csv(df)

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

def create_new_csv(df: pd.DataFrame):
    '''
    Takes in a Pandas cleaned Dataframe and outputs a CSV
    containing the average house prices for each county
    for each year represented by this program.
    '''
    #print(df)
    grouped_df = df.groupby(['Year','County'])
    mean_prices_by_county = grouped_df.mean()
    
    # Formatting the mean values to two decimal places
    mean_prices_by_county = mean_prices_by_county.applymap(
        lambda x: str('%.2f' % x)
    )

    mean_prices_by_county.reset_index(inplace=True)
    new_df = mean_prices_by_county.pivot(index='Year', columns='County', values='Price')
    new_df.to_csv('data/cleaned_csv.csv')