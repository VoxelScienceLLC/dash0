import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

position = np.array([]);
pattern = "LogBlueprintUserMessages:"
file = open("FPPhysics_0621.log", "r")
for line in file:
    if re.search(pattern, line):
        position = np.append(position, 
        line.replace('LogBlueprintUserMessages:','').replace('\n',''))


TimePosition = np.array([" "])
for TimePosition in position:
  TimePosition = np.append(TimePosition, position)

ts = np.array([])
x = np.array([])
y = np.array([])
z = np.array([])
for t in TimePosition:
  ts = np.append(ts, str.split(t)[0].replace("[","").replace("]","")) #.replace("-",",")
  x = np.append(x, str.split(t)[2].replace("X=",""))
  y = np.append(y, str.split(t)[3].replace("Y=",""))
  z = np.append(z, str.split(t)[4].replace("Z=",""))  



df = pd.DataFrame({'Time':ts, 'X Position': x, 'Y Position': y, 'Z Position': z}) #Position data!

df["X Position"] = pd.to_numeric(df["X Position"], errors="coerce")
df["Y Position"] = pd.to_numeric(df["Y Position"], errors="coerce")
df["Z Position"] = pd.to_numeric(df["Z Position"], errors="coerce")
df = df.dropna().iloc[1:]


st.title("""Demo Dashboard for First Person Physics""")

col1, col2 = st.beta_columns([5,1])

# a = st.sidebar.radio('Table length:',["Full table","Early events only", "Late events only"])
b = st.sidebar.slider('How many rows of do you want to see?', min_value=10, max_value=len(df))
st.dataframe(df.iloc[1:b])


WhichPlot = st.sidebar.radio('Which 2D Plot:',["X v Y","X v Z", "Y v Z", "3D Scatter Plot"])

# if a=="Full table":
#     st.header('Full data')
#     st.dataframe(df)
# elif a=="Early events only":
#     st.header('Early events')
#     st.dataframe(df.head(10))
# else: 
#    st.header('Late events only')
#    st.dataframe(df.tail(10))

st.header("Visualization")
if WhichPlot == "X v Y":
    fig = px.scatter(df.drop_duplicates(['Time']).iloc[1:b], x="X Position", y="Y Position", color="Z Position")
    st.plotly_chart(fig)
elif WhichPlot == "X v Z":
    fig = px.scatter(df.drop_duplicates(['Time']).iloc[1:b], x="X Position", y="Z Position", color = "Z Position")
    st.plotly_chart(fig)
elif WhichPlot == "Y v Z"         :
    fig = px.scatter(df.drop_duplicates(['Time']).iloc[1:b], x="Y Position", y="Z Position")
    st.plotly_chart(fig)
else:
    fig = px.scatter_3d(df.drop_duplicates(['Time']).iloc[1:b], x="X Position", y="Y Position", z="Z Position",
    opacity = 0.7)
    st.plotly_chart(fig)    