import pandas as pd
tables = pd.read_html('table_data.html')
print('Tables found:', len(tables))
df1 = tables[0]  # Save first table in variable df1
df2 = tables[1]  # Saving next table in variable df2

print('First Table')
print(df1)
print('Another Table')
print(df2)