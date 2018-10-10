import pandas as pd

pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('/Users/mtony/Downloads/splunk_ces_data.csv')
df.columns = ['id', 'timestamp']
df1 = df.head(10)
# df1['timestamp'] = df1['timestamp'].utcnow
# df1.groupby(['id']).count()
df1['timestamp'] = pd.to_datetime(df1['timestamp'])
df1.groupby(["id"]).count()