import pandas as pd
import plotly_express as px

filename=input("Enter file name: ")
independent=input("Independant variable")
dependent=input("dependant variable")
control=input("Enter name of controlling variable: ")
title1=input("title")
type=input("Enter type of Graph: ").lower()
df=pd.read_csv(filename)

if type=="line":
    fig=px.line(df, x=independent,y=dependent,color=control,title=title1)
    fig.show()

elif type=="bar":
    fig=px.bar(df, x=independent,y=dependent,color=control,title=title1)
    fig.show()

else:
    print("Please choose from line or bar")