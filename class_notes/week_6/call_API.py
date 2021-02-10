# call_API.py

import pandas as pd

def call_API(n_data_pts,weather_type):
    """
    call_API() is a function that calls the ThingSpeak web API for a .csv file and returns a Pandas dataframe
    
    input: n_data_pts (number of data points to get from ThingSpeak, an integer), weather_type (weather type to query. Can be 'temperature', 'pressure', 'humidity' or 'rainfall', a string)
    
    output: df (a Pandas dataframe) with the results from ThingSpeak
    
    Example:
    
    n=2
    w_type="temperature"
    df = call_API(n, w_type)
    print(df)
    
                    created_at  entry_id  field4
0  2021-02-10 19:43:03 UTC   3237227    31.7
1  2021-02-10 19:44:03 UTC   3237228    31.4
    
    """
    d = {'temperature':'4','pressure':'6','humidity':'3','rainfall':'5'}
    field_num_str = d[weather_type]
    n_data_pts_str = str(n_data_pts)
    url = 'https://api.thingspeak.com/channels/12397/fields/' + field_num_str +'.csv?results=' + n_data_pts_str
    df = pd.read_csv(url)
    
    return df