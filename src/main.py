import pandas as pd

def read_data() -> pd.DataFrame:
    '''
    Reads the raw input CSV File and returns a cleaned version of the file.
    '''
    df = pd.read_csv('data/Raw_Input.csv', encoding='ISO-8859-1')

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

    print(df_cleaned['Price'].mean())

    with open('data/Cleaned_Input.csv','w') as f:
        f.write(df_cleaned.to_csv())

    return df_cleaned

def csv_to_json(df: pd.DataFrame) -> str:
    '''
    Takes in a Pandas Dataframe and outputs a JSON String representing
    the data as the means of the prices for every possible combinations
    of the year and county.
    '''
    grouped_df = df.groupby(['Year','County'])
    mean_prices_by_county = grouped_df.mean()
    json_data = mean_prices_by_county.reset_index().to_json(orient='records')
    return json_data

def main():
    json_filepath = 'data/mean_housing_prices_by_county.json'
    df = read_data()
    with open(json_filepath, 'w') as f:
       f.write(csv_to_json(df))

if __name__ == '__main__':
    main()