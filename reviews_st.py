import streamlit as st
import pandas as pd
from annotated_text import annotated_text
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('logo.png')
st.set_page_config(page_title="App Reviews Analyzer", page_icon=img)

header = st.container()
test = st.container()
#graphs = st.container()

add_selectbox = st.sidebar


with add_selectbox:
    st.title("Aidetic App Analyzer")
    st.write('**Choose an App**')
    app_choice = st.selectbox(label = "The reviews of the following apps from play store have been analyzed",options = ("HDFC PayZapp", "NPCI Bhim", "Zest Money"),help = "choose the app you want")
    st.write('**Choose Themes**')
    theme_choice = st.radio(label = "Positive Themes represents ideas/themes people like about the app",options = ['Positive Themes','Negative Themes','All Themes'])
    #st.write("**Compare Reviews**")
    #st.radio(label = "Do you want to compare reviews",options = ['Yes','No'])
    #options = st.multiselect(
    # 'Select Apps to Compare',
    # ['HDFC PayZapp', 'NPCI Bhim', 'Zest Pay'],
    # ['HDFC PayZapp'])

    #st.write('You selected:', options)


with header:
    st.title(app_choice)

    if app_choice == "HDFC PayZapp":
        v = {0:"3.9",1:"434 K",2: "10 M+"}
    
    if app_choice == "NPCI Bhim":
        v = {0:"4.6",1:"1.21 M",2:"50 M+"}
    
    if app_choice == "Zest Money":
        v = {0:"4.4",1:"167 K",2:"5 M+"}

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Rating out of 5", value=v[0])
    col2.metric(label="No of Ratings", value=v[1])
    col3.metric("Downloads", value = v[2])
    

#with graphs:

#    st.header("App Analytics")
    
#    import numpy as np

#    arr = np.random.normal(1, 1, size=100)
#    fig, ax = plt.subplots()
#    ax.hist(arr, bins=5)
#    plt.figure(figsize=(5,5)) 

#    st.pyplot(fig)
    
    
    #st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

with test:

    st.header("Themes")

# hdfc
    
    if (app_choice == "HDFC PayZapp") & (theme_choice == 'Negative Themes'):

        image = Image.open('hdfc_neg.png')
        st.image(image, caption='HDFC PayZapp Negative Reviews')

    elif (app_choice == "HDFC PayZapp") & (theme_choice == 'Positive Themes'):

        image = Image.open('hdfc_pos.png')
        st.image(image, caption='HDFC PayZapp Positive Reviews')
    
    elif (app_choice == "HDFC PayZapp") & (theme_choice == 'All Themes'):

        image = Image.open('hdfc_all.png')
        st.image(image, caption='HDFC PayZapp Reviews')


# zest
    
    elif (app_choice == "Zest Money") & (theme_choice == 'Negative Themes'):

        image = Image.open('zest_neg.png')
        st.image(image, caption='Zest Money Negative Reviews')

    elif (app_choice == "Zest Money") & (theme_choice == 'Positive Themes'):

        image = Image.open('zest_pos.png')
        st.image(image, caption='Zest Money Positive Reviews')
    
    elif (app_choice == "Zest Money") & (theme_choice == 'All Themes'):

        image = Image.open('zest_all.png')
        st.image(image, caption='Zest Money Reviews')


# bhim upi

    elif (app_choice == "NPCI Bhim") & (theme_choice == 'Negative Themes'):

        image = Image.open('bhim_neg.png')
        st.image(image, caption='NPCI Bhim Negative Reviews')

    elif (app_choice == "NPCI Bhim") & (theme_choice == 'Positive Themes'):

        image = Image.open('bhim_pos.png')
        st.image(image, caption='NPCI Bhim Positive Reviews')
    
    elif (app_choice == "NPCI Bhim") & (theme_choice == 'All Themes'):

        image = Image.open('bhim_all.png')
        st.image(image, caption='NPCI Bhim Reviews')
    

    else:

        image = Image.open('wip.jpg')
        st.image(image, caption='Under Construction')




    
    #annotated_text(
    #    ("annotated", "", "#faa"),
    #)
    #st.write(annotated_text)
    
 




