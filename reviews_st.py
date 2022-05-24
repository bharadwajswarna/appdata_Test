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
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Rating out of 5", value="4.2")
    col2.metric(label="No of Ratings", value="465,025")
    col3.metric("No of Reviews Analyzed", value = "125,000")
    

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
    
    if (app_choice == "HDFC PayZapp") & (theme_choice == 'Negative Themes'):

        image = Image.open('hdfc_neg.png')
        st.image(image, caption='HDFC PayZapp Negative Reviews')

    elif (app_choice == "HDFC PayZapp") & (theme_choice == 'Positive Themes'):

        image = Image.open('hdfc_pos.png')
        st.image(image, caption='HDFC PayZapp Positive Reviews')
    
    elif (app_choice == "HDFC PayZapp") & (theme_choice == 'All Themes'):

        image = Image.open('hdfc_neg.png')
        st.image(image, caption='HDFC PayZapp Negative Reviews')

        image = Image.open('hdfc_pos.png')
        st.image(image, caption='HDFC PayZapp Positive Reviews')
    

    else:

        image = Image.open('wip.jpg')
        st.image(image, caption='Under Construction')




    
    #annotated_text(
    #    ("annotated", "", "#faa"),
    #)
    #st.write(annotated_text)
    
 




