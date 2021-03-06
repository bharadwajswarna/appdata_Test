import streamlit as st
import pandas as pd
from annotated_text import annotated_text
import matplotlib.pyplot as plt
from PIL import Image

def read_pkl(filename):
    import pickle
    file = open(filename,'rb')
    df = pickle.load(file)
    file.close()
    return df

img = Image.open('logo.png')
st.set_page_config(page_title="App Reviews Analyzer", page_icon=img)

header = st.container()
test = st.container()
#graphs = st.container()

add_selectbox = st.sidebar


with add_selectbox:
    st.title("Aidetic App Analyzer")
    st.write('**Choose an App**')
    app_choice = st.selectbox(label = "The reviews of the following apps from play store have been analyzed",options = ("HDFC PayZapp", "NPCI Bhim", "Zest Money",
                                        "PhonePe Business","GooglePay Business","Kredit Bee", "Lending Kart", "CASHe", "Khata Book", "Vyapaar", "Slice"),
                                        help = "choose the app you want")
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

    if app_choice == "GooglePay Business":
        v = {0:"4.5",1:"190 K",2: "10 M+"}
    
    if app_choice == "PhonePe Business":
        v = {0:"4.5",1:"307 K",2:"10 M+"}
    
    if app_choice == "Kredit Bee":
        v = {0:"4.4",1:"780 K",2:"10 M+"}

    if app_choice == "Lending Kart":
        v = {0:"2.9",1:"18.2 K",2:"1 M+"}
    
    if app_choice == "CASHe":
        v = {0:"4.4",1:"179 K",2:"5 M+"}

    if app_choice == "Khata Book":
        v = {0:"4.6",1:"461 K",2:"50 M+"}
    
    if app_choice == "Vyapaar":
        v = {0:"4.6",1:"84.6 K",2:"5 M+"}
    
    if app_choice == "Slice":
        v = {0:"4.6",1:"84.6 K",2:"5 M+"}
    
    

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

    st.title("Themes")

