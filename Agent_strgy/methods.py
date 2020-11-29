import numpy as np
import start as st
import random

#this basically decides how each agen t will make decision
Mem = 5
def pram_scale(Input_param):

    Input_param['weather_condition'] = ((Input_param['weather_condition']*2)/10)
    Input_param['restaurant_capacity'] = Input_param['restaurant_capacity']/100
    Input_param['rate_of_spread'] = ((Input_param['rate_of_spread'])/3.5)    #3.5 is the max rate of spread reproted so far


def get_random_weight(Input_param):

    w1 = Input_param['weather_condition']* (random.randint(50,100 )/20)
    #print('weather_condition',w1)
    w2 = Input_param['restaurant_capacity']* (random.randint(50, 100)/100)
    #print('restaurant_capacity',w2)
    #print('w3', int(2+ Input_param['rate_of_spread']*100))
    w3 = Input_param['rate_of_spread']*(random.randint(60,100)/100)#int(1+ Input_param['rate_of_spread']*100))/100)
    #print('rate_of_spread',w3)
    w4 = Input_param['un_employment_rate']*(random.randint(1,100)/100)
    #print('un_employment_rate',w4)
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
    return[random.randint(40,population) for _ in range(0,Mem) ]

def compute_thrshold(NUM_RESTAURANTS, AVG_RESTAURANT_CAP, Input_param):
    #print(rst_capacity)
    return  int(Input_param['num_agents']*.5) # (NUM_RESTAURANTS*AVG_RESTAURANT_CAP * ((Input_param['restaurant_capacity']*100)/100))

def compute_agent_decision(agents, Global_mem ,thrs_hold):
    agent_decisions = []
    num_going = 0
    num_notgoing = 0
    for agent in agents:
        opt_strgy = agent.strgy[agent.top_strgy]
        #print(opt_strgy)
        expected_turnout = 0
        for i in range(0,len(opt_strgy)):
            expected_turnout += opt_strgy[i]*Global_mem[i]


        #print("expected turnout" ,int(expected_turnout*(1/len(opt_strgy))))
        #print("threshold", thrs_hold)
        if( int(expected_turnout*(1/len(opt_strgy))) < thrs_hold):
            agent_decisions.append(1)
            num_going +=1
        else:
            agent_decisions.append(0)
            num_notgoing +=1
    return agent_decisions , num_going ,num_notgoing

def get_winner_loosers( agent_decision, num_going, num_notgoing):
    not_g = False
    g = False
    win_loose_arr =[]
    if( num_notgoing > num_going):
        g = True
    else:
        not_g = True
    if( not_g is True):
        for i in range(0,len(agent_decision)):
            if( agent_decision[i]==0):
                win_loose_arr.append(1)
            else:
                win_loose_arr.append(0)

    if(g==True):
        win_loose_arr = agent_decision.copy()
    return(win_loose_arr)
