# user_input.py

def user_input():
    w_type = input(f'What weather data are you looking for? ')
    dp = input(f'How many data points should be collected? ' )
    n = int(dp)
    return w_type, n
