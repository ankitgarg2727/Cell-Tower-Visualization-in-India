from flask import Flask, render_template,request,send_from_directory,jsonify
import pandas as pd
import json
import matplotlib
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('Agg')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/subdistricts')
def subdistricts():
    filename="INDIAN_SUB_DISTRICTS.geojson"
    return render_template('subdistricts.html',filename=filename)
@app.route('/Data/<path:filename>')
def serve_geojson(filename):
    return send_from_directory('Data', filename)


@app.route('/towers',methods=['POST'])
def towers():
    if request.method == 'POST':
        radio=request.form['tower']
    
    if radio=='3G':
        file_name='./delhitowers/3G.geojson'
    elif radio=='4G':
        file_name='./delhitowers/4G.geojson'

    df=gpd.read_file(file_name)
    points = []
    for idx, row in df.iterrows():
        points.append({
            'lat': row.geometry.y,
            'lng': row.geometry.x,
        })
    return render_template('towers.html',points=points)

@app.route('/cdf',methods=['POST'])
def cdf():
    if request.method == 'POST':
        tower=request.form['tower']
        road=request.form['road']
    if tower=="3G" and road=="highway":
        path='./static/3G_highway_cdf.html'   
    elif tower=="3G" and road=="residential":
        path='./static/3G_residential_cdf.html' 
    elif tower=="3G" and road=="combined":
        path='./static/3G_combined_cdf.html' 
    elif tower=="4G" and road=="highway":
        path='./static/4G_highway_cdf.html' 
    elif tower=="4G" and road=="residential":
        path='./static/4G_residential_cdf.html' 
    elif tower=="4G" and road=="combined":
        path='./static/4G_combined_cdf.html' 
                         
    return render_template('cdf.html',path=path)

@app.route('/grid')
def grid():
    correlations = []
    road_types = ['Highways', 'Residential', 'Residential and Highways']
    file_paths = [
        './Data/3G_highway_presence.csv',
        './Data/3G_residential_presence.csv',
        './Data/3G_combined_presence.csv',
        './Data/4G_highway_presence.csv',
        './Data/4G_residential_presence.csv',
        './Data/4G_combined_presence.csv'
    ]
    for i, file in enumerate(file_paths):
        df = pd.read_csv(file)
        correlation_value = df['highway_present'].corr(df['cell_tower_present'])
        correlation_value = f"{correlation_value:.3f}"
        tower_type = "3G" if i < 3 else "4G"
        road_type = road_types[i % 3]
        # sns.regplot(x=df['highway_present'], y=df['cell_tower_present'], data=df, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
        # plt.title(f'Scatter Plot of {tower_type} vs Cell {road_type}')
        # plt.xlabel(f'{tower_type}')
        # plt.ylabel(f'{road_type}')
        # plt.savefig(f'static/plots/{tower_type}_{road_type}_{correlation_value}.png')
        # plt.close()
        correlations.append({
            'tower': tower_type,
            'road': road_type,
            'correlation':correlation_value,
            'plot_link': f'/plots/{tower_type}/{road_type}/{correlation_value}'
        })
    return render_template('grid_table.html', correlations=correlations)

@app.route('/plots/<tower_type>/<road_type>/<correlation_value>')
def show_plot2(tower_type, road_type,correlation_value):
    plot_path = f'static/plots/{tower_type}_{road_type}_{correlation_value}.png'
    return render_template('metrics.html', plot_path=f'/{plot_path}',correlation=correlation_value)


@app.route('/cdf1')
def grid1(): 
    corr_df=pd.read_csv("./Data/3G_highway_presence.csv")
    correlation_value = corr_df['highway_present'].corr(corr_df['cell_tower_present'])
    correlation_value = f"{correlation_value:.3f}"
    plotpath='./static/3G_highways.html'
    return render_template('grid_analysis.html', correlation_value=correlation_value,plotpath=plotpath)


