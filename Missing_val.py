import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
import requests
import re
import numpy as np
import pandas as pd
pd.options.display.max_rows=999
pd.options.display.max_columns=999
from bs4 import BeautifulSoup
plt.rcParams['axes.unicode_minus'] = False


# 출처: 위키피디아 - 중앙선거여론조사심의위원회

source_url = "https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EB%8C%80%ED%86%B5%EB%A0%B9_%EC%A7%80%EC%A7%80%EC%9C%A8"
req = requests.get(source_url)
html = req.content
soup = BeautifulSoup(html,'lxml')
contents_table = soup.find(name="table", attrs={"class":"wikitable"} )
table_body = contents_table.find(name="tbody")
table_data = pd.DataFrame(table_body.text.replace("\n", " ").split("  "))
table_data = table_data.drop(table_data.index[0:300]).reset_index(drop=True)


# 결측값 : NaN = 미조사
print(table_data[table_data[0].str.match(pat="미조사")==True])
table_data[table_data[0].str.match(pat="미조사")==True] = np.nan


#missing_part graph!
#!pip install missingno
import missingno as msno

msno.matrix(table_data)
