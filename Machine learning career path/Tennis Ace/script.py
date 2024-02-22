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
# Later note: Ranking is actually an outcome and not a feature, so this plot is not useful

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
lr = LinearRegression()

# Get X and y values
X_label = 'Aces'
X = df[[X_label]]
y = df['Winnings']

# Split into test and training data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=6)

# Fit data
lr.fit(x_train, y_train)

# Predict
y_predict = lr.predict(x_test)

# Plot the results
plt.figure()
plt.scatter(x_test, y_test, label='Actual')
plt.plot(x_test, y_predict, label='Predicted', color='red')
plt.xlabel(X_label)
plt.ylabel('Winnings [USD]')
plt.legend()
plt.title(X_label + ' vs Winnings')
plt.show()

# %% perform two feature linear regressions here:

# First we need to extract the features we want to use
X = df[['BreakPointsOpportunities', 'Aces']] # Alternatively we could use FirstServeReturnPointsWon

# Split into test and training data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=6)

# Fit data
lr.fit(x_train, y_train)

# Predict
y_predict = lr.predict(x_test)

# Plot the results
# We can't plot this as a 2D plot, so we will plot the residuals
plt.figure()
plt.scatter(y_test, y_predict - y_test)
plt.xlabel('Actual Winnings [USD]')
plt.ylabel('Residuals')
plt.title('Residuals of 2 feature linear regression')
plt.show()

# We can also plot the y_predict vs y_test
plt.figure()
plt.scatter(y_test, y_predict)
plt.xlabel('Actual Winnings [USD]')
plt.ylabel('Predicted Winnings [USD]')
plt.title('Predicted vs Actual Winnings')
# Limit the x and y axis to be the same
plt.xlim(0, 1000000)
plt.ylim(0, 1000000)
plt.show()

# Lets calculate the R^2 score
print('R^2 score for test:', lr.score(x_test, y_test))
print('R^2 score for train:', lr.score(x_train, y_train))

# The R^2 score is 0.82, which is quite good! (>0.7 is good)
# That means that 82% of the variance in the winnings can be explained by the model

# %% perform multiple feature linear regressions here:

# This can be done by adding more features to the X matrix
# I am going to skip this part, as it is quite similar to the previous part