# hdfc
    
    if (app_choice == "HDFC PayZapp") & (theme_choice == 'Negative Themes'):

        st.header("Negative Themes")
        image = Image.open('hdfc_payzapp_neg2.png')
        st.image(image, caption='HDFC PayZapp Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_minus = read_pkl("cd_hdfc_payzapp_minus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")

    elif (app_choice == "HDFC PayZapp") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes")
        image = Image.open('hdfc_payzapp_pos2.png')
        st.image(image, caption='HDFC PayZapp Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_minus1 = read_pkl("cd_hdfc_payzapp_plus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus1]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus1[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "HDFC PayZapp") & (theme_choice == 'All Themes'):

        st.header("All Themes")
        image = Image.open('hdfc_all.png')
        st.image(image, caption='HDFC PayZapp Reviews')



# zest
    
    if (app_choice == "Zest Money") & (theme_choice == 'Negative Themes'):

        st.header("Negative Themes")
        image = Image.open('zestmoney_neg2.png')
        st.image(image, caption='Zest Money Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_minus1 = read_pkl("cd_zestmoney_minus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus1]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus1[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")



    elif (app_choice == "Zest Money") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes")
        image = Image.open('zestmoney_pos2.png')
        st.image(image, caption='Zest Money Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_minus1 = read_pkl("cd_zestmoney_plus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus1]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus1[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "Zest Money") & (theme_choice == 'All Themes'):

        st.header("All Themes")
        image = Image.open('zest_all.png')
        st.image(image, caption='Zest Money Reviews')


# bhim upi

    elif (app_choice == "NPCI Bhim") & (theme_choice == 'Negative Themes'):

        st.header("Negative Themes")
        image = Image.open('bhimupi_neg2.png')
        st.image(image, caption='NPCI Bhim Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_minus = read_pkl("cd_bhimupi_minus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")

    elif (app_choice == "NPCI Bhim") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes")
        image = Image.open('bhimupi_pos2.png')
        st.image(image, caption='NPCI Bhim Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_minus = read_pkl("cd_bhimupi_plus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "NPCI Bhim") & (theme_choice == 'All Themes'):

        st.header("All Themes.")
        image = Image.open('bhim_all.png')
        st.image(image, caption='NPCI Bhim Reviews')

# google pay business

    elif (app_choice == "GooglePay Business") & (theme_choice == 'Negative Themes'):

        st.header("Negative Themes old")
        image = Image.open('googlepaybusiness_neg.png')
        st.image(image, caption='GooglePay Business Negative Reviews')

        st.header("Negative Themes New")
        image = Image.open('googlepaybusiness_neg2.png')
        st.image(image, caption='Google Business Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_minus = read_pkl("cd_googlepay_minus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")


    elif (app_choice == "GooglePay Business") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes")
        image = Image.open('googlepaybusiness_pos.png')
        st.image(image, caption='GooglePay Business Positive Reviews')

        st.header("Positive Themes New")
        image = Image.open('googlepaybusiness_pos2.png')
        st.image(image, caption='Google Business Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_plus = read_pkl("cd_googlepay_plus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_plus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_plus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "GooglePay Business") & (theme_choice == 'All Themes'):

        st.header("All Themes")
        image = Image.open('googlepaybusiness_all.png')
        st.image(image, caption='GooglePay Business Reviews')


# phonepe business

    elif (app_choice == "PhonePe Business") & (theme_choice == 'Negative Themes'):


        st.header("Negative Themes Old")
        image = Image.open('phonepebusiness_neg.png')
        st.image(image, caption='PhonePe Business Negative Reviews')

        st.header("Negative Themes New")
        image = Image.open('phonepebusiness_neg2.png')
        st.image(image, caption='PhonePe Business Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_phonepe_minus = read_pkl("cd_phonepe_minus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_phonepe_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_phonepe_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")


        #st.write(annotated_text)


    elif (app_choice == "PhonePe Business") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes Old")
        image = Image.open('phonepebusiness_pos.png')
        st.image(image, caption='PhonePe Business Positive Reviews')

        st.header("Positive Themes New")
        image = Image.open('phonepebusiness_pos2.png')
        st.image(image, caption='PhonePe Business Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_phonepe_plus = read_pkl("cd_phonepe_plus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_phonepe_plus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_phonepe_plus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "PhonePe Business") & (theme_choice == 'All Themes'):

        st.header("All Themes")
        image = Image.open('phonepebusiness_all.png')
        st.image(image, caption='PhonePe Business Reviews')
    



# kredit bee

    elif (app_choice == "Kredit Bee") & (theme_choice == 'Negative Themes'):

        st.header("Negative Themes")
        image = Image.open('kreditbee_neg2.png')
        st.image(image, caption='Kredit Bee Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_minus = read_pkl("cd_kreditbee_minus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")

    elif (app_choice == "Kredit Bee") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes")
        image = Image.open('kreditbee_pos2.png')
        st.image(image, caption='Kredit Bee Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_minus = read_pkl("cd_kreditbee_plus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "Kredit Bee") & (theme_choice == 'All Themes'):

        st.header("All Themes")
        image = Image.open('kreditbee_all.png')
        st.image(image, caption='Kredit Bee Reviews')

# cashe

    elif (app_choice == "CASHe") & (theme_choice == 'Negative Themes'):

        st.header("Negative Themes")
        image = Image.open('cashe_neg2.png')
        st.image(image, caption='CASHe Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_minus = read_pkl("cd_cashe_minus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")



    elif (app_choice == "CASHe") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes")
        image = Image.open('cashe_pos2.png')
        st.image(image, caption='CASHe Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_minus = read_pkl("cd_cashe_plus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "CASHe") & (theme_choice == 'All Themes'):

        st.header("All Themes")
        image = Image.open('cashe_all.png')
        st.image(image, caption='CASHe Reviews')

# lending kart

    elif (app_choice == "Lending Kart") & (theme_choice == 'Negative Themes'):

        st.header("Negative Themes")
        image = Image.open('lendingkart_neg2.png')
        st.image(image, caption='Lending Kart Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_minus = read_pkl("cd_lendingkart_minus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")



    elif (app_choice == "Lending Kart") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes")
        image = Image.open('lendingkart_pos2.png')
        st.image(image, caption='Lending Kart Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_minus = read_pkl("cd_lendingkart_plus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "Lending Kart") & (theme_choice == 'All Themes'):

        st.header("All Themes")
        image = Image.open('lendingkart_all.png')
        st.image(image, caption='Lending Kart Reviews')

# khatabook

    elif (app_choice == "Khata Book") & (theme_choice == 'Negative Themes'):

        st.header("Negative Themes")
        image = Image.open('khatabook_neg2.png')
        st.image(image, caption='KhataBook Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_minus = read_pkl("cd_khatabook_minus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")

    elif (app_choice == "Khata Book") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes")
        image = Image.open('khatabook_pos2.png')
        st.image(image, caption='KhataBook Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_minus = read_pkl("cd_khatabook_plus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "Khata Book") & (theme_choice == 'All Themes'):

        st.header("All Themes")
        image = Image.open('khatabook_all.png')
        st.image(image, caption='KhataBook Reviews')

# vyapaar

    elif (app_choice == "Vyapaar") & (theme_choice == 'Negative Themes'):

        st.header("Negative Themes")
        image = Image.open('vyapaar_neg2.png')
        st.image(image, caption='Vyapaar Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_minus = read_pkl("cd_vyapaar_minus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")

    elif (app_choice == "Vyapaar") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes")
        image = Image.open('vyapaar_pos2.png')
        st.image(image, caption='Vyapaar Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_minus = read_pkl("cd_vyapaar_plus")
        option_comment = st.selectbox('How would you like to be contacted?', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "Vyapaar") & (theme_choice == 'All Themes'):

        st.header("All Themes")
        image = Image.open('vyapaar_all.png')
        st.image(image, caption='Vyapaar Reviews')
    
    #slice

    elif (app_choice == "Slice") & (theme_choice == 'Negative Themes'):

        st.header("Negative Themes")
        image = Image.open('slice_neg2.png')
        st.image(image, caption='Slice Negative Reviews')

        st.header("Relevant Negative Comments")

        cd_minus = read_pkl("cd_slice_minus")
        option_comment = st.selectbox('Please Select', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")

    elif (app_choice == "Slice") & (theme_choice == 'Positive Themes'):

        st.header("Positive Themes")
        image = Image.open('slice_pos2.png')
        st.image(image, caption='Slice Positive Reviews')

        st.header("Relevant Positive Comments")

        cd_minus = read_pkl("cd_slice_plus")
        option_comment = st.selectbox('Please Choose', ([*cd_minus]))
        st.write('You selected:', option_comment)

        import re
        reviews_list = cd_minus[option_comment] #['very nice and easy use', 'verry good apps and easy used apps', 'best app from all other upi app.... convient and easy use']
        r = option_comment #"and easy use"
        
        #annotated_text("very nice",("and easy use","feature","#faa"))
        for i in range(len(reviews_list)):
            index = re.search(r,reviews_list[i]).span()
            annotated_text(reviews_list[i][:index[0]-1], (reviews_list[i][index[0]:index[1]],'feature','#faa'), reviews_list[i][index[1]:])
            st.write(" ")
    
    elif (app_choice == "Slice") & (theme_choice == 'All Themes'):

        st.header("All Themes")
        image = Image.open('slice_all.png')
        st.image(image, caption='Slice Reviews')

    else:

        image = Image.open('wip.jpg')
        st.image(image, caption='Under Construction')




    
    #annotated_text(
    #    ("annotated", "", "#faa"),
    #)
    #st.write(annotated_text)
    
 




