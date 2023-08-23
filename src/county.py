import json

class County:
    '''
    Class representing a county in the Republic of Ireland. Contains information
    about the average housing price on a given year.
    '''
    def __init__(self, name) -> None:
        self.__name = name
        self.__year = None
        self.__house_price_avg = None
        self.__location_in_json = None

    def get_year(self):
        return self.__year

    def update_year(self, new_year: str):
        '''
        Updates the year that is being accessed from the county's data.
        Updates the county's relevant attributes.
        '''
        self.__year = new_year
        json_filepath = 'data/mean_housing_prices_by_county.json'
        with open(json_filepath, 'r') as f:
            json_data = json.load(f)
            self.__location_in_json = json_data[str(self.__year)][self.__name]
            self.__house_price_avg = self.__location_in_json['Price']

    def get_name(self) -> str:
        return self.__name

    def get_avg_price(self) -> str:
        return self.__house_price_avg
    
def init_counties(county_list: list):
    '''
    Initialises the list of counties with all relevant
    county objects.
    '''
    with open('data/mean_housing_prices_by_county.json', 'r') as f:
        json_data = json.load(f)
        counties = dict(json_data)['2010'].keys()
        for c in counties:
            county_list.append(County(c))

def update_counties(county_list: list, year: str):
    '''
    Updates the year that is being accessed from
    every county in the list of counties.
    '''
    for c in county_list:
        c.update_year(year)