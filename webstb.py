import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit_echarts,os
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
#https://pythonwebstb.streamlit.app/
st.set_page_config(page_title="飞哥数据分析测试平台", layout="wide")



if os.path.exists('展示数据.csv'):
    df1 = pd.read_csv('展示数据.csv', encoding="utf-8")
    column = df1.columns  #获取表头
    df = pd.DataFrame(df1,columns=column)
    
    option_x = st.sidebar.selectbox("选择要用作x轴的数据列", options=column)
    
    对比对象 = df.set_index(option_x)
    countries = st.multiselect(
        "选择对比对象", list(对比对象.index), []
    )
    print(countries)
    countries2 = st.multiselect(
        "选择对比数据", list(column), []
    )
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(countries2)
        .set_global_opts(title_opts=opts.TitleOpts(title="柱状图", subtitle="副标题"))
    )
    
    for 主播 in countries:
        对比数据 = []
        for cow in countries2:
            对比数据.append(int(对比对象.loc[主播][cow]))
        bar.add_yaxis(主播, 对比数据)
    # 在Streamlit应用程序中显示图表 
    streamlit_echarts.st_pyecharts(bar)
    
else:
    st.title('暂无数据表展示')