
import pandas as pd 

# read the newly created complaints file for 2022
complaints_2022 = pd.read_csv('us_consumer_complaints_2022.csv')

def get_complaints_2022_companies(data: pd.DataFrame) -> dict[str:int]:
    '''
        find all companies and the number of complaints they had in 2022
    '''
    all_complaints = {}
    for n in data.index:
        complaint = data.loc[n, 'company']
        if complaint not in all_complaints:
            all_complaints[complaint] = 1
        else:
            all_complaints[complaint] += 1
    
    return all_complaints

c_2022 = get_complaints_2022_companies(complaints_2022)











