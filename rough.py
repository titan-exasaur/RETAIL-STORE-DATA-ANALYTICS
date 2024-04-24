import subprocess
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu

retail_store_data = pd.read_csv(r'/media/kumar/HDD1/INFIDATA/INFIDATA PROJECTS/OCT-DEC RBITS PROJECTS/29 [REVA] RETAIL STORE DATA ANALYTICS/merged_data.csv')
print(retail_store_data.columns)