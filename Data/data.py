# import pandas as pd
# df=pd.read_csv('3G AND 4G.csv')
# output_csv='4G.csv'
# filter_df=df[(df['radio']=='LTE')]
# india_df = filter_df[
#     (filter_df['lat'] >= 6.8) & (filter_df['lat'] <= 37.6) &          # longitude and latitude extent of India
#     (filter_df['long'] >= 68.7) & (filter_df['long'] <= 97.25)
# ]
# # del india_df['changeable_0']
# # del india_df['range']
# # del india_df['sample']
# # del india_df['changeable_1']
# # del india_df['created']
# # del india_df['updated']
# # del india_df['avgsignal']
# india_df.to_csv(output_csv,index=False)
# print(india_df.info())

import pandas as pd

# # Load your CSV file
# df = pd.read_csv('3G.csv')
# df2= pd.read_csv('operators_name.csv')
# # # # # Get unique values from the 'mnc' column
# # # # # unique_mnc = df[['mnc','mcc']].drop_duplicates()
# # # # # unique_mnc.to_csv('operator.csv',index=False)

# # # # # Print the unique values
# # # # print("Distinct MNC values:")
# # # # print(unique_mnc)

# merged_df = pd.merge(df, df2[['mcc', 'mnc', 'Operator']], on=['mcc', 'mnc'], how='left', suffixes=('', '_operators_name'))

# # Rename the 'Operator_rty' column to 'Operator'
# merged_df.rename(columns={'Operator_operators_name': 'Operator'}, inplace=True)

# # Save the updated DataFrame to a new CSV file
# merged_df.to_csv('updated_3G.csv', index=False)

df=pd.read_csv('updated_4G.csv')
output_csv="4G_Jio.csv"
filter_df=df[(df['Operator']=="Jio")]
filter_df.to_csv(output_csv,index=False)
print(filter_df.info())