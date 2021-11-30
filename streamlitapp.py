import streamlit as st
import pandas as pd
import numpy as np
import pickle
from utils import *

st.write(
    """ 
# Overall Score Predictor 
"""
)

joined = st.number_input("Enter  joined:")
power_jumping = st.number_input("Enter  power_jumping:")
power_stamina = st.number_input("Enter  power_stamina:")
passing = st.number_input("Enter  passing:")
team_jersey_number = st.number_input("Enter the team_jersey_number:- ")
defending = st.number_input("Enter defending:-")
shooting = st.number_input("Enter shooting:-")
attacking_heading_accuracy = st.number_input(
    "Enter attacking_heading_accuracy:-")
height = st.number_input("Enter your height:")
age = st.sidebar.number_input("Enter your age:", 0, 100, 0)

if st.button("Predict"):
    results = predict(
        joined,
        power_jumping,
        power_stamina,
        passing,
        team_jersey_number,
        defending,
        shooting,
        attacking_heading_accuracy,
        height,
        age,
    )
    st.success(results)
