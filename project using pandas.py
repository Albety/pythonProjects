import pandas as pd

inventory = pd.read_csv('inventory.csv')
print(inventory.head(10))

staten_island = inventory[inventory['location'] == 'Staten Island']
product_request = staten_island['product_description']
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

inventory['in_stock'] = inventory['quantity'].apply(lambda quantity: True if quantity > 0 else False)
inventory['total_value'] = inventory['quantity'] * inventory['price']

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory)

############################################################################################################
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('jeopardy.csv')
df.rename(columns={
  ' Air Date': 'Air Date',
  ' Round': 'Round',
  ' Category': 'Category',
  ' Value': 'Value',
  ' Question': 'Question',
  ' Answer': 'Answer'
}, inplace=True)

### find question where all words in list is substring of it.
def filter_data(data, words):
  filter = lambda x: all([word.lower() in x.lower() for word in words])
  return data[data["Question"].apply(filter)].reset_index()

filtered = filter_data(df, ["King", "England"])
#print(filtered["Question"])

df["Float Value"] = df["Value"].apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)

filtered = filter_data(df, ["King"])
print(filtered["Float Value"].mean())

def get_answer_counts(data):
    return data["Answer"].value_counts()

print(get_answer_counts(filtered))
