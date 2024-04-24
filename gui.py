import subprocess
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

retail_store_data = pd.read_csv(r'/media/kumar/HDD1/INFIDATA/INFIDATA PROJECTS/OCT-DEC RBITS PROJECTS/29 [REVA] RETAIL STORE DATA ANALYTICS/merged_data.csv')

# Specify the desired column order
desired_columns_order = ['product_name',
    'JAN_23_quantity', 'JAN_23_amount',
    'FEB_23_quantity', 'FEB_23_amount',
    'MAR_23_quantity', 'MAR_23_amount',
    'APRIL_23_quantity', 'APRIL_23_amount',
    'MAY_23_quantity', 'MAY_23_amount',
    'JUNE_23_quantity', 'JUNE_23_amount',
    'JULY_23_quantity', 'JULY_23_amount',
    'AUG_23_quantity', 'AUG_23_amount',
    'SEP_23_quantity', 'SEP_23_amount',
    'OCT_23_quantity', 'OCT_23_amount',
    'NOV_23_quantity', 'NOV_23_amount',
    'DEC_23_quantity', 'DEC_23_amount',
    'JAN_24_quantity', 'JAN_24_amount'  # Assuming you want JAN_24 columns at the end
]

retail_store_data = retail_store_data.reindex(columns=desired_columns_order)# Reindex the DataFrame columns
unique_product_list = retail_store_data['product_name'].unique()

st.title('RETAIL STORE DATA ANALYTICS')
with st.sidebar:
    section_name = option_menu("SELECT ONE OF THE FOLLOWING",
                               options=["ABOUT",'FORECAST'])

if section_name == 'ABOUT':
    st.info("project description will come here")

if section_name == 'FORECAST':
    st.subheader("DATA FILTRATION & FORECAST")
    product_name_user_input = st.selectbox("ENTER A PRODUCT NAME TO FETCH DATA",
                                           options=unique_product_list)

    data_filtration_submit_button = st.button("FETCH DATA")

    st.markdown('---')
    if data_filtration_submit_button:
        if product_name_user_input:
            filter = retail_store_data['product_name'] == product_name_user_input.upper()
            filtered_data = retail_store_data[filter]

            # st.subheader(f"HISTORICAL DATA FOR {product_name_user_input}")
            # st.dataframe(filtered_data.T,width=600)

            start_month = filtered_data.columns[1].replace('_quantity','')
            end_month = filtered_data.columns[-2].replace('_quantity','')

            st.subheader(f"DATA OF {product_name_user_input} SALES FROM {start_month} TO {end_month}")
            quantity_columns = [col for col in filtered_data.columns if '_quantity' in col]
            filtered_data_quantity = filtered_data[quantity_columns].T
            st.dataframe(filtered_data_quantity, width=600)


            fig = go.Figure()
            for column in filtered_data_quantity.columns:
                fig.add_trace(go.Scatter(x=filtered_data_quantity.index, y=filtered_data_quantity[column], mode='lines', name=column))

            # Customize layout
            fig.update_layout(
                title=f"PLOT OF {product_name_user_input} SALES FROM {start_month} TO {end_month}",
                xaxis_title="MONTH",
                yaxis_title="QUANTITY SOLD",
                hovermode="x",
            )

            st.plotly_chart(fig)


        st.subheader("DATA FORECAST")
        st.warning('data forecast will come here')

    else:
        st.error("CLICK SUBMIT BUTTON!")