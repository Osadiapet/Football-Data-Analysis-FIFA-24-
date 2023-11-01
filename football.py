<<<<<<< HEAD
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

players_data = pd.read_csv('C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/male_players.csv')

# Streamlit app
st.title('Top Players by Category')

# Create a dropdown to select the category
selected_category = st.selectbox('Select Category', players_data['position_category'].unique())

# Filter data based on the selected category
filtered_data = players_data[players_data['position_category'] == selected_category]

# Calculate the mean overall rating for each player in the category
avg_ratings = filtered_data.groupby('long_name')[['overall']].mean()

# Sort the players by average rating in descending order
top_players = avg_ratings.sort_values(by='overall', ascending=False).head(10)

# Display a bar chart
st.write(f'Top 10 {selected_category} Players by Average Overall Rating')
fig, ax = plt.subplots()
ax.bar(top_players.index, top_players['overall'], color='teal')
plt.xticks(rotation=45)
st.pyplot(fig)

# Display a table with player names and their average ratings
st.write(f'Top Players in {selected_category} (Table View):')
st.dataframe(top_players)
=======
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

players_data = pd.read_csv('C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/male_players.csv')

# Streamlit app
st.title('Top Players by Category')

# Create a dropdown to select the category
selected_category = st.selectbox('Select Category', players_data['position_category'].unique())

# Filter data based on the selected category
filtered_data = players_data[players_data['position_category'] == selected_category]

# Calculate the mean overall rating for each player in the category
avg_ratings = filtered_data.groupby('long_name')[['overall']].mean()

# Sort the players by average rating in descending order
top_players = avg_ratings.sort_values(by='overall', ascending=False).head(10)

# Display a bar chart
st.write(f'Top 10 {selected_category} Players by Average Overall Rating')
fig, ax = plt.subplots()
ax.bar(top_players.index, top_players['overall'], color='teal')
plt.xticks(rotation=45)
st.pyplot(fig)

# Display a table with player names and their average ratings
st.write(f'Top Players in {selected_category} (Table View):')
st.dataframe(top_players)
>>>>>>> 7693083983d44a0160997b731185dbc6e6e38269
