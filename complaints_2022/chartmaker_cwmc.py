
import pandas as pd
import matplotlib.pyplot as plt 
from most_complaints_by_company import top_5_sans_ccra

def display_most_common_complaints(top_5: pd.Series) -> None:
    '''create a base for our horizontal chart'''

    # create necessary variables
    companies = top_5.index.tolist()
    complaints = top_5.values.tolist()
    companies.reverse()
    complaints.reverse()
    color = '#387668'

    fig, ax = plt.subplots()

    ax.barh(
        companies,
        complaints,
        color = color
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    for index, value in enumerate(complaints):
        plt.text(
            value, 
            index, 
            str(value),
            position = (value+100, index)
        )

    plt.show()


print(display_most_common_complaints(top_5_sans_ccra))