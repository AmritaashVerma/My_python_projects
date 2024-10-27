#src is https://www.football-data.co.uk/englandm.php
import pandas as pd

#reading 1 csv file from the website

df_premier22 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')

#showing dataframe

pd.options.display.max_rows = None
pd.options.display.max_columns = None
print(df_premier22)

#rename columns 

df_premier22.rename(columns={'FTHG':'home_goals',
                             'FTAG':'away_goals'}, inplace=True)
print(df_premier22)