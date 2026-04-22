EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time expected"

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    reamining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return reamining_bake_time
    
PREPARATION_TIME = 2
def preparation_time_in_minutes(number_of_layers):
    """determines the time a lasagne needs to cook based on its layers

    parameters:
    number_of_layers : an integer 

    returns:
    (int): minutes 
    """
    minutes = PREPARATION_TIME * number_of_layers
    return minutes
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    
    """
    elapsed_time = 40 + preparation_time_in_minutes(number_of_layers) -        bake_time_remaining(elapsed_bake_time)
    return elapsed_time
    

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
