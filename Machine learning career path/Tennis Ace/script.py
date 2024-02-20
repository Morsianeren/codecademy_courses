#%% Imports
import seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# %% load and investigate the data here:
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

# %% perform exploratory analysis here:

# We have 4 different outcomes:
# Wins: number of matches won in a year
# Losses: number of matches lost in a year
# Winnings: total winnings in USD($) in a year
# Ranking: ranking at the end of year

# Lets just focus on the Winnings
# We can start by plotting the winnings compared to appearences
# So the y-axis is total winnings and x-axis is number of appearances (1 to 9)

# Plotting total winnings compared to appearances (GitHub Copilot was used here)
plt.figure()
plt.scatter(df['Player'].value_counts(), df.groupby('Player')['Winnings'].sum())
plt.xlabel('Number of Appearances')
plt.ylabel('Total Winnings [USD]')
plt.title('Total Winnings vs Appearances')
plt.show()

# Here seems to be no correlation, weirdly enough!
# I think this is cause an misleading representation.

# Lets try and plot the winnings compared to the ranking
plt.figure()
plt.scatter(df['Ranking'], df['Winnings'])
plt.xlabel('Ranking')
plt.ylabel('Winnings [USD]')
plt.title('Yearly Winnings vs Ranking')
plt.show()

# Here we can see a correlation!
# The higher the ranking (1 is highest), the higher the winnings

# Lets try and compare winnings to the year
plt.figure()
plt.scatter(df['Year'], df['Winnings'])
plt.xlabel('Year')
plt.ylabel('Winnings [USD]')
plt.title('Yearly Winnings')
plt.show()
# Its a bit hard to get anything useful from this plot
# Lets try and make it more visually clear

total_yearly_winnings = df['Winnings'].groupby(df['Year']).sum()
#years = df['Year'].groupby(df['Year'])

# Make a boxplot for each year
years = df['Year'].unique()

plt.figure()
for year in years:
    plt.boxplot(df['Winnings'].groupby(df['Year']).get_group(year), positions=[year])

# This actually turned out to be a great plot!
# We see that the average stays the same, however 
# we get more outliers (big prize money) as the year increases  


# %% perform single feature linear regressions here:

# Initialize the regressor
regressor = LinearRegression()

# Get X and y values
X = df[['Ranking']]
y = df['Winnings']

# Split into test and training data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=6)





















# %% perform two feature linear regressions here:






















# %% perform multiple feature linear regressions here:
# %%
