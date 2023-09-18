import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit_echarts
from pyecharts import options as opts
from pyecharts.charts import Bar
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
import subprocess

st.set_page_config(page_title="飞哥数据分析测试平台", layout="wide")
file = st.sidebar.file_uploader("请上传csv表格", type=["csv"])


def 柱状对比图(df,x):
    对比对象 = df.set_index(x)
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
    return bar

def 柱状图(option_x,option_y):
    bar_chart = px.bar(df, x=option_x, y=option_y)
    bar_chart.update_layout(title='柱状图', xaxis_title=option_x, yaxis_title=option_y)
    # 显示图表
    st.plotly_chart(bar_chart)
    
    
def 保存图表(html):
    html.render()
    print('保存成功')
if file is not None:
    df1 = pd.read_csv(file, encoding="utf-8")
    column = df1.columns  #获取表头
    df = pd.DataFrame(df1,columns=column)
    option_x = st.sidebar.selectbox("选择要用作x轴的数据列", options=column)
    option_y = st.sidebar.selectbox("选择要用作y轴的数据列", options=column)
    
    html = 柱状对比图(df,option_x)
    if st.button("保存对比图"):
       保存图表(html)
    
    柱状图(option_x,option_y)
    
    
    
    # 显示表格
    st.dataframe(df)

def 关闭():
    st.stop()
