# user_input.py

def user_input():
    """
    user_input() is a function that asks a user for a weather type and number of data points. The function outputs these choices as function output
    
    input: None (the user is asked for input in the body of the function, not included as input arguments to the function)
    
    output: n_int (an integer), w_type (a string, one of four weather types 'temperature','pressure','humidity','rainfall')
    
    example:
    
    n, w_type = user_input()
    
        Which weather type (temperature, humidity, rainfall or pressure)? temperature
        How many data points (maximum of 8000)? 800
    
    """
    w_type = input('Which weather type (temperature, humidity, rainfall or pressure)? ')
    n_str = input('How many data points (maximum of 8000)? ')     # the input function outputs a string
    n_int = int(n_str)                                           # convert the string to an integer
    
    return n_int, w_type
