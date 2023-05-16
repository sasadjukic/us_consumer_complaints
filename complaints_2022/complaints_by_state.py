
# import necessary libraries and modules
import pandas as pd
from usa_states import states
from main_2022 import complaints_2022
from ccr_agencies import ccra

def exclude_ccra(data: pd.DataFrame) -> pd.DataFrame:
    '''return a new data sheet excluding ccr agencies'''
    non_ccra = data[~data['company'].isin(ccra)]
    return non_ccra

def find_complaints_in_states_not_ccra(data: pd.DataFrame, states: dict[str:dict]) -> dict[str:dict]:
    '''find what companies logged most complaints in each US state for 2022, excluding ccr agencies'''

    for i in data.index:
        state = data.loc[i, 'state']
        company = data.loc[i, 'company']
        if company not in states[state]:
            states[state][company] = 1
        else:
            states[state][company] += 1

    return states

def get_highest_complaints_by_state(complaints: dict[str:dict]) -> dict[str:str]:
    '''find a company people complaint the most in each state in 2022(not including ccr agencies)'''
    top_complaints = {}

    for key, value in complaints.items():
        top_complaints[key] = sorted(value.items(), key = lambda x: x[1], reverse=True)[0][0]

    return top_complaints

non_ccra = exclude_ccra(complaints_2022)
state_complaints = find_complaints_in_states_not_ccra(non_ccra, states)
top_complaints_by_state = get_highest_complaints_by_state(state_complaints)

for key, value in top_complaints_by_state.items():
    print(key, value)