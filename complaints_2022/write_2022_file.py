
# import necessary libraries
import sys, os 
from usa_states import states

# locate the main package and add it to the list of available paths for imports
userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\\us_complaints_temp\main_data'
sys.path.append(file_path)

# import main complaints module
from main import usa_complaints

# get only complaints from 2022 
complaints_2022 = usa_complaints[usa_complaints['date_received'].str.contains('2022')]

# keep only 50 US states and DC in the sheet
usa = complaints_2022[complaints_2022['state'].isin(states)]

# write a smaller csv file only for 2022
usa.to_csv('us_consumer_complaints_2022.csv')