import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import plotly.express as px

matplotlib.use('Agg')  # Use the 'Agg' backend for saving figures
import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Configure Streamlit
st.set_page_config(page_title="FIFA'24 Player Analysis", page_icon="⚽", layout="wide")

# Load the data
players_data = pd.read_csv('male_players.csv')

# Remove unnecessary columns
selected_columns = [
    'long_name', 'update_as_of', 'value_eur', 'wage_eur', 'age', 'dob', 'height_cm',
    'weight_kg', 'overall', 'potential', 'skill_moves', 'pace', 'shooting',
    'passing', 'dribbling', 'defending', 'physic', 'attacking_crossing', 'player_url',
    'attacking_finishing', 'attacking_heading_accuracy', 'preferred_foot',
    'work_rate', 'body_type', 'release_clause_eur', 'player_positions',
    'attacking_short_passing', 'attacking_volleys', 'skill_dribbling',
    'skill_curve', 'skill_fk_accuracy', 'skill_long_passing', 'nationality_name',
    'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed',
    'movement_agility', 'movement_reactions', 'movement_balance',
    'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength',
    'power_long_shots', 'mentality_aggression', 'mentality_interceptions',
    'mentality_positioning', 'mentality_vision', 'mentality_penalties',
    'mentality_composure', 'defending_marking_awareness', 'club_name',
    'defending_standing_tackle', 'defending_sliding_tackle',
    'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
    'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed',
]
players_data = players_data[selected_columns]

# Main page title and description
st.title("FIFA'24 Player Analysis (2014-2024)")
st.write(
    "Welcome to the Football Data Analysis app. Explore various aspects of football player data, including attributes, player rankings, and more."
)



# Data Wrangling section
st.header("Data overview")
st.write("Let's start by exploring the data and its attributes.")

# Show first rows of the data
if st.checkbox("Show Data"):
    st.dataframe(players_data.head())

# Number of players in the dataset
if st.checkbox('Show Number of Players'):
    num_players = players_data['long_name'].nunique()
    st.write(f"Number of players in the dataset: {num_players}")

# Descriptive statistics
st.subheader("Descriptive Statistics")
st.write("Descriptive Statistics of Player Attributes.")
if st.checkbox("Show Descriptive Statistics"):
    st.write(players_data.describe())


# Find the oldest player in the dataset
oldest_player = players_data.loc[players_data['age'] == players_data['age'].max()]

if st.checkbox('Show Oldest Player'):
    st.write("Oldest Player Details:")
    st.write(f"Name: {oldest_player['long_name'].values[0]}")
    st.write(f"Club: {oldest_player['club_name'].values[0]}")
    st.write(f"Country: {oldest_player['nationality_name'].values[0]}")
    st.write(f"Age: {oldest_player['age'].values[0]}")
    st.write(f"Overall Rating: {oldest_player['overall'].values[0]}")


# Find the oldest player in the dataset
youngest_player = players_data.loc[players_data['age'] == players_data['age'].min()]

if st.checkbox('Show Youngest Player'):
    st.write("Youngest Player Details:")
    st.write(f"Name: {youngest_player['long_name'].values[0]}")
    st.write(f"Club: {youngest_player['club_name'].values[0]}")
    st.write(f"Country: {youngest_player['nationality_name'].values[0]}")
    st.write(f"Age: {youngest_player['age'].values[0]}")
    st.write(f"Overall Rating: {youngest_player['overall'].values[0]}")


# Define a function to categorize player positions
def categorize_positions(positions):
    if 'M' in positions:
        return 'Midfield'
    if any(role in positions for role in ['D', 'CB', 'RWB', 'LWB', 'LB', 'RB']):
        return 'Defense'
    if any(role in positions for role in ['CF', 'ST', 'RW', 'LW']):
        return 'Attacker'
    if 'GK' in positions:
        return 'Goalkeeper'
    return 'Unknown'


# Apply the categorization function to create a new column
players_data['position_category'] = players_data['player_positions'].apply(categorize_positions)

