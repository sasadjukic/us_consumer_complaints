
import pandas as pd
from main_2022 import c_2022

def get_total_complaints_2022(companies: dict[str:int]) -> int:
    '''get the number of total complaints for 2022'''
    return sum([value for value in companies.values()])

def get_total_complaints_top_3_companies_2022(companies: dict[str:int]) -> int:
    '''
        get the number of complaints for top 3 companies in 2022
        top 3 will definitely be the credit score providers
        three of them have more than 50% of complaints 
    '''
    return pd.Series(companies).nlargest(3).sum()

total_complaints_2022 = get_total_complaints_2022(c_2022)
top_3_total_complaints_2022 = get_total_complaints_top_3_companies_2022(c_2022)