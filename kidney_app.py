import streamlit as st
import os
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import altair as alt
#from pandas.plotting import scatter_matrix
import plotly.express as px
#from PIL import Image
#import base64
from sklearn.manifold import TSNE
from utils import *

#st.set_page_config(layout='wide')


st.image('./variationred.png')


@st.cache
def read_data():
    df=pd.read_csv('Kidney_Q3Norm_TargetCountMatrix.csv')
    df2=pd.read_csv('Kidney_Sample_Annotations.csv')
    return df,df2
df,df2=read_data()


scan = st.sidebar.checkbox('by scan')
genes = st.sidebar.checkbox('by genes')

if (genes==False and scan==False):
    
    st.header('Presentation')
    '''
    Diabetic Kidney desease is an affection that quenches kidney function and affects people with diabates.
    The causes of diabetic kidney disease are diverse and complex and gene expression is used to understand this problem.

    This web app allows to see the data provided for the Hackaton. There are two main approaches which 
    you can test by cliking the two options at the side bar.
    For both cases, gene expression by glomeruli, proximal and distal tubules is used.
    '''
    st.image('https://upload.wikimedia.org/wikipedia/commons/0/02/Gray1128.png')
    st.write('By Henry Vandyke Carter - Henry Gray (1918) Anatomy of the Human Body (See &quot;Book&quot; section below)Bartleby.com: Gray&#039;s Anatomy, Plate 1128, Public Domain, https://commons.wikimedia.org/w/index.php?curid=567094')

    
    with st.sidebar.beta_expander("Credits"):
        """
        Although minimalist, this app is the result of weeks of work by:
        - [José Manuel Nápoles] (https://github.com/napoles-uach)
        
        The full code is provided as open source on github. 
        
            """
        st.image('https://avatars.githubusercontent.com/u/30182239?v=4')
        

if genes:

    df_=df.drop('TargetName',1)
    dft=df_.T

    genco1,genco2 = st.beta_columns([1,1])
    with genco1:
        ts=st.checkbox('t-SNE')
    with genco2:
        gi=st.checkbox('gene importance')
    
    if ts:
        xx,yy,cla,nam=tsne_genes(dft,df2)
        fig = px.scatter(x=xx,y=yy,color=cla,hover_name=nam)
        st.plotly_chart(fig)

    names_list=dft.index.to_list()



#---------------------------
    genes=df
    genes_list=genes.TargetName
    #names_list=dft.index.to_list()


    if gi:
        with st.beta_expander("See explanation"):
            st.write("""
            Here we evaluate a measurement of gene expression anomalies
            """)
            st.image('./variation.png')
        tipo_cel = st.selectbox('type',['Geometric Segment','PanCK','neg'])
        var_list_normal=var(tipo_cel,'normal',names_list)
        var_list_disease=var(tipo_cel,'disease',names_list)

        total=[]
        for i in range(len(var_list_normal)):
            total.append(np.log10(var_list_disease[i]/var_list_normal[i]))

        total_df=pd.Series(total, index=genes_list)
        total_df=total_df.sort_values(ascending=False)

        fig = px.bar(total_df[:20],x=total_df.index[:20], y=total_df.values[:20])
        fig.update_layout(xaxis=dict(title='Genes'),
        yaxis=dict(title='log(var. disease/var. normal)')
        )
        st.plotly_chart(fig)

    #st.write(total_df[:50].index.tolist())

        gen=st.selectbox('Select gene',total_df[:20].index.tolist())



        lista=get_gen(gen,tipo_cel,'disease',names_list,total_df,df)
    #fig = px.bar(total_df[:50],x=total_df.index[:50], y=total_df.values[:50])

        fig = px.bar(lista[:20],x=lista.index[:20], y=lista.values[:20])
        fig.update_layout(xaxis=dict(title=''),
        yaxis=dict(title='Normalized Expression')
        )
        st.plotly_chart(fig)




if scan:

    caso=st.sidebar.radio('case',('disease1B_scan','disease2B_scan','disease3_scan','disease4_scan','normal2B_scan','normal3_scan','normal4_scan'))
    plot_roi=st.sidebar.checkbox('ROI')

    col1,col2,col3 =st.sidebar.beta_columns(3)




    with col1:
    #pics=st.radio('  ',('no','yes'))
        plot_dot=st.checkbox('Cosine Matrix')

    with col2:
    #pair_target = st.radio(' ',('no','yes'))
        pair_target = st.checkbox('Pair Targets')


    with col3:
    #pics=st.radio('  ',('no','yes'))
        pics = st.checkbox('Pictures')





    normal=df2[df2['ScanName']==caso]
    groups=normal['SegmentDisplayName']
    groups_list=groups.to_list()
    hist=df[groups_list]
    hist=hist.describe()
    row1 = hist.iloc[1]
    normal['mean']=row1.values #average of all genes expression

#-------------producto punto

    if plot_dot:
       dot_mat(groups_list,df)


#---------------------ROI-------------------------------
    
    if plot_roi:
       ROI(caso,normal)


#---------------------Pair Targets ----------------------

    if pair_target:
      target(normal,df)


#----------------------- columnas con imagenes -----------------
    directory = r'./ROI reports/'+caso+'/'
    listdir=[]
    for filename in os.listdir(directory):
       if filename.endswith('.png'):
           listdir.append(filename)

    if pics:
       columnas_imagenes(listdir,directory)



