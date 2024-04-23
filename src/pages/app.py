
import pandas as pd
import streamlit as st

# Load the data
excel_file = 'path_to_your_file.xlsx'
sheet_to_df_map = pd.read_excel(excel_file, sheet_name=None)