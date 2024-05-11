import pandas as pd

# Read data from CSV file

df = pd.read_csv('POC_Trainee.csv')
# df = pd.read_csv('deduplicated_data_final.csv')

df['group_id'] = None

# Function to assign group IDs
def assign_group(row, group_id):
    if df.at[row, 'group_id'] is not None:
        return
    df.at[row, 'group_id'] = group_id

    record_id1_val = df.at[row, 'record_id1']
    record_id2_val = df.at[row, 'record_id2']

    for i in range(len(df)):
        if df.at[i, 'group_id'] is None:
            if df.at[i, 'record_id1'] == record_id2_val:
                assign_group(i, group_id)
            elif df.at[i, 'record_id2'] == record_id2_val:
                assign_group(i, group_id)

# Assign group IDs
#program starts from here
group_id = 1
for i in range(len(df)):
    if df.at[i, 'group_id'] is None:
        assign_group(i, group_id)
        group_id += 1

# Output the result
print(df[['record_id1', 'group_id']])
