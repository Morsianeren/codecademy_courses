#%% Imports
import seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv('./tennis_stats.csv')

#print(df.head())

#player_group = df.groupby('Player')['TotalPointsWon']

# The following line explores how many times each player appears
print(df['Player'].value_counts())
# As we can see here, players appear between 1 and 9 times

# Lets try and figure out why:
print(df[df['Player'] == 'Ivan Dodig']) # Ivan appears 9 times

# It seems that the players are appearing multiple 
# times because of different years!

# perform exploratory analysis here:

# We have 4 different outcomes:
# Wins: number of matches won in a year
# Losses: number of matches lost in a year
# Winnings: total winnings in USD($) in a year
# Ranking: ranking at the end of year

# Lets just focus on the Winnings
# We can start by plotting the winnings compared to appearences
# So the y-axis is total winnings and x-axis is number of appearances (1 to 9)

# Plotting total winnings compared to appearances (GitHub Copilot was used here)
plt.scatter(df['Player'].value_counts(), df.groupby('Player')['Winnings'].sum())
plt.xlabel('Number of Appearances')
plt.ylabel('Total Winnings')
plt.title('Total Winnings vs Appearances')
plt.show()

















## perform single feature linear regressions here:






















## perform two feature linear regressions here:






















## perform multiple feature linear regressions here:
# %%