@app.route('/cdf2')
def grid2(): 
    corr_df=pd.read_csv("./Data/4G_highway_presence.csv")
    correlation_value = corr_df['highway_present'].corr(corr_df['cell_tower_present'])
    correlation_value = f"{correlation_value:.3f}"
    plotpath='./static/4G_highways.html'
    return render_template('grid_analysis.html', correlation_value=correlation_value,plotpath=plotpath)


@app.route('/filter',methods=['POST'])
def filter():
    if request.method == 'POST':
        operator=request.form['operator']
        radio=request.form['radio']
    file_name = None
    if operator == 'all_operators' and radio == "5g":
        file_name = './5G_CSV/india.csv'
    elif operator == 'airtel' and radio == "5g":
        file_name = './5G_CSV/Airtel.csv'
    elif operator == 'jio' and radio == "5g":
        file_name = './5G_CSV/Jio.csv'
    elif operator == 'vodafone' and radio == "5g":
        file_name = './5G_CSV/Vodafone.csv'
    elif operator == 'all_operators' and radio == "4g":
        file_name = './4G_CSV/updated_4G.csv'
    elif operator == 'airtel' and radio == "4g":
        file_name = './4G_CSV/4G_Airtel.csv'
    elif operator == 'jio' and radio == "4g":
        file_name = './4G_CSV/4G_Jio.csv'
    elif operator == 'vodafone' and radio == "4g":
        file_name = './4G_CSV/4G_Vodafone.csv'
    elif operator == 'all_operators' and radio == "3g":
        file_name = './3G_CSV/updated_3G.csv'
    elif operator == 'airtel' and radio == "3g":
        file_name = './3G_CSV/3G_Airtel.csv'
    elif operator == 'jio' and radio == "3g":
        file_name = './3G_CSV/3G_Jio.csv'
    elif operator == 'vodafone' and radio == "3g":
        file_name = './3G_CSV/3G_Vodafone.csv'
    data = pd.read_csv(file_name)
    data = data.dropna(subset=['operator'])
    if radio == "5g":
        data = data.fillna('')  
        points = data[['lat', 'long', 'city_name', 'operator']].to_dict(orient='records')
    else:
        data = data.fillna('')  
        points = data[['lat', 'long', 'mcc', 'mnc', 'operator']].to_dict(orient='records')
    
    return render_template('map.html', points=points)

@app.route('/filter2',methods=['POST'])
def filter2():
    if request.method == 'POST':
        operator=request.form['operator2']
        radio=request.form['radio2']
    file_name = None
    if operator == 'all_operators' and radio == "5g":
        file_name = './5G_Number_of_cell_towers_geojson/5G.geojson'
    elif operator == 'airtel' and radio == "5g":
        file_name = './5G_Number_of_cell_towers_geojson/5G_Airtel.geojson'
    elif operator == 'jio' and radio == "5g":
        file_name = './5G_Number_of_cell_towers_geojson/5G_Jio.geojson'
    elif operator == 'vodafone' and radio == "5g":
        file_name = './5G_Number_of_cell_towers_geojson/5G_Vodafone.geojson'
    elif operator == 'all_operators' and radio == "4g":
        file_name = './4G_Number_of_cell_towers_geojson/4G.geojson'
    elif operator == 'airtel' and radio == "4g":
        file_name = './4G_Number_of_cell_towers_geojson/4G_Airtel.geojson'
    elif operator == 'jio' and radio == "4g":
        file_name = './4G_Number_of_cell_towers_geojson/4G_Jio.geojson'
    elif operator == 'vodafone' and radio == "4g":
        file_name = './4G_Number_of_cell_towers_geojson/4G_Vodafone.geojson'
    elif operator == 'all_operators' and radio == "3g":
        file_name = './3G_Number_of_cell_towers_geojson/3G.geojson'
    elif operator == 'airtel' and radio == "3g":
        file_name = './3G_Number_of_cell_towers_geojson/3G_Airtel.geojson'
    elif operator == 'jio' and radio == "3g":
        file_name = './3G_Number_of_cell_towers_geojson/3G_Jio.geojson'
    elif operator == 'vodafone' and radio == "3g":
        file_name = './3G_Number_of_cell_towers_geojson/3G_Vodafone.geojson'
    with open(file_name, 'r') as f:
        geojson_data = json.load(f)
    return render_template('map2.html', geojson_data=json.dumps(geojson_data))


    
