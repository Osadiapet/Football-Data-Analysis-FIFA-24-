<<<<<<< HEAD
#!/usr/bin/env python
# coding: utf-8

# <a id='intro'></a>
# 
# # Project Title: Unlocking the Game: A Football Data Analytics Odyssey
# 
# ## Introduction
# 
# The world of football is not just about goals and cheers; it's a realm where data and insights can elevate the game. Our project takes you on a journey through a treasure trove of football data, encompassing more than 25,000 matches, 10,000 players, and 11 European countries' top championships, spanning from the 2008/2009 season to 2015/2016. Sourced from EA Sports' FIFA video game serie.
# 
# This football data analytics project is poised to be a deep dive into the world of European professional football. It aims to uncover patterns, strategies, and extraordinary talents that make this sport the global phenomenon it is. From teams' remarkable turnarounds to the secrets behind star players and the intricate relationships among player attributes, we will leave no stone unturned.
# 
# Our mission is to present this project in a captivating and well-drafted manner, designed to win the hearts of football enthusiasts and data aficionados alike. With a blend of statistics, data visualization, and in-depth analysis, we will bring the passion and strategy of football to life in a new and exciting way.
# 

# In[ ]:





# In[1]:


#importing packages 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import datetime as dt

#for statistical analysis 
import scipy
from scipy.stats import chisquare
from bioinfokit.analys import stat
get_ipython().run_line_magic('matplotlib', 'inline')

pd.set_option('display.max_colwidth', None) #to display all columns in the dataframe
pd.set_option('display.max_columns', None )

import warnings
warnings.filterwarnings('ignore')


# 

# <a id='wrangling'></a>
# ## Data Wrangling

# In[2]:


players_data=pd.read_csv('C:/Users/osadi/OneDrive/Desktop/Projects\Europe-Football-Data-Analysis-/male_players.csv')
players_data.head()


# In[3]:


players_data.info()


# In[4]:


#descriptive statistics of players attributes 
players_data.describe()


# In[5]:


numerical_columns = players_data.select_dtypes(include=['number'])


# In[6]:


numerical_columns.columns


# In[29]:


# Select the variables you want to plot
players_variables_to_plot = ['overall', 'potential', 
       'skill_moves', 'pace', 'shooting',
       'passing', 'dribbling', 'defending', 'physic', 'attacking_crossing',
       'attacking_finishing', 'attacking_heading_accuracy',
       'attacking_short_passing', 'attacking_volleys', 'skill_dribbling',
       'skill_curve', 'skill_fk_accuracy', 'skill_long_passing',
       'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed',
       'movement_agility', 'movement_reactions', 'movement_balance',
       'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength',
       'power_long_shots', 'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
       'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
       'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']

# Calculate the number of rows and columns needed for subplots
n_variables = len(players_variables_to_plot)
n_rows = (n_variables - 1) // 4 + 1
n_columns = min(n_variables, 4)

# Create subplots for the variables
plt.figure(figsize=(18, 4 * n_rows))

# Loop through the selected variables and create density plots
for i, variable in enumerate(players_variables_to_plot, 1):
    plt.subplot(n_rows, n_columns, i)
    sns.kdeplot(players_data[variable], shade=True, color='b')
    plt.title(f'Distribution of {variable}')
    plt.xlabel(variable)

plt.tight_layout()
plt.show()  # Display the plot


# In[30]:


players_num = players_data[players_variables_to_plot]
#let's see how these attributes relate with each other with heatmap
plt.figure(figsize=(30,24))
sns.heatmap(players_num.corr(), cmap='coolwarm', annot=True, fmt='.2f').\
set_title('Heatmap Showing Relationship Between Player Attributes');


# In[9]:


# Group by player_name and calculate the average overall rating
top_10_players = players_data.groupby('long_name')[['overall']].mean().sort_values(by='overall', ascending=False).head(10)

