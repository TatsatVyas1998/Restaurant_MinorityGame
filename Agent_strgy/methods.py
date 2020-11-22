import numpy as np
import start as st
import random

#this basically decides how each agen t will make decision
Mem = 5
def pram_scale(Input_param):

    Input_param['weather_condition'] = ((Input_param['weather_condition']*2)/10) - 0.01
    Input_param['restaurant_capacity'] = Input_param['restaurant_capacity']/100
    Input_param['rate_of_spread'] = ((Input_param['rate_of_spread'])/3.5)    #3.5 is the max rate of spread reproted so far


def get_random_weight(Input_param):

    w1 = Input_param['weather_condition']* (random.randint(1,100 - int((Input_param['weather_condition']*100)))/16)
    #print('weather_condition',w1)
    w2 = Input_param['restaurant_capacity']* (random.randint(1, int(Input_param['restaurant_capacity']*100))/100)
    #print('rate_of_spred',Input_param['rate_of_spread'])
    #print('w3', int(2+ Input_param['rate_of_spread']*100))
    w3 = Input_param['rate_of_spread']*(random.randint(1,int(1+ Input_param['rate_of_spread']*100))/100)
    #print('rate_of_spread',w3)
    w4 = Input_param['un_employment_rate']*(random.randint(1,int(1+Input_param['un_employment_rate']*100))/100)

    return ((w1+w2-w3-w4)/2)

def compute_random_strgy(NUM_STRGY, Input_param):

    strgy_lst = []
    for _ in range(0,NUM_STRGY):
        temp = []
        for _ in range(0, Mem):
            temp.append( get_random_weight(Input_param) )
        strgy_lst.append(temp)
    #print(strgy_lst)
    return strgy_lst

def compute_agent_strgy(NUM_STRGY , Input_param):
    pram_scale(Input_param)
    #print(Input_param)
    agent_list = []
    for agent in range(0,Input_param['num_agents']):
        agent_list.append(st.agent(compute_random_strgy(NUM_STRGY , Input_param)))
    return agent_list


def compute_random_mem(population):
    return[random.randint(10,population) for _ in range(0,Mem) ]
