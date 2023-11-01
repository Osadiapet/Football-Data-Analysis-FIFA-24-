<<<<<<< HEAD
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the datasets
# Add the paths to your CSV files
data_paths = {
    'Country': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Country.csv',
    'League': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/League.csv',
    'Player': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Player.csv',
    'Team': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Team.csv',
    'Team_Attributes': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Team_Attributes.csv',
    'Player_Attributes': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Player_Attributes.csv',
    'Match': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Match.csv'
}

# Create empty dictionary for datasets
dataframes = {}

# Load datasets
for name, path in data_paths.items():
    dataframes[name] = pd.read_csv(path)

def main():
    st.title('Football Match Data Analysis App')

    # Data Summary
    st.subheader('Data Summary')
    selected_dataset = st.selectbox('Select a dataset', list(dataframes.keys()))
    st.write(dataframes[selected_dataset].head())  # Display the first few rows of the selected dataset
    st.write(f'Data Shape: {dataframes[selected_dataset].shape}')

    # Data Exploration
    st.subheader('Data Exploration')

    # Interactive Widgets for Data Exploration
    selected_columns = st.multiselect('Select columns to display:', dataframes[selected_dataset].columns)
    if selected_columns:
        st.write(dataframes[selected_dataset][selected_columns])

    # Data Visualization
    st.subheader('Data Visualization')

    # You can add your data visualization code here to explore the data visually.
    # For example, your density plots and countplots:

    if st.button("Visualize Variables"):
        visualize_variables(dataframes[selected_dataset])

def visualize_variables(data):
    # Select the variables you want to plot
    variables_to_plot = ['defenceAggression', 'defenceTeamWidth', 'defencePressure',
                         'buildUpPlayPassing', 'chanceCreationCrossing',
                         'chanceCreationShooting', 'chanceCreationPassing', 'buildUpPlaySpeed']

    # Create subplots for the variables
    plt.figure(figsize=(18, 12))  # Adjust the figure size as needed

    # Loop through the selected variables and create density plots
    for i, variable in enumerate(variables_to_plot, 1):
        plt.subplot(2, 4, i)  # 2 rows, 4 columns of subplots
        sns.kdeplot(data[variable], shade=True, color='b')
        plt.title(f'Distribution of {variable}')
        plt.xlabel(variable)

    plt.tight_layout()  # Ensure subplots do not overlap
    st.pyplot()

    # Select the categorical variables
    categorical_variables = [
        'buildUpPlaySpeedClass', 'buildUpPlayDribblingClass', 'buildUpPlayPassingClass',
        'buildUpPlayPositioningClass', 'chanceCreationPassingClass', 'chanceCreationCrossingClass',
        'chanceCreationShootingClass', 'chanceCreationPositioningClass', 'defencePressureClass',
        'defenceAggressionClass', 'defenceTeamWidthClass', 'defenceDefenderLineClass',
    ]

    # Create subplots for the categorical variables
    plt.figure(figsize=(18, 12))

    for i, variable in enumerate(categorical_variables, 1):
        plt.subplot(4, 4, i)  # Create a 4x4 grid of subplots
        sns.countplot(data=data, x=variable, order=data[variable].value_counts().index)
        plt.title(f'{variable} Distribution')
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    plt.tight_layout()  # Ensure subplots do not overlap
    st.pyplot()

    teams_num = data[variables_to_plot]
    # Let's see how these attributes relate with each other with a heatmap
    plt.figure(figsize=(16, 14))
    sns.heatmap(teams_num.corr(), cmap='coolwarm', annot=True, fmt='.2f')
    plt.title('Heatmap Showing Relationship Between Variables')
    st.pyplot()

    # Your additional code
    if st.button("Perform Chi-Square Tests"):
        perform_chi_square_tests(data)

def perform_chi_square_tests(data):
    # List of independent variables
    independent_vars = [
        'buildUpPlaySpeedClass', 'buildUpPlayDribblingClass', 'buildUpPlayPassingClass',
        'buildUpPlayPositioningClass', 'chanceCreationPassingClass', 'chanceCreationCrossingClass',
        'chanceCreationShootingClass', 'chanceCreationPositioningClass', 'defencePressureClass',
        'defenceAggressionClass',
    'defenceTeamWidthClass', 'defenceDefenderLineClass',
    ]

    # Create an empty DataFrame to store the results
    results = pd.DataFrame(columns=['Variable', 'Chi-Square Statistic', 'Degrees of Freedom', 'P-Value'])

    # Loop through independent variables and perform chi-square tests
    for var in independent_vars:
        # Create a contingency table
        contingency_table = pd.crosstab(data[var], data['HomeResults'])

        # Perform chi-square test
        chi2, p, dof, _ = stats.chi2_contingency(contingency_table)

        # Append results to the results DataFrame
        results = results.append({
            'Variable': var,
            'Chi-Square Statistic': chi2,
            'Degrees of Freedom': dof,
            'P-Value': p
        }, ignore_index=True)

    # Display the results
    st.write("Chi-Square Test Results:")
    st.write(results)

if __name__ == '__main__':
    main()

