import pandas as pd

df = pd.read_csv('accident_dataset.csv')

attributes = df.columns[:-1]
attribute_values = {attr: df[attr].unique().tolist() for attr in attributes}

specific_h = ['0'] * len(attributes)
general_h = ['?'] * len(attributes)

# Candidate Elimination algorithm
for index, row in df.iterrows():
    if row['label'] == 'positive':  
        for i, attr in enumerate(attributes):
            if specific_h[i] == '0':
                specific_h[i] = row[attr]
            elif specific_h[i] != row[attr]:
                specific_h[i] = '?'
            if general_h[i] != '?' and general_h[i] != row[attr]:
                general_h[i] = '?'
    else:  
        for i, attr in enumerate(attributes):
            if specific_h[i] == row[attr]:
                specific_h[i] = '?'
            if specific_h[i] != '?' and general_h[i] != '?' and specific_h[i] != general_h[i]:
                temp = general_h[i]
                general_h[i] = ['?'] if specific_h[i] == '0' else specific_h[i]
                general_h[i] = [temp] if temp == '0' else [temp, specific_h[i]]

print("Final Version Space:")
print("Specific Hypothesis:", specific_h)
print("General Hypothesis:", general_h)