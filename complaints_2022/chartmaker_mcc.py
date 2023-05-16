
import pandas as pd
import matplotlib.pyplot as plt 
from most_common_complaints import most_common_complaints_sans_csp

def display_most_common_complaints(comp: pd.Series) -> None:


    complaints = comp.index.tolist()
    vals = comp.values.tolist()
    color = '#d1a730'

    fig, ax = plt.subplots()

    ax.barh(
        complaints,
        vals,
        color = color
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    for index, value in enumerate(vals):
        plt.text(
            value, 
            index, 
            str(value),
            position = (value+100, index)
        )

    plt.show()


display_most_common_complaints(most_common_complaints_sans_csp)