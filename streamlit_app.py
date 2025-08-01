import streamlit as st
from dotenv import load_dotenv
import os
import psycopg
import pandas as pd

load_dotenv()

st.title("Hello World")
st.badge("Home", color="violet")

def getData():
    dbconn = os.getenv("DBCONN")
    conn = psycopg.connect(dbconn)
    cur = conn.cursor()
    
    query = '''
        SELECT * FROM weather_data;
    '''
    
    cur.execute(query)
    data = cur.fetchall()
    # df = pd.DataFrame(data, columns=["date", "city", "temp", "feels", "description"])
    return data
    
data = getData()
value = st.selectbox("Select a city", ["Berlin", "Sydney", "Tokyo"])
print(value)
filtered = [x for x in data if x[1] == value]
print(filtered)
df = pd.DataFrame(filtered, columns=["date", "city", "temp", "feels", "description"])
st.dataframe(df)