import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import os




def AIS2ESRI(ais: pd.DataFrame, outputFolder: str, Timeframe: list):
    """
    Funzione che esegue la conversione del messaggio AIS in shapefiles
    ais: Dataframe del messaggio ais
    outputFolder: cartella di output
    Timeframe: tempo inizio, tempo fine --> ['01/03/2022 01:00:00','01/03/2022 02:00:00']
    """

    style = 'symbol:pin; fill:#0000ff; fill-opacity:0.7; stroke:#ffffff; stroke-opacity:1.0; stroke-width:0.5'
    text = None
    dateTime = None

    ais.dropna(axis=0,subset=['Longitude','Latitude'], inplace=True)
    ais.reset_index(inplace=True, drop=True)

    ais = ais[ (ais['# Timestamp']>Timeframe[0]) & (ais['# Timestamp']<Timeframe[1])]
    ais.dropna(axis=0,subset=['Longitude','Latitude'], inplace=True)
    ais.reset_index(inplace=True, drop=True)

    SHP = gpd.GeoDataFrame(columns = ['style_css', 'label', 'text', 'dateTime', 'geometry'])
    ais.reset_index(inplace=True, drop=True)

    os.makedirs(outputFolder, exist_ok=True)
    output_path = outputFolder

    for i in range(len(ais)):
        label = ais['MMSI'][i]
        lat, lon = float(ais['Latitude'][i]), float(ais['Longitude'][i])
        # coordinates = [(lat, lon)]
        coordinates = [(lon, lat)]
        geometry = Point(coordinates)
        new_row = {'style_css':style, 'label':label, 'text':text, 'dateTime':dateTime, 'geometry':geometry}
        SHP = SHP.append(new_row, ignore_index=True)
    SHP.to_file(output_path+'\\'+'navi.shp')
    
    return SHP


def main():
     print('Executing main...')


if __name__ == '__main__':
     main()