# Plot the data
plt.figure(figsize=(12, 6))
bars = plt.barh(top_10_players.index, top_10_players['overall'], color='skyblue')
plt.xlabel('Average Overall Rating')
plt.title('Top 10 Players by Average Overall Rating Over Time')
plt.gca().invert_yaxis()  # Invert the y-axis for better visualization

# Add data labels to the bars
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f'{width:.2f}', ha='left', va='center', color='black')

plt.show()


# In[23]:


# players_data[players_data['long_name']=='Cristiano Ronaldo dos Santos Aveiro']


# In[24]:


# Define attribute groups
goalkeeper_attrs = ['goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
                   'goalkeeping_positioning', 'goalkeeping_reflexes']
defender_attrs = ['defending_marking_awareness', 'defending_standing_tackle', 'defending_sliding_tackle']
midfielder_attrs = ['passing', 'dribbling', 'movement_acceleration', 'movement_sprint_speed',
                  'movement_agility', 'movement_reactions', 'movement_balance', 'mentality_vision', 'skill_dribbling',
                  'mentality_penalties', 'mentality_composure', 'mentality_interceptions', 'physic',
                 'mentality_positioning']
attacker_attrs = ['shooting', 'attacking_crossing', 'attacking_finishing', 
                 'attacking_heading_accuracy', 'attacking_short_passing', 'attacking_volleys', 
                 'skill_dribbling', 'skill_curve', 'skill_fk_accuracy', 'skill_long_passing', 
                 'skill_ball_control', 'power_shot_power', 'power_jumping', 'power_stamina', 'physic',
                 'power_strength', 'power_long_shots', 'mentality_aggression']


# Calculate the mean for each group
players_data['Goalkeepers'] = players_data[goalkeeper_attrs].mean(axis=1)
players_data['Defenders'] = players_data[defender_attrs].mean(axis=1)
players_data['Midfielders'] = players_data[midfielder_attrs].mean(axis=1)
players_data['Attackers'] = players_data[attacker_attrs].mean(axis=1)


# In[25]:


# Sort by the top 10 players for each group
top_10_defenders = players_data.sort_values(by='Defenders', ascending=False).head(10)
top_10_goalkeepers = players_data.sort_values(by='Goalkeepers', ascending=False).head(10)
top_10_midfielders = players_data.sort_values(by='Midfielders', ascending=False).head(10)
top_10_attackers = players_data.sort_values(by='Attackers', ascending=False).head(10)


# In[34]:


# Create subplots for each group
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Top 10 Players by Mean Attributes for Each Category", fontsize=16)

# Plot and label the top 10 players for each group
for ax, top_players, group_name in zip(axes.flatten(), [top_10_defenders, top_10_goalkeepers, top_10_midfielders, top_10_attackers], 
                                      ['Defenders', 'Goalkeepers', 'Midfielders', 'Attackers']):
    bars = ax.barh(top_players['short_name'], top_players[group_name], color='skyblue')
    ax.set_xlabel(f'Mean {group_name} Attributes')
    ax.set_title(f'Top 10 {group_name}', fontsize=12)
    ax.invert_yaxis()
    
    # Add data labels
    for bar in bars:
        width = bar.get_width()
        label_x_pos = width if width >= 0 else width - 1
        ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', )

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()


# In[15]:


# Create subplots for each group
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Top 10 Leagues by Mean Attributes for Each Category", fontsize=16)

# Plot and label the top 10 players for each group
for ax, top_players, group_name in zip(axes.flatten(), [top_10_defenders, top_10_goalkeepers, top_10_midfielders, top_10_attackers], 
                                      ['Defenders', 'Goalkeepers', 'Midfielders', 'Attackers']):
    bars = ax.barh(top_players['club_name'], top_players[group_name], color='skyblue')
    ax.set_xlabel(f'Mean {group_name} Attributes')
    ax.set_title(f'Top 10 {group_name}', fontsize=12)
    ax.invert_yaxis()
    
    # Add data labels
    for bar in bars:
        width = bar.get_width()
        label_x_pos = width if width >= 0 else width - 1
        ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='center', va='center')

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()


