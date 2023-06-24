#text extraction from websites 

import pandas as pd 

list_of_tables = pd.read_html('https://en.wikipedia.org/wiki/Adolf_Hitler')

print(list_of_tables[1])