@app.route('/correlation_tables')
def correlation_tables():
    correlations = []
    operators=['Airtel','Jio','Vodafone','All Operators']
    for operator in operators:
        for radio in ['3G', '4G', '5G']:
            file_name = f'./{radio}_Metrics/{radio}_{operator}.csv' if operator != 'All Operators' else f'./{radio}_Metrics/{radio}.csv'
            df = pd.read_csv(file_name)
            metric_column_map = {
                'Area': 'Area_total',
                'Population Density': 'population density_total',
                'Household density': 'Household density',
                '% Rural Population Density': '% Rural_pop_per_area'   ,
                '% Rural Households Density': '% Rural_house_per_area',
                '% Rural Area': '% Rural Area'
            }
            for metric, column in metric_column_map.items():
                if metric=='Area' or metric=="% Rural Area":
                    correlation_value = df[column].corr(df['number_of_cell_towers'])
                    y_col='number_of_cell_towers'
                else:
                    correlation_value = df[column].corr(df['cell_towers_per_area'])
                    y_col='cell_towers_per_area'
                correlation_value = f"{correlation_value:.3f}"

                # sns.regplot(x=df[column], y=df[y_col], data=df, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
                # plt.title(f'Scatter Plot of {metric} vs Cell Towers per Area' if (metric != 'Area' and metric!='% Rural Area')  else f'Scatter Plot of {metric} vs Number of Cell Towers')
                # plt.xlabel(f'{metric}')
                # plt.ylabel('Cell Towers per Area' if (metric != 'Area' and metric!='% Rural Area') else 'Number of Cell Towers')
                # plt.savefig(f'static/plots/{operator}_{radio}_{metric}_{correlation_value}.png')
                # plt.close()
                correlations.append({
                    'metric': metric,
                    'operator': operator,
                    'radio': radio,
                    'correlation': correlation_value,
                    'plot_link': f'/plots/{operator}/{radio}/{metric}/{correlation_value}'
                })
    for operator in operators:
        for radio in ['3G', '4G', '5G']:
            file_name = f'./{radio}_Income/{radio}_{operator}.csv' if operator != 'All Operators' else f'./{radio}_Income/{radio}.csv'
            df = pd.read_csv(file_name)
            metric_column_map = {
                'Household Income Annual per Area' : 'income_per_area'
            }
            for metric, column in metric_column_map.items():
                correlation_value = df[column].corr(df['cell_towers_per_area'])
                correlation_value = f"{correlation_value:.3f}"
                # sns.regplot(x=df[column], y=df['cell_towers_per_area'], data=df, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
                # plt.title(f'Scatter Plot of {metric} vs Cell Towers per Area' )
                # plt.xlabel(f'{metric}')
                # plt.ylabel('Cell Towers per Area')
                # plt.savefig(f'static/plots/{operator}_{radio}_{metric}_{correlation_value}.png')
                # plt.close()
                correlations.append({
                    'metric': metric,
                    'operator': operator,
                    'radio': radio,
                    'correlation': correlation_value,
                    'plot_link': f'/plots/{operator}/{radio}/{metric}/{correlation_value}'
                })            
    grouped_correlations = {}
    for row in correlations:
        metric = row['metric']
        radio = row['radio']
        
        if metric not in grouped_correlations:
            grouped_correlations[metric] = {}
        
        if radio not in grouped_correlations[metric]:
            grouped_correlations[metric][radio] = []
        
        grouped_correlations[metric][radio].append(row)            
    return render_template('correlation_tables.html', grouped_correlations=grouped_correlations)

@app.route('/plots/<operator>/<radio>/<metric>/<correlation_value>')
def show_plot(operator, radio, metric,correlation_value):
    plot_path = f'static/plots/{operator}_{radio}_{metric}_{correlation_value}.png'
    return render_template('metrics.html', plot_path=f'/{plot_path}',correlation=correlation_value)


if __name__ == "__main__":
    app.run(debug=True,port=8080)