# In[ ]:





# ### Analyzing Football Player Attributes Using Factor Analysis (FA)
# 
# Factor analysis is a powerful statistical technique used to explore the underlying structure and relationships among a set of observed variables. FA analysis can provide valuable insights into the latent factors that may influence a player's performance. 
# 
# Description:
# 
# Football is a game of skill, precision, and teamwork. To gain a deeper understanding of what makes a player truly exceptional, we would look into the  player attributes. From their dribbling finesse to their goalkeeping prowess, footballers possess a wide range of skills and abilities.
# 
# Factor Analysis is our key to unlocking the hidden patterns within these attributes. Our goal is to simplify the complexity of player attributes and discover the latent factors that drive performance on the field. By identifying these underlying factors, we aim to gain insights into the essential skills and characteristics that contribute to a player's success.
# 
# We will analyze attributes such as crossing, finishing, sprint speed, and goalkeeping reflexes. Through Factor Analysis, we'll uncover whether these attributes can be grouped into common factors, providing a more comprehensive perspective on player capabilities. Are there inherent skills that define an exceptional forward, midfielder, or defender? Our analysis seeks to answer these questions and offer a fresh perspective on the intricate world of football player attributes.
# 
# By revealing the underlying factors, we aim to help football enthusiasts, coaches, and analysts better understand what truly matters on the pitch. Factor Analysis can provide a structured approach to evaluating players, informing recruitment strategies, and enhancing overall team performance.

# In[17]:


fa_attributes = players_data[['skill_moves', 'pace', 'shooting',
       'passing', 'dribbling', 'defending', 'physic', 'attacking_crossing',
       'attacking_finishing', 'attacking_heading_accuracy',
       'attacking_short_passing', 'attacking_volleys', 'skill_dribbling',
       'skill_curve', 'skill_fk_accuracy', 'skill_long_passing',
       'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed',
       'movement_agility', 'movement_reactions', 'movement_balance',
       'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength',
       'power_long_shots', 'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
       'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
       'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']]


# In[18]:


from sklearn.preprocessing import StandardScaler

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the data
scaled_fa_attributes = scaler.fit_transform(fa_attributes)

# Create a new DataFrame with the scaled data
scaled_fa_attributes_df = pd.DataFrame(scaled_fa_attributes, columns=fa_attributes.columns)

# Display the first few rows of the scaled data
scaled_fa_attributes_df.head()


# In[19]:


# Instantiate factor analysis object
from factor_analyzer.factor_analyzer import FactorAnalyzer 
fa = FactorAnalyzer(rotation='varimax')
fa.fit(scaled_fa_attributes_df)
# Check Eigenvalues
ev, v = fa.get_eigenvalues()
ev


# We are employing the Kaiser Criterion for selecting the number of factors in our factor analysis. According to this criterion, we will retain factors for which the eigenvalues are greater than 1. Eigenvalues measure the variance explained by each factor, and an eigenvalue exceeding 1 signifies that the factor accounts for more variance than an individual observed variable. By adopting this criterion, we aim to identify and keep factors that capture a substantial amount of information in our data, aiding our analysis in deriving meaningful insights.

# In[ ]:





# In[20]:


# Select the player attributes
attributes = players_num # Include all your attributes

# Ensure the data is suitable for FA (e.g., no missing values)

# Perform Factor Analysis
fa = FactorAnalyzer(rotation='varimax', n_factors=6)  # Adjust the number of factors as needed
fa.fit(scaled_fa_attributes_df)

# Get factor loadings
factor_loadings = fa.loadings_

# Create a DataFrame to display factor loadings
factor_loadings_df = pd.DataFrame(factor_loadings, index=scaled_fa_attributes_df.columns, columns=['Factor 1', 'Factor 2', 'Factor 3', 'Factor 4', 'Factor 5', 'Factor 6'])
factor_loadings_df


