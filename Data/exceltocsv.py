# import pandas as pd
# excel_file = 'area_pop_sdt.xlsx'
# sheet_name = 'Sheet1' 
# df = pd.read_excel(excel_file, sheet_name=sheet_name)
# csv_file = 'area_pop_sdt.csv'
# df.to_csv(csv_file, index=False)

# import pandas as pd 
# df=pd.read_csv('subdistrict_trial2.csv')
# df1=pd.read_csv('states.csv')
# df2=pd.read_csv('district.csv') 
# merge_df=pd.merge(df,df1,how='inner',left_on='State_code',right_on='State_code')
# merge_df=pd.merge(merge_df,df2,how='inner',left_on='District_code',right_on='District_code')
# merge_df.to_csv('final1.csv',index=False)
# print(merge_df)
# df=df.dropna()
# print(df.info())
# df.to_csv('clean.csv',index=False)
# print(df.columns)
# df=df.rename(columns={'A-1 NUMBER OF VILLAGES, TOWNS, HOUSEHOLDS, POPULATION AND AREA': 'State_code',
#                       'Unnamed: 1' :'District_code',
#                       'Unnamed: 2' : 'Subdistrict_code',
#                       'Unnamed: 3' : 'Subdistrict',
#                       'Unnamed: 4' : 'Subdistrict_name',
#                       'Unnamed: 5' : 'T/r/u',
#                       'Unnamed: 6' : 'Number_of_villages_habitated',
#                       'Unnamed: 7' : 'Unhabitated',
#                       'Unnamed: 8': 'Number of towns',
#                       'Unnamed: 9' : 'Number of households',
#                       'Unnamed: 10' : 'population',
#                       'Unnamed: 13' : 'Area',
#                       'Unnamed: 14': 'population density'
# }) 
# del df['Unnamed: 11']
# del df['Unnamed: 12']
# df.to_csv("clean.csv",index=False)
# state=df[['State_code','Subdistrict_name']]
# state=state.drop_duplicates(subset=['State_code'])
# state.to_csv('states.csv',index=False)
# print(state)
# districts=df[['State_code','District_code','Subdistrict_name']]
# districts=districts.drop_duplicates(subset=['State_code','District_code'])
# districts=districts[(districts['District_code']!=0)]
# districts.to_csv('district.csv',index=False)
# print(districts)

# districts=df[['State_code','District_code','Subdistrict_code','Subdistrict_name','T/r/u','Number of households','population','Area','population density']]
# # districts=districts.drop_duplicates(subset=['State_code','District_code','Subdistrict_code'])
# districts=districts[(districts['District_code']!=0)]
# districts=districts[(districts['Subdistrict_code']!=0)]
# districts.to_csv('subdistrict_trial2.csv',index=False)
# print(districts)
# filter_df=df[(df['Subdistrict']=='SUB-DISTRICT')]
# filter_df=filter_df.dropna()
# filter_df.to_csv('subdistrict.csv',index=False)
# print(filter_df.info())




# import pandas as pd
# df = pd.read_csv('subdistrict.csv')
# total_df = df[df['T/r/u'] == 'Total']
# rural_df = df[df['T/r/u'] == 'Rural']
# urban_df=  df[df['T/r/u'] == 'Urban']
# merged_df1 = pd.merge(total_df, rural_df, on=['State_code_x', 'District_code', 'Subdistrict_code', 'Subdistrict_name_x'], suffixes=('_total', '_rural'))
# merged_df = pd.merge(merged_df1, urban_df, on=['State_code_x', 'District_code', 'Subdistrict_code', 'Subdistrict_name_x'])
# merged_df.to_csv('final3.csv',index=False)
# print(merged_df)
# merged_df['% Rural Population'] = (merged_df['population_rural'] / merged_df['population_total']) * 100
# merged_df['% Rural Households'] = (merged_df['Number of households_rural']/merged_df['Number of households_total']) * 100
# merged_df['% Rural Area'] = (merged_df['Area_rural'] / merged_df['Area_total']) * 100
# merged_df['% Urban Population'] = (merged_df['population'] / merged_df['population_total']) * 100
# merged_df['% Urban Households'] = (merged_df['Number of households']/merged_df['Number of households_total']) * 100
# merged_df['% Urban Area'] = (merged_df['Area'] / merged_df['Area_total']) * 100
# merged_df['Household density']=(merged_df['Number of households_total']/merged_df['Area_total'])
# final_df = merged_df[['State_code_x', 'District_code', 'Subdistrict_code', 'Subdistrict_name_x', 'Number of households_total', 'population_total', 'Area_total', 'population density_total', 'Subdistrict_name_y_total','Subdistrict_name_total','Household density','% Rural Population','% Rural Households', '% Rural Area','% Urban Population','% Urban Households', '% Urban Area']]
# final_df=final_df.rename(columns={'Subdistrict_name_total' : 'District_name',
#                                   'Subdistrict_name_y_total' : 'State_name',
#                                   'State_code_x' : 'State_code',
#                                   'Subdistrict_name_x' : 'Subdistrict_name'})
# final_df.to_csv('final3.csv', index=False)
# print(final_df)

