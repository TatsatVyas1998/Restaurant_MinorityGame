import numpy as np
import methods as mtd
import random
INPUT_PARAMS = {'weather_condition' : 5 , 'rate_of_spread': 0.8 , 'restaurant_capacity' : 25 ,'un_employment_rate': 0.8,  'num_agents' : 100}
NUM_STRGY = 10
population= 1000
class agent:
    def __init__(self, strgy):
        self.strgy = strgy
        self.top_strgy = random.randint(0,9) #giving random strategy the best strategy
    def best_strgy(idx):
        self.top_strgy = idx

class strgy:
    """docstring for ."""
    def __init__(self, weights):
        self.w = arg
        self.best_score = 0






if __name__ == "__main__":
#this is where the execution starts
    agents = mtd.compute_agent_strgy( NUM_STRGY , INPUT_PARAMS)
    Global_mem = mtd.compute_random_mem(population)#redomly generated memory at the begining
    