# **Factor 1 - `Technical Prowess`:**
# 
# `Attributes:` skill_moves, shooting, passing, dribbling, attacking_crossing, attacking_finishing, attacking_heading_accuracy, attacking_short_passing, attacking_volleys, skill_dribbling, skill_curve, skill_fk_accuracy, skill_long_passing, skill_ball_control
# 
# `Description:` Factor 1 represents a player's technical skills and proficiency in areas like dribbling, passing, and shooting.
# 
# **Factor 2: `Mental Attributes`**
# 
# `Attributes:` mentality_aggression, mentality_interceptions, mentality_positioning, mentality_vision, mentality_penalties, mentality_composure
# `Description:` Factor 4 represents a player's mental attributes, including aggression, positioning, and composure, which affect decision-making on the field.
# 
# **Factor 3 - `Defensive Abilities`:**
# 
# `Attributes:` defending, defending_marking_awareness, defending_standing_tackle, defending_sliding_tackle, power_jumping, power_stamina, power_strength
# `Description:` Factor 3 is associated with a player's defensive capabilities and physical attributes that contribute to defensive strength.
# 
# **Factor 4: `Dynamic Movement Proficiency`**
# 
# `Attributes:` movement_acceleration, movement_sprint_speed, movement_agility, movement_reactions, andmovement_balance
# 
# `Description:` This captures the player's attributes related to their ability to move dynamically on the field. It reflects how well a player can perform agility, acceleration, sprint speed, balance, and how quickly they can react to changes in the game. This factor emphasizes a player's physical attributes for agility and quick reaction times, making them effective at changing direction rapidly and responding to the dynamic nature of football.
# 
# Attributes: physic
# Description: Factors 5 and 6 doesn't have a clear thematic grouping based on the attributes. It may be related to physical attributes but isn't easily categorized with a specific label.
# 
# 
# 
# 
# 
# 

# In[ ]:




=======
#!/usr/bin/env python
# coding: utf-8

# <a id='intro'></a>
# 
# # Project Title: Unlocking the Game: A Football Data Analytics Odyssey
# 
# ## Introduction
# 
# The world of football is not just about goals and cheers; it's a realm where data and insights can elevate the game. Our project takes you on a journey through a treasure trove of football data, encompassing more than 25,000 matches, 10,000 players, and 11 European countries' top championships, spanning from the 2008/2009 season to 2015/2016. Sourced from EA Sports' FIFA video game serie.
# 
# This football data analytics project is poised to be a deep dive into the world of European professional football. It aims to uncover patterns, strategies, and extraordinary talents that make this sport the global phenomenon it is. From teams' remarkable turnarounds to the secrets behind star players and the intricate relationships among player attributes, we will leave no stone unturned.
# 
# Our mission is to present this project in a captivating and well-drafted manner, designed to win the hearts of football enthusiasts and data aficionados alike. With a blend of statistics, data visualization, and in-depth analysis, we will bring the passion and strategy of football to life in a new and exciting way.
# 

# In[ ]:





# In[1]:


#importing packages 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import datetime as dt

#for statistical analysis 
import scipy
from scipy.stats import chisquare
from bioinfokit.analys import stat
get_ipython().run_line_magic('matplotlib', 'inline')

pd.set_option('display.max_colwidth', None) #to display all columns in the dataframe
pd.set_option('display.max_columns', None )

import warnings
warnings.filterwarnings('ignore')


# 

# <a id='wrangling'></a>
# ## Data Wrangling

# In[2]:


players_data=pd.read_csv('C:/Users/osadi/OneDrive/Desktop/Projects\Europe-Football-Data-Analysis-/male_players.csv')
players_data.head()


# In[3]:


players_data.info()


# In[4]:


#descriptive statistics of players attributes 
players_data.describe()


# In[5]:


numerical_columns = players_data.select_dtypes(include=['number'])


