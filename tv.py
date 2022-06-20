import numpy as np
import plotly.express as px
import pandas
import csv

def plotFigure(data_path):
    with open(data_path) as c_file:
        df = csv.DictReader(c_file)
        fig=px.scatter(df, x="Size of TV", y="Average time spent watching TV in a week (hours)")
        fig.show()

def getDataSource(data_path):
    tvSize=[]
    TimeSpent=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            tvSize.append(float(row["Size of TV"]))
            TimeSpent.append(float(row["Average time spent watching TV in a week (hours)"]))
    return{"x":tvSize, "y":TimeSpent}
    
def findCorrelation(datasource):
    c=np.corrcoef(datasource["x"], datasource["y"])
    print(f"Correlation Is :{c[0,1]} ")

def setup():
    dp="Size of TV,_Average time spent watching TV in a week (hours).csv"
    ds=getDataSource(dp)
    findCorrelation(ds)
    plotFigure(dp)

setup()

#Tv Size and Hours watched are not correlated, as the value is -0.21596489617950243