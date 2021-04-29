import streamlit as st
import plotly.express as px
import base64
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.manifold import TSNE


def get_gen(gen,tipo,diagnostico,names_list,total_df,df):
    st.write('Where is gen ',gen, 'more expressed? 👇')
    substring=tipo
    res = [i for i in names_list if substring in i]
    substring=diagnostico
    res = [i for i in res if substring in i]
    res.append('TargetName')

        

    lista=df.loc[df['TargetName'] == gen]
    lista=lista.T
    lista=lista.iloc[:,0]
        
    lista=lista[1:].sort_values(ascending=False)
    #st.write(lista)
    return lista

def var(tipo,diagnostico,names_list):
    substring=tipo
    res = [i for i in names_list if substring in i]
    substring=diagnostico
    res = [i for i in res if substring in i]
    df=pd.read_csv('Kidney_Q3Norm_TargetCountMatrix.csv')
    df=df[res]
    df=df.T
    var_list=df[:].var()
    return var_list


def tsne_genes(dft,df2):
    exag = 10# st.sidebar.slider('early_exaggeration', 1, 50, 10)
    tsne = TSNE(random_state=42,early_exaggeration=exag)
    digits_tsne = tsne.fit_transform(dft)
    #names=pd.read_csv('Kidney_Sample_Annotations.csv')
    names_list=dft.index.to_list()
    Slide_list=df2['SlideName'].to_list()
    Segmen_list=df2['SegmentDisplayName'].to_list()
    clase=[]
    for name in names_list:
        i=Segmen_list.index(name)
        clase.append(Slide_list[i])
    
    selectbox=st.multiselect('pick one',['disease3','normal3','disease4','normal4','disease2B','normal2B','disease1B'],default=['disease3','normal3','disease4','normal4','disease2B','normal2B','disease1B'])

    if selectbox:

        indices=[]
        for i in range(len(clase)):
          for nombre in selectbox:
            if clase[i]==nombre:
              indices.append(i)

    #fig = px.scatter(x=digits_tsne[:,0],y=digits_tsne[:,1],color=clase,hover_name=names_list)

        fig = px.scatter(x=digits_tsne[indices[0]:indices[-1],0],y=digits_tsne[indices[0]:indices[-1],1],color=clase[indices[0]:indices[-1]],hover_name=names_list[indices[0]:indices[-1]])
        st.plotly_chart(fig)



def dot_mat(groups_list,df):
    subs='PanCK'
    res1 = list(filter(lambda x: subs in x, groups_list))

    subs='neg'
    res2 = list(filter(lambda x: subs in x, groups_list))

    subs='Geometric Segment'
    res3 = list(filter(lambda x: subs in x, groups_list))

    groups_list2=[]
    groups_list2=res1+res2+res3

    groups_list=groups_list2
    df_=df[groups_list]
    i=-1
    j=-1
    mat=np.zeros((int(len(groups_list)),int(len(groups_list))))
    for element1 in groups_list:
      j+=1
      i=-1
      for element2 in groups_list:
       i+=1
       vec1=np.array(df_[element1])
       vec2=np.array(df_[element2])
       v1=np.linalg.norm(vec1)
       v2=np.linalg.norm(vec2)
       mat[i][j]=np.dot(vec1,vec2)/(v1 * v2)

    mat_df = pd.DataFrame(mat, columns = groups_list,index =groups_list)
    fig3 = px.imshow(mat_df**2, )
    fig3.update_layout(height=685,)


    st.header('Cosine similarity matrix for genetic expression')
    st.latex(r'''\cos{ \theta } = \frac{\vec{U} \cdot \vec{V}}{||\vec{U}|| ||\vec{U}||}''')

    st.plotly_chart(fig3)

def columnas_imagenes(listdir,directory):
    #directory = r'./ROI reports/'+caso+'/'
    images=st.sidebar.multiselect('Choose Pictures', listdir) # lista con selección de imagenes
    if images:
        len_images=len(images)
        for iname in range(len_images):
            st.sidebar.write(images[int(iname)])
            st.sidebar.image(directory+images[int(iname)],width=300)


def target(normal,df):
    cols_names = list(normal['SegmentDisplayName'])
    colname=st.multiselect('Pair Targets', cols_names) # widget ---> 'Pair Tagets'
    #st.write(colname[1][10])
    res = {colname[x] : x for x in range(len(colname))}
    #st.write(res)
    fig2 = px.scatter_matrix(df[colname],hover_name=df['TargetName'])
    #fig2.update_layout(xaxis=dict(title=))
    #fig2.update_xaxes(automargin=True,overlaying='free',title=res)
    fig2.update_layout(
                width=800,
                height=1000,)
    st.plotly_chart(fig2)    






def ROI(caso,normal):
    

    image_filename = './ROI reports/'+caso+'/output.jpg'
    image = Image.open(image_filename)
    width, height = image.size
    back_im = base64.b64encode(open(image_filename, 'rb').read())
    fig=px.scatter(normal, x='ROICoordinateX', y='ROICoordinateY',color="SegmentLabel",
          hover_name='SegmentDisplayName',
          size='mean',range_x=[0,40000], range_y=[-40000,0])
    img_width = width
    img_height = height
    scale_factor = 60

    fig.update_xaxes(
    #visible=False,
    range=[0, img_width * scale_factor]
    )

    fig.update_yaxes(
    #visible=False,
    range=[-img_height * scale_factor,0],#[0, img_height * scale_factor],
    # the scaleanchor attribute ensures that the aspect ratio stays constant
    scaleanchor="x"
    )
    
    
    if caso == 'disease1B_scan':
        x_= 6500
        y_ = 4500
    elif caso == 'disease2B_scan':
        x_= 6500
        y_ = 2500
    elif caso == 'disease3_scan':
        x_= 6500
        y_ = 4500
    elif caso == 'disease4_scan':
        scale_factor = 56
        x_= 8000
        y_ = 4000
        #x_=st.slider('x-',-10000,10000,1000,step=500) 
        #y_=st.slider('y-',-10000,10000,1000,step=500)  

    elif caso == 'normal2B_scan':
        #scale_factor = 60
        x_= 6500
        y_ = 3500

    elif caso == 'normal3_scan':
        scale_factor = 51
        x_= 1000
        y_ = -500

    else :
        x_= 6500
        y_ = 3500  
        #scale_factor = 60
   

    fig.add_layout_image(
    dict(
        x=x_,#6500,
        sizex=img_width * scale_factor,
        y=-1*y_,#-4600,#img_height * scale_factor,
        sizey=img_height * scale_factor,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        #sizing="stretch",
         
        source='data:image/png;base64,{}'.format(back_im.decode()),)
    )


    # Configure other layout
    fig.update_layout(
        width=800,#img_width * scale_factor/40,
        height=800,#img_height * scale_factor/80,
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
    )
    






 
    st.plotly_chart(fig)