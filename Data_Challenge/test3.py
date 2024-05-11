import pandas as pd

# Read data from CSV file
df = pd.read_csv('deduplicated_data_final.csv')

# Initialize group_id column with NaN
df['group_id'] = None

# Create a dictionary to store the mapping of record_id to group_id
record_to_group = {}

# Assign group IDs
group_id = 1
for index, row in df.iterrows():
    if row['group_id'] is None:
        record_id1 = row['record_id1']
        record_id2 = row['record_id2']
        
        # Check if record_id1 already has a group_id assigned
        if record_id1 in record_to_group:
            group_id = record_to_group[record_id1]
        # Check if record_id2 already has a group_id assigned
        elif record_id2 in record_to_group:
            group_id = record_to_group[record_id2]
        
        # Update group_id for record_id1 and record_id2
        df.loc[(df['record_id1'] == record_id1) | (df['record_id2'] == record_id1), 'group_id'] = group_id
        df.loc[(df['record_id1'] == record_id2) | (df['record_id2'] == record_id2), 'group_id'] = group_id
        
        # Store the mapping of record_id to group_id
        record_to_group[record_id1] = group_id
        record_to_group[record_id2] = group_id
        
        # Increment group_id for the next group
        group_id += 1

# Output the result
print(df[['record_id1', 'group_id']].to_string(index=False))
