import pandas as pd
import numpy as np

class County:
    '''
    Class representing a county in the Republic of Ireland. Contains information
    about the average housing price over a span of several years.
    '''
    def __init__(self, name) -> None:
        self.__name = name
        self.__year = None
        self.__avg_price_list = None

    def get_year(self):
        return self.__year

    def update_year(self, new_year: str):
        '''
        Updates the year that is being accessed from the county's data.
        Updates the county's relevant attributes.
        '''
        self.__year = new_year
        csv_filepath = 'data/cleaned_csv.csv'
        df = pd.read_csv(csv_filepath)
        self.__avg_price_list = df[self.__name].tolist()

    def get_name(self) -> str:
        return self.__name

    def get_avg_prices(self) -> str:
        return self.__avg_price_list
    
def get_county_by_name(county_list: list, name: str):
    '''
    Searches for a County object in a list of counties by name.
    '''
    for c in county_list:
        if c.get_name() == name:
            return c
    return None

def init_counties(county_list: list):
    '''
    Initialises the list of counties with all relevant
    county objects.
    '''
    csv_filepath = 'data/cleaned_csv.csv'
    df = pd.read_csv(csv_filepath)
    county_names = df.columns.tolist()[1:]
    for c in county_names:
        county_list.append(County(c))

def update_counties(county_list: list, year: str):
    '''
    Updates the year that is being accessed from
    every county in the list of counties.
    '''
    for c in county_list:
        c.update_year(year)