# Add a checkbox to show the pie chart
show_pie_chart = st.checkbox("Show Pie Chart of Player Positions")

if show_pie_chart:
    # Count the number of players in each category
    category_counts = players_data['position_category'].value_counts()
    
    # Create a pie chart using Plotly Express
    fig = px.pie(
        values=category_counts,
        names=category_counts.index,
        title='Player Position Categories Distribution'
    )
    
    # Display the pie chart
    st.plotly_chart(fig)
else:
    st.write("Check the box above to show distribution of player positions.")



# Add a checkbox to show the pie chart
show_pie_chart = st.checkbox("Show Pie Chart of Distribution of Players Preferred Foot")

if show_pie_chart:
    # Count the number of players in each category
    foot_counts = players_data['preferred_foot'].value_counts()
    
    # Create a pie chart using Plotly Express
    fig = px.pie(
        values=foot_counts,
        names=foot_counts.index,
        title='Player Preferred Foot Categories Distribution'
    )
    
    # Display the pie chart
    st.plotly_chart(fig)
else:
    st.write("Check the box above to show the pie chart for players preferred foot.")


# Create a checkbox to display the trend
show_trend = st.checkbox('Show Trend of Average Overall Rating Overtime')

if show_trend:
    # Convert the 'date' column to datetime format
    players_data['update_as_of'] = pd.to_datetime(players_data['update_as_of'])

    # Extract the year from the 'date' column and create a new column 'year'
    players_data['year'] = players_data['update_as_of'].dt.year

    # Group the data by 'year' and calculate the average overall rating for each year
    average_ratings_by_year = players_data.groupby('year')['overall'].mean()

    # Create a line plot to show the trend
    st.write('Trend of Average Overall Rating of Players Over the Years:')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(average_ratings_by_year.index, average_ratings_by_year.values, marker='o', linestyle='-')
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Overall Rating')
    ax.set_title('Trend of Average Overall Rating')
    
    # Set the y-axis limit to start from 0 and end at 100
    ax.set_ylim(40, 100)
    ax.grid(True)

    # Add data labels to the data points
    for year, rating in zip(average_ratings_by_year.index, average_ratings_by_year.values):
        ax.text(year, rating, f'{rating:.2f}', ha='center', va='bottom')

    st.pyplot(fig)


# Create a multiselect dropdown to select a team
selected_teams = st.multiselect('Select a Team to Show the Trend of Average Rating Overtime', players_data['club_name'].unique())

if selected_teams:
    selected_team = selected_teams[0]  # Get the first (and presumably only) selected team

    # Filter data based on the selected team
    team_data = players_data[players_data['club_name'] == selected_team]

    # Convert the 'date' column to datetime format
    team_data['update_as_of'] = pd.to_datetime(team_data['update_as_of'])

    # Extract the year from the 'date' column and create a new column 'year'
    team_data['year'] = team_data['update_as_of'].dt.year

    # Group the data by 'year' and calculate the average overall rating for each year
    average_ratings_by_year = team_data.groupby('year')['overall'].mean()

    # Create a line plot to show the trend
    st.write(f'Trend of Average Overall Rating for {selected_team} Over the Years:')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(average_ratings_by_year.index, average_ratings_by_year.values, marker='o', linestyle='-')
    
    # Set the y-axis limit to start from 0
    ax.set_ylim(40, 100)

    ax.set_xlabel('Year')
    ax.set_ylabel('Average Overall Rating')
    ax.set_title(f'Trend of Average Overall Rating for {selected_team}')
    ax.grid(True)

    # Add data labels to the data points
    for year, rating in zip(average_ratings_by_year.index, average_ratings_by_year.values):
        ax.text(year, rating, f'{rating:.2f}', ha='center', va='bottom')

    st.pyplot(fig)



# Create a multiselect dropdown to select a player
selected_players = st.sidebar.multiselect('Select Player', players_data['long_name'].unique())

