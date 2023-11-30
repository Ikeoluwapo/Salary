import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image

hide_streamlit_style = """ 
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

Salary = pd.read_csv("Salary_Data.csv") #Importation of data
HR1 = Image.open("HR1.jpg")
HR3 = Image.open("HR3.jpg")
HR4 = Image.open("HR4.jpg")
HR2 = Image.open("HR2.jpg")
st.image(HR2, width = 400)

st.title("Estimate your staffs salary based on their years of experience")
st.sidebar.write('"Happy employees makes happy customers"')
st.sidebar.image(HR3, width = 200)
st.sidebar.image(HR1, width = 200)
st.sidebar.image(HR4, width = 200)
#Split the data into dependent(y) and independent(x)
x = Salary.iloc[:, 0:-1].values
y = Salary.iloc[:, -1].values
#Split into Train and Test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 12)

#KNN seems to be the best model
from sklearn.neighbors import KNeighborsRegressor
model6 = KNeighborsRegressor(n_neighbors=11, weights='uniform', algorithm='auto',leaf_size=30,p=2,metric='minkowski')
model6.fit(x_train, y_train)

Years = float(st.number_input("Enter the years of experience"))
if st.button("Calculate"):
    y_predict6 = model6.predict([[Years]])
    st.write(f'The estimated salary = {round(y_predict6[0],2)}')

    st.text("'You are free to increase or reduce the salary from the estimate calculated'")















    








    


