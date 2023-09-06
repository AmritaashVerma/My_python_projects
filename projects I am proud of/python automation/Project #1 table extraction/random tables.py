import pandas as pd 

tables = pd.read_html('https://international.collegeboard.org/students/sat/acceptance-india')

print(tables)