from county import *
from format_data import *

def main():
    csv_filepath = 'data/Raw_Input.csv'
    json_filepath = 'data/mean_housing_prices_by_county.json'
    format_data(csv_filepath, json_filepath)

    counties = []
    init_counties(counties)
    update_counties(counties,'2015')
    print([(c.get_name(), c.get_avg_price()) for c in counties])

if __name__ == '__main__':
    main()