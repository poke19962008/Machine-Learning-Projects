import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

def ageSurvivalFreq():
    ageGroupS = df.groupby(['Survived']).get_group(1)
    ageGroupS = ageGroupS.groupby(['Age'])['Age'].aggregate(len)
    ageGroupS = pd.DataFrame({'Age': ageGroupS.index, 'Frequency': ageGroupS.values})

    ageGroupD = df.groupby(['Survived']).get_group(0)
    ageGroupD = ageGroupD.groupby(['Age'])['Age'].aggregate(len)
    ageGroupD = pd.DataFrame({'Age': ageGroupD.index, 'Frequency': ageGroupD.values})

    ageGroup = pd.merge(ageGroupD, ageGroupS, how='inner', on='Age', suffixes=('Dead', 'Survived'))
    ageGroup[['FrequencyDead', 'FrequencySurvived']].plot.bar( title='Age And Survival Frequency', stacked=True, xticks=ageGroup['Age'])

if __name__ == '__main__':
    ageSurvivalFreq()

    plt.show()