if selected_players:
    # Retrieve the information for the selected player
    selected_player_info = players_data[players_data['long_name'] == selected_players[0]]  

    # Display the selected player's information in a tabular form
    st.subheader("Information of Selected Player")
    st.dataframe(selected_player_info.T)

    # Calculate and display descriptive statistics for numerical variables
    player_numerical_stats = selected_player_info.describe()
    st.subheader("Descriptive Statistics for Selected Player")
    st.dataframe(player_numerical_stats.T)

else:
    st.warning("Please select a player from the dropdown to view their information and statistics.")


# Create a multiselect dropdown to select a player
# selected_players = st.multiselect('Select a Player', players_data['long_name'].unique())

if selected_players:
    selected_player = selected_players[0]  # Get the first (and presumably only) selected player

    # Filter data based on the selected player
    player_data = players_data[players_data['long_name'] == selected_player]

    # Convert the 'date' column to datetime format
    player_data['update_as_of'] = pd.to_datetime(player_data['update_as_of'])

    # Extract the year from the 'date' column and create a new column 'year'
    player_data['year'] = player_data['update_as_of'].dt.year

    # Group the data by 'year' and calculate the average overall rating for each year
    player_average_ratings_by_year = player_data.groupby('year')['overall'].mean()

    # Create a line plot to show the trend
    st.write(f'Trend of Average Overall Rating for {selected_player} Over the Years:')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(player_average_ratings_by_year.index, player_average_ratings_by_year.values, marker='o', linestyle='-')
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Overall Rating')
    ax.set_title(f'Trend of Average Overall Rating for {selected_player}')
    ax.grid(True)

    # Set the y-axis limit to start from 0 and end at 100
    ax.set_ylim(0, 100)

    # Add data labels to the data points
    for year, rating in zip(player_average_ratings_by_year.index, player_average_ratings_by_year.values):
        ax.text(year, rating, f'{rating:.2f}', ha='center', va='bottom')

    st.pyplot(fig)


# Create a multiselect widget to choose one or more team
selected_teams = st.sidebar.multiselect("Select Team", players_data['club_name'])

if selected_teams:
    # Retrieve the information for the selected teams
    selected_team_info = players_data[players_data['club_name'].isin(selected_teams)]

    # Display the selected teams' information in a tabular form
    st.subheader("Information of Selected Teams")
    st.dataframe(selected_team_info)

    # Calculate and display descriptive statistics for numerical variables
    team_numerical_stats = selected_team_info.describe()
    st.subheader("Descriptive Statistics for Selected Teams")
    st.dataframe(team_numerical_stats.T)

else:
    st.warning("Please select a team from the dropdown to view their information and statistics.")


# Create a multiselect widget to choose one or more countries
selected_countries = st.sidebar.multiselect("Select Country", players_data['nationality_name'])

if selected_countries:
    # Retrieve the information for the selected countries
    selected_country_info = players_data[players_data['nationality_name'].isin(selected_countries)]

    # Display the selected countries' information in a tabular form
    st.subheader("Information of Selected Countries")
    st.dataframe(selected_country_info)

    # Calculate and display descriptive statistics for numerical variables
    country_numerical_stats = selected_country_info.describe()
    st.subheader("Descriptive Statistics for Selected Country")
    st.dataframe(country_numerical_stats.T)
else:
    st.warning("Please select a country from the dropdown to view their information and statistics.")


# Data Visualization section
st.header("Data Visualization")
st.write("Explore the distribution of player attributes and their relationships.")



# Select attributes to plot
selected_variable = st.multiselect("Select a player attribute to show distribution", players_data.columns[2:])

# Check if any attribute has been selected
if selected_variable:
    # Display histogram
    st.subheader(f"Histogram of {', '.join(selected_variable)}")
    plt.figure(figsize=(10, 6))
    for variable in selected_variable:
        plt.hist(players_data[variable], bins=20, alpha=0.7, edgecolor='black', label=variable)
    plt.xlabel("Attribute Values")
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {', '.join(selected_variable)}")
    plt.legend()
    st.pyplot()