=======
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the datasets
# Add the paths to your CSV files
data_paths = {
    'Country': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Country.csv',
    'League': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/League.csv',
    'Player': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Player.csv',
    'Team': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Team.csv',
    'Team_Attributes': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Team_Attributes.csv',
    'Player_Attributes': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Player_Attributes.csv',
    'Match': 'C:/Users/osadi/OneDrive/Desktop/Projects/Europe-Football-Data-Analysis-/Match.csv'
}

# Create empty dictionary for datasets
dataframes = {}

# Load datasets
for name, path in data_paths.items():
    dataframes[name] = pd.read_csv(path)

def main():
    st.title('Football Match Data Analysis App')

    # Data Summary
    st.subheader('Data Summary')
    selected_dataset = st.selectbox('Select a dataset', list(dataframes.keys()))
    st.write(dataframes[selected_dataset].head())  # Display the first few rows of the selected dataset
    st.write(f'Data Shape: {dataframes[selected_dataset].shape}')

    # Data Exploration
    st.subheader('Data Exploration')

    # Interactive Widgets for Data Exploration
    selected_columns = st.multiselect('Select columns to display:', dataframes[selected_dataset].columns)
    if selected_columns:
        st.write(dataframes[selected_dataset][selected_columns])

    # Data Visualization
    st.subheader('Data Visualization')

    # You can add your data visualization code here to explore the data visually.
    # For example, your density plots and countplots:

    if st.button("Visualize Variables"):
        visualize_variables(dataframes[selected_dataset])

def visualize_variables(data):
    # Select the variables you want to plot
    variables_to_plot = ['defenceAggression', 'defenceTeamWidth', 'defencePressure',
                         'buildUpPlayPassing', 'chanceCreationCrossing',
                         'chanceCreationShooting', 'chanceCreationPassing', 'buildUpPlaySpeed']

    # Create subplots for the variables
    plt.figure(figsize=(18, 12))  # Adjust the figure size as needed

    # Loop through the selected variables and create density plots
    for i, variable in enumerate(variables_to_plot, 1):
        plt.subplot(2, 4, i)  # 2 rows, 4 columns of subplots
        sns.kdeplot(data[variable], shade=True, color='b')
        plt.title(f'Distribution of {variable}')
        plt.xlabel(variable)

    plt.tight_layout()  # Ensure subplots do not overlap
    st.pyplot()

    # Select the categorical variables
    categorical_variables = [
        'buildUpPlaySpeedClass', 'buildUpPlayDribblingClass', 'buildUpPlayPassingClass',
        'buildUpPlayPositioningClass', 'chanceCreationPassingClass', 'chanceCreationCrossingClass',
        'chanceCreationShootingClass', 'chanceCreationPositioningClass', 'defencePressureClass',
        'defenceAggressionClass', 'defenceTeamWidthClass', 'defenceDefenderLineClass',
    ]

    # Create subplots for the categorical variables
    plt.figure(figsize=(18, 12))

    for i, variable in enumerate(categorical_variables, 1):
        plt.subplot(4, 4, i)  # Create a 4x4 grid of subplots
        sns.countplot(data=data, x=variable, order=data[variable].value_counts().index)
        plt.title(f'{variable} Distribution')
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    plt.tight_layout()  # Ensure subplots do not overlap
    st.pyplot()

    teams_num = data[variables_to_plot]
    # Let's see how these attributes relate with each other with a heatmap
    plt.figure(figsize=(16, 14))
    sns.heatmap(teams_num.corr(), cmap='coolwarm', annot=True, fmt='.2f')
    plt.title('Heatmap Showing Relationship Between Variables')
    st.pyplot()

    # Your additional code
    if st.button("Perform Chi-Square Tests"):
        perform_chi_square_tests(data)

def perform_chi_square_tests(data):
    # List of independent variables
    independent_vars = [
        'buildUpPlaySpeedClass', 'buildUpPlayDribblingClass', 'buildUpPlayPassingClass',
        'buildUpPlayPositioningClass', 'chanceCreationPassingClass', 'chanceCreationCrossingClass',
        'chanceCreationShootingClass', 'chanceCreationPositioningClass', 'defencePressureClass',
        'defenceAggressionClass',
    'defenceTeamWidthClass', 'defenceDefenderLineClass',
    ]

    # Create an empty DataFrame to store the results
    results = pd.DataFrame(columns=['Variable', 'Chi-Square Statistic', 'Degrees of Freedom', 'P-Value'])

    # Loop through independent variables and perform chi-square tests
    for var in independent_vars:
        # Create a contingency table
        contingency_table = pd.crosstab(data[var], data['HomeResults'])

        # Perform chi-square test
        chi2, p, dof, _ = stats.chi2_contingency(contingency_table)

        # Append results to the results DataFrame
        results = results.append({
            'Variable': var,
            'Chi-Square Statistic': chi2,
            'Degrees of Freedom': dof,
            'P-Value': p
        }, ignore_index=True)

    # Display the results
    st.write("Chi-Square Test Results:")
    st.write(results)

if __name__ == '__main__':
    main()

>>>>>>> 7693083983d44a0160997b731185dbc6e6e38269
