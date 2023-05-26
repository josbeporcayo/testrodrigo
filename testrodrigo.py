#%%
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from config import postuser,postpassword,postipaddress,postport,database
#%%
postengine=create_engine(f'postgresql+psycopg2://{postuser}:{postpassword}@{postipaddress}:{postport}/{database}')
#%%
query='''SELECT * 
        FROM yearlysales'''
test2=pd.read_sql(query,postengine,parse_dates=['Order Date'])
test2
#%%[markdown]
# $\sigma_{i}$
# %%