# Correlation heatmap
corr_columns = players_data[['overall', 'potential', 'pace', 'shooting',
    'passing', 'dribbling', 'defending', 'physic', 
    'attacking_finishing', 'attacking_heading_accuracy', 'skill_dribbling',
    'skill_fk_accuracy', 'skill_long_passing',
    'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed',
    'movement_agility',  'movement_balance',
    'power_shot_power', 'power_jumping', 'power_stamina', 
    'power_long_shots', 
    'mentality_positioning', 'mentality_vision', 'mentality_penalties',
    'mentality_composure', 'defending_marking_awareness', 
    'defending_standing_tackle', 'defending_sliding_tackle']]

st.subheader("Show Correlation Heatmap of Player Attributes")
st.write("Explore the relationships between key player attributes.")
if st.checkbox("Show Correlation Heatmap"):
    # Create a heatmap of attribute correlations
    plt.figure(figsize=(20, 16))
    sns.heatmap(corr_columns.corr(), cmap='coolwarm', annot=True, fmt='.2f')
    plt.title("Heatmap Showing Relationship Between Player Attributes")
    st.pyplot()

# Top Players by Average Overall Rating section
# Using HTML to style the header text
# st.write("<h2>Top 10 Teams by Average Overall Rating of Players</h2>", unsafe_allow_html=True)
st.subheader("Top Players by Average Overall Rating Over Time")
st.write("Visualize the top players by their average overall rating")

# Group by player_name and calculate the average overall rating
top_10_players = players_data.groupby('long_name')[['overall']].mean().sort_values(by='overall', ascending=False).head(10)

# Plot the top players
if st.checkbox("Show Top 10 Players"):
    plt.figure(figsize=(12, 6))
    bars = plt.barh(top_10_players.index, top_10_players['overall'], color='skyblue')
    plt.xlabel('Average Overall Rating')
    
    st.subheader('Top 10 Players by Average Overall Rating Over Time')
    plt.gca().invert_yaxis()  # Invert the y-axis for better visualization

    # Add data labels to the bars
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', color='black')

    st.pyplot()


# Top tems by Average Overall Rating section
st.subheader("Top 10 Teams by Average Overall Rating of Players")
st.write("Visualize the top 10 Teams by their Players Average Overall Rating")

# Group by player_name and calculate the average overall rating
top_10_teams = players_data.groupby('club_name')[['overall']].mean().sort_values(by='overall', ascending=False).head(10)

# Plot the top players
if st.checkbox("Show Top 10 Teams"):
    plt.figure(figsize=(12, 6))
    bars = plt.barh(top_10_teams.index, top_10_teams['overall'], color='skyblue')
    plt.xlabel('Average Overall Rating')
    plt.title('Top 10 Teams by Average Overall Rating of their Players')
    plt.gca().invert_yaxis()  # Invert the y-axis for better visualization

    # Add data labels to the bars
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', color='black')

    st.pyplot()

# Create a multiselect dropdown to select one or more categories
selected_categories = st.multiselect('Select Position to View Top 10 Players', players_data['position_category'].unique())

if selected_categories:
    # Filter data based on the selected category
    filtered_data = players_data[players_data['position_category'].isin(selected_categories)]

    # Calculate the mean overall rating for each player in the category
    avg_ratings = filtered_data.groupby('long_name')[['overall']].mean()

    # Sort the players by average rating in descending order
    top_players = avg_ratings.sort_values(by='overall', ascending=False).head(10)

    # Display a bar chart
    st.write(f'Top 10 Players by Average Overall Rating for Selected Categories (2014 - 2024)')
    fig, ax = plt.subplots()
    bars = ax.bar(top_players.index, top_players['overall'], color='teal')
    plt.xticks(rotation=90)

    # Add data labels to the bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}', (bar.get_x() + bar.get_width() / 2, height),
                    ha='center', va='bottom', fontsize=8, color='black')

    st.pyplot(fig)


# End of the app
st.sidebar.write("Developed by Simon-Peter Osadiapet")
