<<<<<<< HEAD
import streamlit as st
import pandas as pd

#loading datasets
#creating a list containing all datasets 
list_of_names=['Country', 'League', 'Player', 'Team', 'Team_Attributes', 'Player_Attributes', 'Match']

#create empty list for datasets
dataframe_list=[]

#appending datasets into the list 
for i in range(len(list_of_names)):
    df=pd.read_csv('C:/Users/osadi/OneDrive/Desktop/Projects\Europe-Football-Data-Analysis-/'+list_of_names[i]+'.csv')
    dataframe_list.append(df)


#calling each of the datasets 
countries=dataframe_list[0]
league=dataframe_list[1]
players=dataframe_list[2]
teams=dataframe_list[3]
team_attributes=dataframe_list[4]
player_attributes=dataframe_list[5]
matches=dataframe_list[6]

#
def main():
    st.title('Football Match Data Analysis App')

    # Data Summary
    st.subheader('Data Summary')
    st.write(team_attributes.head())  # Display the first few rows of the data
    st.write(f'Data Shape: {team_attributes.shape}')

    # Data Exploration
    st.subheader('Data Exploration')

    # Interactive Widgets for Data Exploration
    selected_columns = st.multiselect('Select columns to display:', team_attributes.columns)
    if selected_columns:
        st.write(team_attributes[selected_columns])

    # Data Visualization
    st.subheader('Data Visualization')

    # You can add your data visualization code here to explore the data visually.
    # For example:
    # st.bar_chart(data['some_column'])
    # st.line_chart(data['another_column'])


if __name__ == '__main__':
    main()
=======
import streamlit as st
import pandas as pd

#loading datasets
#creating a list containing all datasets 
list_of_names=['Country', 'League', 'Player', 'Team', 'Team_Attributes', 'Player_Attributes', 'Match']

#create empty list for datasets
dataframe_list=[]

#appending datasets into the list 
for i in range(len(list_of_names)):
    df=pd.read_csv('C:/Users/osadi/OneDrive/Desktop/Projects\Europe-Football-Data-Analysis-/'+list_of_names[i]+'.csv')
    dataframe_list.append(df)


#calling each of the datasets 
countries=dataframe_list[0]
league=dataframe_list[1]
players=dataframe_list[2]
teams=dataframe_list[3]
team_attributes=dataframe_list[4]
player_attributes=dataframe_list[5]
matches=dataframe_list[6]

#
def main():
    st.title('Football Match Data Analysis App')

    # Data Summary
    st.subheader('Data Summary')
    st.write(team_attributes.head())  # Display the first few rows of the data
    st.write(f'Data Shape: {team_attributes.shape}')

    # Data Exploration
    st.subheader('Data Exploration')

    # Interactive Widgets for Data Exploration
    selected_columns = st.multiselect('Select columns to display:', team_attributes.columns)
    if selected_columns:
        st.write(team_attributes[selected_columns])

    # Data Visualization
    st.subheader('Data Visualization')

    # You can add your data visualization code here to explore the data visually.
    # For example:
    # st.bar_chart(data['some_column'])
    # st.line_chart(data['another_column'])


if __name__ == '__main__':
    main()
>>>>>>> 7693083983d44a0160997b731185dbc6e6e38269
