
import re
import pandas as pd
from pathlib import Path 

# find the directory containing the main complaints file
directory = (
    Path.home()
    /'Desktop'
    /'data'
    /'complaints.csv'
)

# locate the file
file = directory / 'complaints.csv'

# read the main complaints file
complaints = pd.read_csv(file)

def fix_columns(data: pd.DataFrame) -> pd.DataFrame:
    ''' 
        uniform the appearance of columns in the following way:
        - make all words lower cases
        - remove question marks
        - remove empty spaces between words
        - remove - beteween words
        - connect the words with _
    '''
    data.columns = ['_'.join(re.split('-| ', x.lower().replace('?', ''))) for x in data.columns]
    return data 

usa_complaints = fix_columns(complaints)
