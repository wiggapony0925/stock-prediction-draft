import pandas as pd 
import numpy as np
import streamlit as st 


df = pd.DataFrame(
        np.random.randn(50,20),
        colums = ('col %d' i for in range(20)))


st.dataframe(df)
