
import matplotlib.pyplot as plt 
from credit_score_providers_share_of_complaints import total_complaints_2022, top_3_total_complaints_2022

def display_share_of_ccra(tc_2022: int, t3_2022: int) -> None:
    '''create a base for our pie chart'''

    # create necessary variables
    CCRA = round((t3_2022/tc_2022)*100, 2)
    REST = 100 - CCRA 
    labels = ['CREDIT SCORE PROVIDERS', 'REST']
    colors = ['#387668', '#d1a730']

    #  create a pie chart
    patches, texts, autotexts = plt.pie(
        [CCRA, REST],
        labels = labels,
        colors = colors,
        autopct = '%.2f %%',
        startangle = 55,
        pctdistance = 0.85
    )

    # sahow chart
    plt.show()


display_share_of_ccra(total_complaints_2022, top_3_total_complaints_2022)
