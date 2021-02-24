# call_API.py

import pandas as pd

N_DATA_PTS = 10
WEATHER_TYPE = 'pressure'

def call_API(n_data_pts, weather_type):
    """
    call_API() calls thinkspeak web api for a .csv file and returns a pandas date frame

    input: n_data_pts (numer of data points to get from thingspeak, must be integer), 
    weather_type (weather type to query. can be temperature, pressure, humidity or rainfall must be string)

    output: df(pandas dataframe) with the results from thingspeak
    example:

    """
    
    d = {'temperature':'4','pressure':'6','humidity':'3','rainfall':'5'}
    try:
        field_num_str = d[weather_type]
    except:
        field_num_str = '4'
    n_data_pts_str = str(n_data_pts)
    url = 'https://api.thingspeak.com/channels/12397/fields/' + field_num_str + '.csv?results=' + n_data_pts_str
    df = pd.read_csv(url)
    
    return df