# In[6]:


numerical_columns.columns


# In[29]:


# Select the variables you want to plot
players_variables_to_plot = ['overall', 'potential', 
       'skill_moves', 'pace', 'shooting',
       'passing', 'dribbling', 'defending', 'physic', 'attacking_crossing',
       'attacking_finishing', 'attacking_heading_accuracy',
       'attacking_short_passing', 'attacking_volleys', 'skill_dribbling',
       'skill_curve', 'skill_fk_accuracy', 'skill_long_passing',
       'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed',
       'movement_agility', 'movement_reactions', 'movement_balance',
       'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength',
       'power_long_shots', 'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
       'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
       'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']

# Calculate the number of rows and columns needed for subplots
n_variables = len(players_variables_to_plot)
n_rows = (n_variables - 1) // 4 + 1
n_columns = min(n_variables, 4)

# Create subplots for the variables
plt.figure(figsize=(18, 4 * n_rows))

# Loop through the selected variables and create density plots
for i, variable in enumerate(players_variables_to_plot, 1):
    plt.subplot(n_rows, n_columns, i)
    sns.kdeplot(players_data[variable], shade=True, color='b')
    plt.title(f'Distribution of {variable}')
    plt.xlabel(variable)

plt.tight_layout()
plt.show()  # Display the plot


# In[30]:


players_num = players_data[players_variables_to_plot]
#let's see how these attributes relate with each other with heatmap
plt.figure(figsize=(30,24))
sns.heatmap(players_num.corr(), cmap='coolwarm', annot=True, fmt='.2f').\
set_title('Heatmap Showing Relationship Between Player Attributes');


# In[9]:


# Group by player_name and calculate the average overall rating
top_10_players = players_data.groupby('long_name')[['overall']].mean().sort_values(by='overall', ascending=False).head(10)

# Plot the data
plt.figure(figsize=(12, 6))
bars = plt.barh(top_10_players.index, top_10_players['overall'], color='skyblue')
plt.xlabel('Average Overall Rating')
plt.title('Top 10 Players by Average Overall Rating Over Time')
plt.gca().invert_yaxis()  # Invert the y-axis for better visualization

# Add data labels to the bars
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f'{width:.2f}', ha='left', va='center', color='black')

plt.show()


# In[23]:


# players_data[players_data['long_name']=='Cristiano Ronaldo dos Santos Aveiro']


# In[24]:


# Define attribute groups
goalkeeper_attrs = ['goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
                   'goalkeeping_positioning', 'goalkeeping_reflexes']
defender_attrs = ['defending_marking_awareness', 'defending_standing_tackle', 'defending_sliding_tackle']
midfielder_attrs = ['passing', 'dribbling', 'movement_acceleration', 'movement_sprint_speed',
                  'movement_agility', 'movement_reactions', 'movement_balance', 'mentality_vision', 'skill_dribbling',
                  'mentality_penalties', 'mentality_composure', 'mentality_interceptions', 'physic',
                 'mentality_positioning']
attacker_attrs = ['shooting', 'attacking_crossing', 'attacking_finishing', 
                 'attacking_heading_accuracy', 'attacking_short_passing', 'attacking_volleys', 
                 'skill_dribbling', 'skill_curve', 'skill_fk_accuracy', 'skill_long_passing', 
                 'skill_ball_control', 'power_shot_power', 'power_jumping', 'power_stamina', 'physic',
                 'power_strength', 'power_long_shots', 'mentality_aggression']


# Calculate the mean for each group
players_data['Goalkeepers'] = players_data[goalkeeper_attrs].mean(axis=1)
players_data['Defenders'] = players_data[defender_attrs].mean(axis=1)
players_data['Midfielders'] = players_data[midfielder_attrs].mean(axis=1)
players_data['Attackers'] = players_data[attacker_attrs].mean(axis=1)


# In[25]:


# Sort by the top 10 players for each group
top_10_defenders = players_data.sort_values(by='Defenders', ascending=False).head(10)
top_10_goalkeepers = players_data.sort_values(by='Goalkeepers', ascending=False).head(10)
top_10_midfielders = players_data.sort_values(by='Midfielders', ascending=False).head(10)
top_10_attackers = players_data.sort_values(by='Attackers', ascending=False).head(10)


# In[34]:


# Create subplots for each group
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Top 10 Players by Mean Attributes for Each Category", fontsize=16)

# Plot and label the top 10 players for each group
for ax, top_players, group_name in zip(axes.flatten(), [top_10_defenders, top_10_goalkeepers, top_10_midfielders, top_10_attackers], 
                                      ['Defenders', 'Goalkeepers', 'Midfielders', 'Attackers']):
    bars = ax.barh(top_players['short_name'], top_players[group_name], color='skyblue')
    ax.set_xlabel(f'Mean {group_name} Attributes')
    ax.set_title(f'Top 10 {group_name}', fontsize=12)
    ax.invert_yaxis()
    
    # Add data labels
    for bar in bars:
        width = bar.get_width()
        label_x_pos = width if width >= 0 else width - 1
        ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', )

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()


# In[15]:


# Create subplots for each group
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Top 10 Leagues by Mean Attributes for Each Category", fontsize=16)

# Plot and label the top 10 players for each group
for ax, top_players, group_name in zip(axes.flatten(), [top_10_defenders, top_10_goalkeepers, top_10_midfielders, top_10_attackers], 
                                      ['Defenders', 'Goalkeepers', 'Midfielders', 'Attackers']):
    bars = ax.barh(top_players['club_name'], top_players[group_name], color='skyblue')
    ax.set_xlabel(f'Mean {group_name} Attributes')
    ax.set_title(f'Top 10 {group_name}', fontsize=12)
    ax.invert_yaxis()
    
    # Add data labels
    for bar in bars:
        width = bar.get_width()
        label_x_pos = width if width >= 0 else width - 1
        ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='center', va='center')

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()


# In[ ]:





# ### Analyzing Football Player Attributes Using Factor Analysis (FA)
# 
# Factor analysis is a powerful statistical technique used to explore the underlying structure and relationships among a set of observed variables. FA analysis can provide valuable insights into the latent factors that may influence a player's performance. 
# 
# Description:
# 
# Football is a game of skill, precision, and teamwork. To gain a deeper understanding of what makes a player truly exceptional, we would look into the  player attributes. From their dribbling finesse to their goalkeeping prowess, footballers possess a wide range of skills and abilities.
# 
# Factor Analysis is our key to unlocking the hidden patterns within these attributes. Our goal is to simplify the complexity of player attributes and discover the latent factors that drive performance on the field. By identifying these underlying factors, we aim to gain insights into the essential skills and characteristics that contribute to a player's success.
# 
# We will analyze attributes such as crossing, finishing, sprint speed, and goalkeeping reflexes. Through Factor Analysis, we'll uncover whether these attributes can be grouped into common factors, providing a more comprehensive perspective on player capabilities. Are there inherent skills that define an exceptional forward, midfielder, or defender? Our analysis seeks to answer these questions and offer a fresh perspective on the intricate world of football player attributes.
# 
# By revealing the underlying factors, we aim to help football enthusiasts, coaches, and analysts better understand what truly matters on the pitch. Factor Analysis can provide a structured approach to evaluating players, informing recruitment strategies, and enhancing overall team performance.

# In[17]:


fa_attributes = players_data[['skill_moves', 'pace', 'shooting',
       'passing', 'dribbling', 'defending', 'physic', 'attacking_crossing',
       'attacking_finishing', 'attacking_heading_accuracy',
       'attacking_short_passing', 'attacking_volleys', 'skill_dribbling',
       'skill_curve', 'skill_fk_accuracy', 'skill_long_passing',
       'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed',
       'movement_agility', 'movement_reactions', 'movement_balance',
       'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength',
       'power_long_shots', 'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
       'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
       'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']]


