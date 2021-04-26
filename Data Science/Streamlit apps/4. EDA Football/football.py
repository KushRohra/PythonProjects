import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import date

st.title('NFL Football Stats (Rushing) Explorer')

st.markdown("""
This app performs simple webscraping of NFL Football player stats data (focusing on Rushing)!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")

currentYear = date.today().year
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990, currentYear))))

# Web scraping of NFL Players
@st.cache
def load_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/rushing.htm"
    html = pd.read_html(url, header = 1)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
    raw = raw.fillna(0)
    player_stats = raw.drop(['Rk'], axis=1)
    return player_stats
player_stats = load_data(selected_year)

# Sidebar Team Selection
sorted_unique_team = sorted(player_stats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar - Position selection
unique_position = ['RB', 'QB', 'WR', 'FB', 'TE']
selected_position = st.sidebar.multiselect('Position', unique_position, unique_position)

# Filtering data
df_selected_team = player_stats[(player_stats.Tm.isin(selected_team)) & (player_stats.Pos.isin(selected_position))]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns')
st.dataframe(df_selected_team)

# Download NFL Player Stats data
def download_file(df):
	csv = df.to_csv(index=False)
	b64 = base64.b64encode(csv.encode()).decode() # stromg <-> bytes conversion
	href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv"> Download CSV File</a>'
	return href
st.markdown(download_file(df_selected_team), unsafe_allow_html=True)

# Heatmap
if st.button('Intercorrelation Heatmap'):
	st.header('Intercorrelation Matrix Heatmap')
	df_selected_team.to_csv('output.csv', index=False)
	df = pd.read_csv('output.csv')

	corr = df.corr()
	mask = np.zeros_like(corr)
	mask[np.triu_indices_from(mask)] = True
	with sns.axes_style("white"):
		f, ax = plt.subplots(figsize=(7, 5))
		ax = sns.heatmap(corr, mask=mask, square=True)
	st.pyplot(f)