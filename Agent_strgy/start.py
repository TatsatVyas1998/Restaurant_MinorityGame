import numpy as np
import methods as mtd
import random
INPUT_PARAMS = {'weather_condition' : 1 , 'rate_of_spread': .5 , 'restaurant_capacity' : 100 ,'un_employment_rate': 0.1,  'num_agents' : 100 , 'num_rounds' : 20}
NUM_STRGY = 10
NUM_RESTAURANTS = 60 #Estimated number of rastaurants in the are
AVG_RESTAURANT_CAP= 40 #average restaurant capacity in the area
population= 100
class agent:
    def __init__(self, strgy):
        self.strgy = strgy
        self.top_strgy = random.randint(0,9) #giving random strategy the best strategy
        self.top_strgy_score = 0
    def best_strgy(idx):
        self.top_strgy = idx
    def increase_top_score():
        self.top_strgy_score +=1
    def decrease_top_score():
        self.top_strgy_score = max(0,self.top_strgy_score-1)


class strgy:
    """docstring for ."""
    def __init__(self, weights):
        self.w = arg
        self.best_score = 0






if __name__ == "__main__":
#this is where the execution starts
    agents = mtd.compute_agent_strgy( NUM_STRGY , INPUT_PARAMS )
    Global_mem = mtd.compute_random_mem(population)#redomly generated memory at the begining
    thrs_hold = mtd.compute_thrshold(NUM_RESTAURANTS, AVG_RESTAURANT_CAP, INPUT_PARAMS)
    for _ in range(0,INPUT_PARAMS['num_rounds']):
        agent_decision , num_going , num_notgoing = mtd.compute_agent_decision(agents, Global_mem ,thrs_hold)
        #supply agent decisions to sub-team one and obtain the actual agent_decisions
        #you store the num_goint here( it is the variable that tell you how many agents have decided to go out this round)
        winner_loser = mtd.get_winner_loosers( agent_decision, num_going, num_notgoing)
        

    #print(agent_decision)
    #print(winner_loser)
    #print(Global_mem)
