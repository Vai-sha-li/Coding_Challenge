import pandas as pd

# Sample input data
data = {
    'record_id1': [1480, 3310, 4333, 391, 557, 1978, 3977, 268, 4710, 4856, 4128, 1574, 188, 753, 2072, 4144, 187, 815, 1001, 1012, 2192, 2331, 3074, 4148, 3687, 909, 1272, 579, 1232, 4153],

    'record_id2': [2, 2, 2, 17, 23, 28, 37, 42, 42, 43, 49, 51, 61, 61, 61, 73, 82, 84, 85, 85, 82, 84, 82, 84, 89, 92, 92, 107, 114, 114]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize group_id column with NaN
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
group_id = 1
for i in range(len(df)):
    if df.at[i, 'group_id'] is None:
        assign_group(i, group_id)
        group_id += 1

# Output the result
print(df[['record_id1', 'group_id']])
