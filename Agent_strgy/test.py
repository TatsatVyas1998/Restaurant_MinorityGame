from database import database
import start as st

st.start_simulation({'weather_condition' : 5 , 'rate_of_spread': 2.5 , 'restaurant_capacity' : 75 ,'un_employment_rate': 0,  'num_agents' : 100 , 'num_rounds' : 100},100)
#print('parameters :', st.get_parameter_values(1))
#print('num going :', st.get_round_going(1))
#print('round_turnout :', st.get_round_turnout(1))
#st.clear_database()