# In[18]:


from sklearn.preprocessing import StandardScaler

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the data
scaled_fa_attributes = scaler.fit_transform(fa_attributes)

# Create a new DataFrame with the scaled data
scaled_fa_attributes_df = pd.DataFrame(scaled_fa_attributes, columns=fa_attributes.columns)

# Display the first few rows of the scaled data
scaled_fa_attributes_df.head()


# In[19]:


# Instantiate factor analysis object
from factor_analyzer.factor_analyzer import FactorAnalyzer 
fa = FactorAnalyzer(rotation='varimax')
fa.fit(scaled_fa_attributes_df)
# Check Eigenvalues
ev, v = fa.get_eigenvalues()
ev


# We are employing the Kaiser Criterion for selecting the number of factors in our factor analysis. According to this criterion, we will retain factors for which the eigenvalues are greater than 1. Eigenvalues measure the variance explained by each factor, and an eigenvalue exceeding 1 signifies that the factor accounts for more variance than an individual observed variable. By adopting this criterion, we aim to identify and keep factors that capture a substantial amount of information in our data, aiding our analysis in deriving meaningful insights.

# In[ ]:





# In[20]:


# Select the player attributes
attributes = players_num # Include all your attributes

# Ensure the data is suitable for FA (e.g., no missing values)

# Perform Factor Analysis
fa = FactorAnalyzer(rotation='varimax', n_factors=6)  # Adjust the number of factors as needed
fa.fit(scaled_fa_attributes_df)

# Get factor loadings
factor_loadings = fa.loadings_

# Create a DataFrame to display factor loadings
factor_loadings_df = pd.DataFrame(factor_loadings, index=scaled_fa_attributes_df.columns, columns=['Factor 1', 'Factor 2', 'Factor 3', 'Factor 4', 'Factor 5', 'Factor 6'])
factor_loadings_df


# **Factor 1 - `Technical Prowess`:**
# 
# `Attributes:` skill_moves, shooting, passing, dribbling, attacking_crossing, attacking_finishing, attacking_heading_accuracy, attacking_short_passing, attacking_volleys, skill_dribbling, skill_curve, skill_fk_accuracy, skill_long_passing, skill_ball_control
# 
# `Description:` Factor 1 represents a player's technical skills and proficiency in areas like dribbling, passing, and shooting.
# 
# **Factor 2: `Mental Attributes`**
# 
# `Attributes:` mentality_aggression, mentality_interceptions, mentality_positioning, mentality_vision, mentality_penalties, mentality_composure
# `Description:` Factor 4 represents a player's mental attributes, including aggression, positioning, and composure, which affect decision-making on the field.
# 
# **Factor 3 - `Defensive Abilities`:**
# 
# `Attributes:` defending, defending_marking_awareness, defending_standing_tackle, defending_sliding_tackle, power_jumping, power_stamina, power_strength
# `Description:` Factor 3 is associated with a player's defensive capabilities and physical attributes that contribute to defensive strength.
# 
# **Factor 4: `Dynamic Movement Proficiency`**
# 
# `Attributes:` movement_acceleration, movement_sprint_speed, movement_agility, movement_reactions, andmovement_balance
# 
# `Description:` This captures the player's attributes related to their ability to move dynamically on the field. It reflects how well a player can perform agility, acceleration, sprint speed, balance, and how quickly they can react to changes in the game. This factor emphasizes a player's physical attributes for agility and quick reaction times, making them effective at changing direction rapidly and responding to the dynamic nature of football.
# 
# Attributes: physic
# Description: Factors 5 and 6 doesn't have a clear thematic grouping based on the attributes. It may be related to physical attributes but isn't easily categorized with a specific label.
# 
# 
# 
# 
# 
# 

# In[ ]:




>>>>>>> 7693083983d44a0160997b731185dbc6e6e38269