# import pandas as pd
# # income_file = 'Area_state.csv'
# # income_df = pd.read_csv(income_file)
# cell_tower_file = '../3G_Income/3G.csv'  
# cell_tower_df = pd.read_csv(cell_tower_file)
# # merged_df = pd.merge(income_df,cell_tower_df, how='inner',left_on='stname',right_on='stname')
# cell_tower_df['cell_towers_per_area'] = cell_tower_df['number_of_cell_towers'] / cell_tower_df['Area']
# cell_tower_df['income_per_area'] = cell_tower_df['Household_income_annual'] / cell_tower_df['Area']


# # # Save the result to a new file
# # # result_file = '../5G_Income/5G.csv'  # Replace with your desired file path
# cell_tower_df.to_csv(cell_tower_file, index=False)

# import pandas as pd
# file_1='../3G_CSV/updated_3G.csv'
# file_2='../delhitowers/3G.csv'


# import pandas as pd
# df1=pd.read_csv('fulldata.csv')
# df2=pd.read_csv('./5G_Number_of_cell_towers_csv/5G_Vodafone.csv')
# merged_df1=pd.merge(df1,df2,how='inner',left_on=['Subdistrict_name','District_name'],right_on=['sdtname','dtname'])
# merged_df2=pd.merge(df1,df2,how='inner',left_on=['Subdistrict_name','State_name'],right_on=['sdtname','stname'])
# merged_df=pd.concat([merged_df1,merged_df2]).drop_duplicates()
# merged_df.to_csv('./5G_Metrics/5G_Vodafone.csv',index=False)
# print(merged_df)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create scatter plot with a best-fit line
# sns.regplot(x='Area_total', y='number_of_cell_towers', data=df, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
# plt.title('Scatter Plot of Area vs Number of Cell Towers')
# plt.xlabel('Area')
# plt.ylabel('Number of Cell Towers')
# plt.show()


# Ensure 'Area' and 'Number_of_cell_towers' are in the DataFrame
# You can check by printing the column names
# print(df.columns)

# Calculate the correlation matrix
# df= df[['Area_total', 'number_of_cell_towers']]
# sns.pairplot(df)
# plt.title('Pair Plot of Area and Number of Cell Towers')
# plt.show()
# sns.jointplot(x='Area_total', y='number_of_cell_towers', data=df, kind='scatter')
# plt.title('Joint Plot of Area vs Number of Cell Towers')
# plt.show()

# import statsmodels.api as sm

# X = df['Area_total']
# y = df['number_of_cell_towers']
# X = sm.add_constant(X)  # Adds a constant term to the predictor
# model = sm.OLS(y, X).fit()
# residuals = model.resid

# sns.residplot(x=df['Area_total'], y=residuals, lowess=True)
# plt.title('Residual Plot of Area vs Number of Cell Towers')
# plt.xlabel('Area')
# plt.ylabel('Residuals')
# plt.show()


# correlations = []
# operators=['Airtel','Jio','Vodafone','All Operators']
# for operator in operators:
#     for radio in ['3G', '4G', '5G']:
#         file_name = f'../{radio}_Metrics/{radio}_{operator}.csv' if operator != 'All Operators' else f'./{radio}_Metrics/{radio}.csv'
#         df = pd.read_csv(file_name)
#         metric_column_map = {
#             'Area': 'Area_total',
#             'Population Density': 'population density_total',
#             'Household density': 'Household density',
#             '% Rural Population': '% Rural Population',
#             '% Rural Households': '% Rural Households',
#             '% Rural Area': '% Rural Area'
#         }
#         for metric, column in metric_column_map.items():
#             if metric=='Population Density':
#                 correlation_value = df[column].corr(df['cell_towers_per_area'])
#                 y_col='cell_towers_per_area'
#             else:
#                 correlation_value = df[column].corr(df['number_of_cell_towers'])
#                 y_col='number_of_cell_towers'
#             correlation_value = f"{correlation_value:.3f}"

#             sns.regplot(x=df[column], y=df[y_col], data=df, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
#             plt.title(f'Scatter Plot of {metric} vs Number of Cell Towers')
#             plt.xlabel(f'{metric}')
#             plt.ylabel('Number of Cell Towers' if metric != 'Population Density' else 'Cell Towers per Area')
#             plt.savefig(f'../static/plots/{operator}/{radio}/{metric}/{correlation_value}.png')
#             plt.close()
            # correlations.append({
            #         'metric': metric,
            #         'operator': operator,
            #         'radio': radio,
            #         'correlation': correlation_value,
            #         'plot_link': f'/plot/{operator}/{radio}/{metric}/{correlation_value}'
            #     })






