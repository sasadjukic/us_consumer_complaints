
import pandas as pd 
from main_2022 import complaints_2022 
from ccr_agencies import ccra

def get_complaints_not_ccra_2022(data: pd.DataFrame, ccra: list[str]) -> dict[str:int]:
    '''
        get complaints for companies that are not 3 major credit score providers
    '''
    complains_type = {}
    for n in data.index:
        complaint = data.loc[n, 'issue']
        company = data.loc[n, 'company']
        if company not in ccra:
            if complaint not in complains_type:
                complains_type[complaint] = 1
            else:
                complains_type[complaint] +=1

    return complains_type 
        
def find_most_common_complaints_not_ccra_2022(complaints: dict[str:int]) -> pd.Series:
    '''find most common complaints for companies in 2022, sans credit score providers'''
    return pd.Series(complaints).nlargest(5)

complaints_sans_csp = get_complaints_not_ccra_2022(complaints_2022, ccra)
most_common_complaints_sans_csp = find_most_common_complaints_not_ccra_2022(complaints_sans_csp)