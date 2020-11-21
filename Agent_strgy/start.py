import numpy as np
import methods as mtd
INPUT_PARAMS = {'weather_condition' : 1 , 'rate_of_spread': 0.01 , 'restaurant_capacity' : 75 ,'un_employment_rate': 0.01,  'num_agents' : 100}
NUM_STRGY = 10

class agent:
    def __init__(self, strgy):
        self.strgy = strgy

class strgy:
    """docstring for ."""
    def __init__(self, weights):
        self.w = arg
        self.best_score = 0






if __name__ == "__main__":
#this is where the execution starts
    agents = mtd.compute_agent_strgy( NUM_STRGY , INPUT_PARAMS)
