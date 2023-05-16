
# This is only to set up the US map
# companies logos will be added with PS

import plotly.express as px 

def display_most_complaints_per_state() -> None:
    '''display USA map with state borders''' 
    fig = px.choropleth(
                        locationmode='USA-states',
                        scope='usa',
                       )

    fig.show()

display_most_complaints_per_state()

