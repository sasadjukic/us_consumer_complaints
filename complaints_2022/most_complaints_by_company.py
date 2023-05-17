
import pandas as pd
from main_2022 import c_2022
from ccr_agencies import ccra

def get_complaints_2022_sans_ccra(companies: dict[str:int], ccra: list[str]) -> dict[str:int]:
    ''' 
        remove credit score providers from the list of companies
        this is to focus on others who are overshadowed by large 3 credit score providers
    '''
    for name in ccra:
        companies.pop(name)

    return companies

def find_top_5_companies_most_complaints_sans_ccra(companies: dict[str:int]) -> pd.Series:
    '''find top 5 companies that recorded most complaints (not including ccra provider)'''
    return pd.Series(companies).nlargest(5)

sans_credit_providers = get_complaints_2022_sans_ccra(c_2022, ccra)
top_5_sans_ccra = find_top_5_companies_most_complaints_sans_ccra(sans_credit_providers)