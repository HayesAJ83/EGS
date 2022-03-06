#Copyright [2021] [EXCISION LIMITED]
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


import streamlit as st

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Main                                                                                           #
# ::: Handles the navigation / routing and data loading / caching                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#

def main():
    #components.iframe("https://en.wikipedia.org/wiki/Crohn%27s_disease", scrolling=True)
    st.sidebar.write('''_Click **X** in top right to hide sidebar_''')
    st.sidebar.subheader('Navigator')
    page = st.sidebar.radio('Go to:',
                            ["Emergency Surgery Tool Lab",
                             "Design Team",])

    if page ==   "Surgical Names App":   show_explore()
    elif page == "Design Team":        show_the_app_team()

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  About the team                                                                                 #
# :::                                                                                             #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_the_app_team():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("App Designer")
    st.markdown('''The team consists of a group of General Surgeons based in Edinburgh who are
                motivated to develop software to improve surgical **data systems**,
                **research** and **education**.''')
    st.markdown('''To meet these aims, a company called **Excision** was founded in 2020, and
                **Surgical Names** web app was the first major project.''',unsafe_allow_html=True)

    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info('''Comments, queries and suggestions welcome: ahayes@surgicalnames.com''')
    
    st.subheader("Project Lead & App Developer")
    with st.beta_expander('Alastair Hayes'):
        col1, col2, col3 = st.beta_columns(3)
        image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Alastair_Hayes.png'
        col1.image(image, width=100);
        col2.write('''Alastair is a General Surgery Specialty Training Registrar in Edinburgh with
                    interests in Endocrine, Upper GI & Emergency General Surgery. His qualifications include FRCSEd(Gen) & PhD.''')
        col3.write('''His main coding language is Python & is working to develop software solutions for clinical
                    data system problems, research & education in surgical practice.''')

    st.markdown("---")
    st.subheader("Acknowledgements")
    with st.beta_expander('Websites'):
        st.markdown('''
                    [Pandas](https://pandas.pydata.org),
                    [Plotly](https://plotly.com/python/),
                    [Streamlit](https://www.streamlit.io)''')

 
#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Explorer                                                                                       #
# ::: Handles the navigation                                                                      #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_explore():
    st.sidebar.subheader('Emergency Surgery Tools Lab')
    exp = st.sidebar.radio('Explore:',
                                ["Home",
                                 "Surgical Emergency Patient Flow",
                                 "Emergency Gallbladder",
                                 "By Operation",
                                 ])
    if   exp == "Home":                             exp_about()         #1
    elif exp == "Surgical Emergency Patient Flow":  exp_A2Z()           #2
    elif exp == "Emergency Gallbladder":            exp_dis()           #3
    elif exp == "By Operation":                     exp_operation()     #5

    
#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  About (1)                                                                                      #
# ::: Handles                                                                                     #                                                                                              
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_about():

    st.write('''_To show sidebar, click **>** in top left_''')
    st.markdown('''# Emergency General Surgery''')
    st.markdown('''_A Web App from Excision Ltd_''')
    st.markdown("---")
    with st.beta_expander('Introduction'):
    
        st.write('''With the development of Machine Learning tools, and in particular the excellent format
                    in intuitive & interactive ways**.''')

        st.write('''The functions built into surgicalnames.com are aimed at simulating how we think of terminology
                    of terms related to their work.''')

        st.write('''You will find several **interactive visualizations** which we hope you will find enjoyable
                    original papers & related webpages**.''')

        st.write('''This project, surgicalnames.com, is under continuous development with a growing database of terms
                    & evolving functionality as we develop the software.''')
        st.markdown("---")
        
    with st.beta_expander('Quick Start'):
        st.write('''Navigate with the sidebar on the left. If sidebar is not shown, **click > in top left** to display.
                    Then explore using sidebar options:''')
           
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">A to Z:</span>
                   <span style="font-size:12pt;color:black;">Search by name and filter by specialty.</span>''',
                   unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By Disease or Symptom:</span>
                   <span style="font-size:12pt;color:black;"> Here you can find eponyms related
                   to conditions of interest.</span>''',unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By Operation:</span>
                   <span style="font-size:12pt;color:black;"> Here you can choose an operation type
                   (eg. Oesophagectomy), and then access all the common eponyms related to that
                   procedure.</span>''',unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">By World Maps:</span>
                   <span style="font-size:12pt;color:black;"> Choose a region of the world to find
                   local eponyms. Select a continent, country or city.</span>''',
                   unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Categories:</span>
                   <span style="font-size:12pt;color:black;">Choose from anatomy,
                   incisions, surgical instruments, operations, pathology, physiology, patient
                   positioning, eponymous fluids, clinical scores or signs, statistical tests, surgical
                   maneuvers & techniques, syndromes, doctrines & rules or research trials.
                   </span>''',unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Exam Favourites:
                   </span><span style="font-size:12pt;color:black;"> Select from those often found
                   in exams & filter by speciality.</span>''',unsafe_allow_html=True)
        st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Teaching Tool:</span>
                   <span style="font-size:12pt;color:black;">Choose from Bedside, Classroom or
                   Operating Room modes.</span>''',unsafe_allow_html=True)
        st.markdown("---")


    with st.beta_expander('Disclaimer'):
        st.write('''The data on this site is artificial and purely to allow experimentation of tools.
                 ''')
        st.markdown("---")

    st.markdown("---")
    st.write('''Copyright © 2022 Excision Ltd. All rights reserved.''')


#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  A to Z (2)                                                                                     #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#

import streamlit.components.v1 as components
import pandas as pd
pd.options.display.max_colwidth = 1000000
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import plotly
import plotly.express as px          
import plotly.graph_objects as go    
import plotly.figure_factory as ff
import io
import requests
import time


def exp_A2Z():

    st.write('''_To show sidebar, click **>** in top left_''')
    st.title('Search the full database')
    types = st.radio('Step 1) Choose specialties:',["All",])

    if types == "All":
        @st.cache(suppress_st_warning=True)
        def load_surgepsdata(url):
            time.sleep(0.1)
            return pd.read_csv(url)

        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        DF1 = load_surgepsdata(url)
        df2 = DF1.sort_values(by=['Eponym'],ascending=True)
        st.markdown("---")
        min_yrs, max_yrs = st.slider('Step 2) Define a time window (years):', 100, 2050, [150, 2021])
        st.markdown("---")
        new_1T = df2.loc[(df2['Year'] >= min_yrs) & (df2['Year'] <= max_yrs)]
        blank_row = {'Alphabet':'','Eponym':'1','Eponym_easy':'1','Eponym_easy_yr':'',}
        new_2T = new_1T.append(blank_row, ignore_index=True)
        new_3T = new_2T.sort_values(by=['Eponym'],ascending=True)
        options = st.selectbox('Step 3) Search:',
                        new_3T['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)
        df_ep_info = new_3T[new_3T['Eponym_easy'].str.match(options)]


    

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Disease (3)                                                                                    #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_dis():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("Search by disease, sign or symptom") 
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df1 = df['Disease'].dropna()
    string = df1.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    disease = st.multiselect('Step 1) Choose a disease, sign or symptom:', options=list(U),)
    st.markdown("---")
    new_dis1 = df.loc[df['Disease'].str.contains('|'.join(disease)) == True]
    new_dis2 = new_dis1.sort_values(by=['Eponym'],ascending=True)
    if disease:
        options = st.selectbox('Step 2) Search list of related terms:',
                                   new_dis2['Eponym_easy'].unique(),
                               format_func=lambda x: ' ' if x == '1' else x)

        df_ep_info = new_dis1[new_dis1['Eponym_easy'].str.match(options)]
        ep_yr = df_ep_info['Year'].to_string(index=False)

        if options == "Aaron sign":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
            st.image(image, width=160)
        if options == "Allis forceps":
            image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
            image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
            col1, col2, col3, col4 = st.beta_columns(4)
            col1.image(image_human, width=160);col2.image(image_forceps, width=386)
            col3.write(''); col4.write('')
        if options == "Allison lung retractor":
            image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
            st.image(image, width=160)

   
  
      

        else:pass
        if df_ep_info['Who'].any(): st.write('*_Who_*:', df_ep_info['Who_B'].to_string(index=False))
        else: pass
        if df_ep_info['Year'].any(): st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))
        else:pass
        if df_ep_info['Where'].any(): st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))
        else:pass

        if df_ep_info['Description'].any():
            st.markdown("---")
        description = df_ep_info['Description'].to_string(index=False)
        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass

        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass

     

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Journals (4)                                                                                   #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_journals():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("Find which eponyms originate from particular journals") 
    ScreenSize = st.radio('Step 1) Select screen size:',
                          options=['Smartphone',
                                   'Desktop / Laptop / Tablet'],index=0)

    if ScreenSize == "Smartphone":
        types = st.radio('Step 2) Choose specialties:',["All","Selected",])
        if types == 'All':
            min_yrs, max_yrs = st.slider("3rd) Choose time window:", 1700, 2030, [1715, 2021])
            url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
            dfY = pd.read_csv(url_J) #,dtype={'year':int}) 
            dfY1 = dfY.dropna()
            dfY1["Journals"] = "Journals"
            dfT = dfY1.sort_values(by=['year'],ascending=True)
            time_df = dfT.loc[(dfT['year'] >= min_yrs) & (dfT['year'] <= max_yrs)]
            time_spec_df = time_df['specialty'].dropna()
            string = time_spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            st.markdown("---")
            st.markdown('''<span style="font-size:10pt;color:black;">**Click on journal name to zoom in**,
                       and in the center to pan out.</span>''', unsafe_allow_html=True)
            figJDLT = px.sunburst(time_df,path=['Journals','journal_short','year','eponym'],
                                  color='Log2 Google hits',hover_data=['eponym'],color_continuous_scale='RdBu',)
            figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0),width=400,height=300)
            figJDLT.update_traces(hovertemplate='<b>%{label}</b>')
            st.write(figJDLT)
            st.markdown("---")
            time_jrnl = time_df.sort_values(by=['journal'],ascending=True)
            time_jrnl1 = time_jrnl['journal'].dropna()
            string1 = time_jrnl1.str.cat(sep=',')
            splits1 = string1.split(",")
            S1 = set(splits1)
            T1 = np.array(list(S1)).astype(object)
            U1 = np.sort(T1)
            jrnls = st.multiselect('4th) Select journals:',options=list(U1),
                              format_func=lambda x: ' ' if x == '1' else x)
            new_jrnls1 = time_df.loc[time_df['journal'].str.contains('|'.join(jrnls)) == True]
            new_jrnls2 = new_jrnls1.sort_values(by=['eponym_yr'],ascending=True)
            if jrnls:
                options = st.selectbox('5th) Eponyms in selected journals:',
                                  new_jrnls2['eponym_yr'].unique(), format_func=lambda x: ' ' if x == '1' else x)
                df_ep_info = new_jrnls1[new_jrnls1['eponym_yr'].str.match(options)]
                journal = df_ep_info['journal_name'].to_string(index=False)

            

                if df_ep_info['journal_name'].any(): st.write(journal, unsafe_allow_html=True)
                else: pass
                if df_ep_info['year_str'].any():st.write('_When_:',df_ep_info['year_str'].to_string(index=False))
                else: pass
                if df_ep_info['Who'].any():st.write('_Who_:',df_ep_info['Who'].to_string(index=False))

                if df_ep_info['Ref'].any():
                    st.markdown("---")
                    st.write('<u>References</u>', unsafe_allow_html=True)
                    st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
           

                
                #if df_ep_info2['Description'].any():
                #    st.markdown(description, unsafe_allow_html=True)
                #if df_ep_info2['History'].any():
                #    st.write('**_History_**:', history)
                #st.markdown("---")


        if types == 'Selected':
            url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
            dfY = pd.read_csv(url_J) #,dtype={'year':int})
            dfY1 = dfY.dropna()
            dfY1["Journals"] = "Journals"
            df2 = dfY1.sort_values(by=['year'],ascending=True)
            spec_df = df2['specialty'].dropna()
            string = spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            journal_spec = st.multiselect('Specilaties of interest - pick and choose',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Academic','Anaesthetics','Bariatrics','Breast','Cardiothoracics',
                                    'Colorectal','Emergency Surgery','Endocrine','ENT',
                                    'General Surgery','Gynaecology','HPB','Hernia',
                                    'Laparoscopic Surgery','Maxillofacial','Neurosurgery','Obstetrics',
                                    'Oesophagogastric','Orthopaedics','Paediatrics','Plastics','Radiology',
                                    'Transplant','Trauma','Urology','Vascular',]
                                          )
            min_yrs, max_yrs = st.slider("3rd) Choose time window:", 1700, 2030, [1715, 2021])
            st.markdown("---")
            st.markdown('''<span style="font-size:10pt;color:black;">**Click on journal name to zoom in**,
                       and in the center to pan out.</span>''', unsafe_allow_html=True)
            new_jrnls1 = df2.loc[df2['specialty'].str.contains('|'.join(journal_spec)) == True]
            new_jrnls1T = new_jrnls1.loc[(new_jrnls1['year'] >= min_yrs) & (new_jrnls1['year'] <= max_yrs)]
            new_jrnls2T = new_jrnls1T.sort_values(by=['eponym'],ascending=True)
            new_jrnls2T["Journals"] = "Journals"
            if not journal_spec == None:
                figJDLT = px.sunburst(new_jrnls2T,path=['Journals','journal_short','year','eponym'],#values='Log10 Google hits',
                                      color='Log2 Google hits',hover_data=['eponym'], color_continuous_scale='RdBu',)
                      #inferno,thermal,Magma,Cividis,deep,Viridis,icefire,ylgnbu,'portland','agsunset'
                figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0),width=400,height=300)
                figJDLT.update_traces(hovertemplate='<b>%{label}</b>')
                st.write(figJDLT)

            time_jrnl = new_jrnls1T.sort_values(by=['journal'],ascending=True)
            time_jrnl1 = time_jrnl['journal'].dropna()
            string1 = time_jrnl1.str.cat(sep=',')
            splits1 = string1.split(",")
            S1 = set(splits1)
            T1 = np.array(list(S1)).astype(object)
            U1 = np.sort(T1)
            st.markdown("---")
            
            jrnls = st.multiselect('4th) Select journals:',options=list(U1),
                                   format_func=lambda x: ' ' if x == '1' else x)
            new_jrnls1 = new_jrnls2T.loc[new_jrnls2T['journal'].str.contains('|'.join(jrnls)) == True]
            new_jrnls2 = new_jrnls1.sort_values(by=['eponym_yr'],ascending=True)

            if jrnls:
                options = st.selectbox('5th) Eponyms in selected journals:',
                                  new_jrnls2['eponym_yr'].unique(), format_func=lambda x: ' ' if x == '1' else x)
                df_ep_info = new_jrnls1[new_jrnls1['eponym_yr'].str.match(options)]
                journal = df_ep_info['journal_name'].to_string(index=False)

                if options == "Aaron sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                    st.image(image, width=160)
                if options == "Allis forceps":
                    image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis.png'
                    image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allis_Forceps.png'
                    col1, col2, col3, col4 = st.beta_columns(4)
                    col1.image(image_human, width=160);col2.image(image_forceps, width=386)
                    col3.write(''); col4.write('')
                if options == "Allison lung retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Allison repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Altemeier procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                    st.image(image, width=160)
                if options == "Ambrosetti classification":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                    st.image(image, width=160)
                if options == "Amyand hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                    st.image(image, width=160)
                if options == "Babcock forceps":
                    image_human = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock.png'
                    image_forceps = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Babcock_Forceps2.png'
                    col1, col2, col3, col4 = st.beta_columns(4)
                    col1.image(image_human, width=160); col2.image(image_forceps, width=297);
                    col3.write(''); col4.write('')
                if options == "Barrett's oesophagus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                    st.image(image, width=160)
                if options == "Bassini hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                    st.image(image, width=160)
                if options == "Battle's sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                    st.image(image, width=160)
                if options == "Beger procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                    st.image(image, width=160)
                if options == "Berry's ligament":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                    st.image(image, width=160)
                if options == "Brown-Séquard syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                    st.image(image, width=160)
                if options == "Brooke ileostomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                    st.image(image, width=160)
                if options == "Calot's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                    st.image(image, width=500)
                if options == "Cushing's ulcer":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                    st.image(image, width=160)
                if options == "DeBakey forceps":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                    st.image(image, width=300)
                if options == "De Garengeot's hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                    st.image(image, width=160)
                if options == "Delorme's procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                    st.image(image, width=160)
                if options == "Fanelli catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                    st.image(image, width=160)
                if options == "Foley catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                    st.image(image, width=160)
                if options == "Graves disease":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                    st.image(image, width=160)
                if options == "Hartmann's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hartmann's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hashimoto's thyroiditis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                    st.image(image, width=160)
                if options == "Ivor Lewis oesophagectomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                    st.image(image, width=160)
                if options == "Joll's retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Joll's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Killian's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                    st.image(image, width=160)
                if options == "Kocher's incision of the abdomen":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Kocher maneuver":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Meckel's diverticulum":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                    st.image(image, width=160)
                if options == "Merendino jejunal interposition":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                    st.image(image, width=160)
                if options == "Morrison's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                    st.image(image, width=160)
                if options == "Nodules of Aranzio":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                    st.image(image, width=160)
                if options == "Sphincter of Oddi":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                    st.image(image, width=160)
                if options == "Mirizzi's syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                    st.image(image, width=160)
                if options == "Rouviere's sulcus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                    st.image(image, width=160)
                if options == "Shouldice hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                    st.image(image, width=160)
                if options == "Strasberg's critical view of safety":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                    st.image(image, width=160)
                if options == "Takayasu's arteritis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                    st.image(image, width=160)
                if options == "Ligament of Treitz":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                    st.image(image, width=160)
                if options == "Whipple's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                    st.image(image, width=160)
                if options == "Foramen of Winslow":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                    st.image(image, width=160)

                if df_ep_info['journal_name'].any(): st.write(journal, unsafe_allow_html=True)
                else: pass
                if df_ep_info['year_str'].any():st.write('_When_:',df_ep_info['year_str'].to_string(index=False))
                else: pass
                if df_ep_info['Who'].any():st.write('_Who_:',df_ep_info['Who'].to_string(index=False))
                else: pass

                if df_ep_info['Ref'].any():
                    st.markdown("---")
                    st.write('<u>References</u>', unsafe_allow_html=True)
                    st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
                else: pass
                
                #if df_ep_info2['Description'].any():
                #    st.markdown(description, unsafe_allow_html=True)
                #if df_ep_info2['History'].any():
                #    st.write('**_History_**:', history)



    if ScreenSize == "Desktop / Laptop / Tablet":
        types = st.radio('2nd) Choose specialties:',["All","Selected",])
        if types == 'All':
            min_yrs, max_yrs = st.slider("3rd) Choose time window:", 1700, 2030, [1715, 2021])
            st.markdown("---")
            url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
            dfY = pd.read_csv(url_J) #, dtype={'year':int})
            dfY1 = dfY.dropna()
            dfY1["Journals"] = "Journals"
            dfT = dfY1.sort_values(by=['year'],ascending=True)
            time_df = dfT.loc[(dfT['year'] >= min_yrs) & (dfT['year'] <= max_yrs)]
            time_spec_df = time_df['specialty'].dropna()
            string = time_spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            st.markdown('''<span style="font-size:12pt;color:black;">**Click on journal name to zoom in**,
                       and click in the center to pan out.</span>''', unsafe_allow_html=True)
            figJDLT = px.sunburst(time_df,path=['Journals','journal_short','year','eponym'],
                            color='Log2 Google hits',hover_data=['eponym'],#values='Log10 Google hits',
                            color_continuous_scale='rdbu',
                                  ) #'RdBu'
            figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=10),width=700,height=550)
            figJDLT.update_traces(hovertemplate='<b>%{label}</b>')
            st.write(figJDLT)
            st.markdown("---")
            time_jrnl = time_df.sort_values(by=['journal'],ascending=True)
            time_jrnl1 = time_jrnl['journal'].dropna()
            string1 = time_jrnl1.str.cat(sep=',')
            splits1 = string1.split(",")
            S1 = set(splits1)
            T1 = np.array(list(S1)).astype(object)
            U1 = np.sort(T1)
            jrnls = st.multiselect('4th) Select journals:',options=list(U1),
                              format_func=lambda x: ' ' if x == '1' else x)
            new_jrnls1 = time_df.loc[time_df['journal'].str.contains('|'.join(jrnls)) == True]
            new_jrnls2 = new_jrnls1.sort_values(by=['eponym_yr'],ascending=True)
            if jrnls:
                options = st.selectbox('5th) Eponyms in selected journals:',
                                  new_jrnls2['eponym_yr'].unique(), format_func=lambda x: ' ' if x == '1' else x)
                df_ep_info = new_jrnls1[new_jrnls1['eponym_yr'].str.match(options)]
                journal = df_ep_info['journal_name'].to_string(index=False)

                if options == "Aaron sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                    st.image(image, width=160)
                if options == "Allison lung retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Allison repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Altemeier procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                    st.image(image, width=160)
                if options == "Ambrosetti classification":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                    st.image(image, width=160)
                if options == "Amyand hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                    st.image(image, width=160)
                if options == "Barrett's oesophagus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                    st.image(image, width=160)
                if options == "Bassini hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                    st.image(image, width=160)
                if options == "Battle's sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                    st.image(image, width=160)
                if options == "Beger procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                    st.image(image, width=160)
                if options == "Berry's ligament":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                    st.image(image, width=160)
                if options == "Brown-Séquard syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                    st.image(image, width=160)
                if options == "Brooke ileostomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                    st.image(image, width=160)
                if options == "Calot's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                    st.image(image, width=500)
                if options == "Cushing's ulcer":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                    st.image(image, width=160)
                if options == "DeBakey forceps":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                    st.image(image, width=300)
                if options == "De Garengeot's hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                    st.image(image, width=160)
                if options == "Delorme's procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                    st.image(image, width=160)
                if options == "Fanelli catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                    st.image(image, width=160)
                if options == "Foley catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                    st.image(image, width=160)
                if options == "Graves disease":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                    st.image(image, width=160)
                if options == "Hartmann's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hartmann's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hashimoto's thyroiditis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                    st.image(image, width=160)
                if options == "Ivor Lewis oesophagectomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                    st.image(image, width=160)
                if options == "Joll's retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Joll's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Killian's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                    st.image(image, width=160)
                if options == "Kocher's incision of the abdomen":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Kocher maneuver":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Meckel's diverticulum":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                    st.image(image, width=160)
                if options == "Merendino jejunal interposition":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                    st.image(image, width=160)
                if options == "Morrison's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                    st.image(image, width=160)
                if options == "Nodules of Aranzio":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                    st.image(image, width=160)
                if options == "Sphincter of Oddi":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                    st.image(image, width=160)
                if options == "Mirizzi's syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                    st.image(image, width=160)
                if options == "Rouviere's sulcus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                    st.image(image, width=160)
                if options == "Shouldice hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                    st.image(image, width=160)
                if options == "Strasberg's critical view of safety":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                    st.image(image, width=160)
                if options == "Takayasu's arteritis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                    st.image(image, width=160)
                if options == "Ligament of Treitz":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                    st.image(image, width=160)
                if options == "Whipple's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                    st.image(image, width=160)
                if options == "Foramen of Winslow":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                    st.image(image, width=160)


                if df_ep_info['journal_name'].any(): st.write(journal, unsafe_allow_html=True)
                else: pass
                if df_ep_info['year_str'].any():st.write('_When_:',df_ep_info['year_str'].to_string(index=False))
                else: pass
                if df_ep_info['Who'].any():st.write('_Who_:',df_ep_info['Who'].to_string(index=False))
                else: pass

                if df_ep_info['Ref'].any():
                    st.markdown("---")
                    st.write('<u>References</u>', unsafe_allow_html=True)
                    st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
                else: pass

                #if df_ep_info2['Description'].any():
                #    st.markdown(description, unsafe_allow_html=True)
                #if df_ep_info2['History'].any():
                #    st.write('**_History_**:', history)
                

        if types == 'Selected':
            url_J = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite4Journals.csv'
            dfY = pd.read_csv(url_J)
            dfY1 = dfY.dropna()
            dfY1["Journals"] = "Journals"
            df2 = dfY1.sort_values(by=['year'],ascending=True)
            spec_df = df2['specialty'].dropna()
            string = spec_df.str.cat(sep=',')
            splits = string.split(",")
            S = set(splits)
            T = np.array(list(S)).astype(object)
            U = np.sort(T)
            journal_spec = st.multiselect('Specilaties of interest - pick and choose',options=list(U),
                           format_func=lambda x: ' ' if x == '1' else x,
                           default=['Academic','Anaesthetics','Bariatrics','Breast','Cardiothoracics',
                                    'Colorectal','Emergency Surgery','Endocrine','ENT',
                                    'General Surgery','Gynaecology','HPB','Hernia',
                                    'Laparoscopic Surgery','Maxillofacial','Neurosurgery','Obstetrics',
                                    'Oesophagogastric','Orthopaedics','Paediatrics','Plastics','Radiology',
                                    'Transplant','Trauma','Urology','Vascular',])
            min_yrs, max_yrs = st.slider("3rd) Choose time window:", 1700, 2030, [1715, 2021])
            st.markdown("---")
            st.markdown('''<span style="font-size:12pt;color:black;">**Click on journal name to zoom in**,
                       and click in the center to pan out.</span>''', unsafe_allow_html=True)
            new_jrnls1 = df2.loc[df2['specialty'].str.contains('|'.join(journal_spec)) == True]
            new_jrnls1T = new_jrnls1.loc[(new_jrnls1['year'] >= min_yrs) & (new_jrnls1['year'] <= max_yrs)]
            new_jrnls2T = new_jrnls1T.sort_values(by=['eponym'],ascending=True)
            new_jrnls2T["Journals"] = "Journals"
            if not journal_spec == None:
                figJDLT = px.sunburst(new_jrnls2T,path=['Journals','journal_short','year','eponym'],
                                      color='Log2 Google hits',hover_data=['eponym'], color_continuous_scale='rdbu')
                figJDLT.update_layout(margin=dict(l=0, r=0, t=0, b=0),width=700,height=550)
                figJDLT.update_traces(hovertemplate='<b>%{label}</b>')
                st.write(figJDLT)
            st.markdown("---")
            time_jrnl = new_jrnls1T.sort_values(by=['journal'],ascending=True)
            time_jrnl1 = time_jrnl['journal'].dropna()
            string1 = time_jrnl1.str.cat(sep=',')
            splits1 = string1.split(",")
            S1 = set(splits1)
            T1 = np.array(list(S1)).astype(object)
            U1 = np.sort(T1)
        
            jrnls = st.multiselect('4th) Select journals:',options=list(U1),
                              format_func=lambda x: ' ' if x == '1' else x)
            new_jrnls1 = new_jrnls2T.loc[new_jrnls2T['journal'].str.contains('|'.join(jrnls)) == True]
            new_jrnls2 = new_jrnls1.sort_values(by=['eponym_yr'],ascending=True)

            if jrnls:
                options = st.selectbox('5th) Eponyms in selected journals:',
                                  new_jrnls2['eponym_yr'].unique(), format_func=lambda x: ' ' if x == '1' else x)
                df_ep_info = new_jrnls1[new_jrnls1['eponym_yr'].str.match(options)]
                journal = df_ep_info['journal_name'].to_string(index=False)

                if options == "Aaron sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aaron.png'
                    st.image(image, width=160)
                if options == "Allison lung retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Allison repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Allison.png'
                    st.image(image, width=160)
                if options == "Altemeier procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Altemeier.png'
                    st.image(image, width=160)
                if options == "Ambrosetti classification":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ambrosetti.png'
                    st.image(image, width=160)
                if options == "Amyand hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Amyand.png'
                    st.image(image, width=160)
                if options == "Barrett's oesophagus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Barrett.png'
                    st.image(image, width=160)
                if options == "Bassini hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Bassini.png'
                    st.image(image, width=160)
                if options == "Battle's sign":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Battle.png'
                    st.image(image, width=160)
                if options == "Beger procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Beger.png'
                    st.image(image, width=160)
                if options == "Berry's ligament":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Berry.png'
                    st.image(image, width=160)
                if options == "Brown-Séquard syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brown-Sequard.png'
                    st.image(image, width=160)
                if options == "Brooke ileostomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Brooke.png'
                    st.image(image, width=160)
                if options == "Calot's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Calot2.png'
                    st.image(image, width=500)
                if options == "Cushing's ulcer":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Cushing.png'
                    st.image(image, width=160)
                if options == "DeBakey forceps":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_DeBakey_Forceps.png'
                    st.image(image, width=300)
                if options == "De Garengeot's hernia":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_De_Garengeot.png'
                    st.image(image, width=160)
                if options == "Delorme's procedure":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Delorme.png'
                    st.image(image, width=160)
                if options == "Fanelli catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Fanelli.png'
                    st.image(image, width=160)
                if options == "Foley catheter":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Foley.png'
                    st.image(image, width=160)
                if options == "Graves disease":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Graves.png'
                    st.image(image, width=160)
                if options == "Hartmann's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hartmann's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Henri_Hartmann.png'
                    st.image(image, width=160)
                if options == "Hashimoto's thyroiditis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Hashimoto.png'
                    st.image(image, width=160)
                if options == "Ivor Lewis oesophagectomy":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Ivor_Lewis.png'
                    st.image(image, width=160)
                if options == "Joll's retractor":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Joll's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Joll.png'
                    st.image(image, width=160)
                if options == "Killian's triangle":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Killian.png'
                    st.image(image, width=160)
                if options == "Kocher's incision of the abdomen":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Kocher maneuver":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Kocher.png'
                    st.image(image, width=160)
                if options == "Meckel's diverticulum":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Meckel.png'
                    st.image(image, width=160)
                if options == "Merendino jejunal interposition":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Merendino.png'
                    st.image(image, width=160)
                if options == "Morrison's pouch":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Morrison.png'
                    st.image(image, width=160)
                if options == "Nodules of Aranzio":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Aranzi.png'
                    st.image(image, width=160)
                if options == "Sphincter of Oddi":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Oddi.png'
                    st.image(image, width=160)
                if options == "Mirizzi's syndrome":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Pablo_Mirizzi.png'
                    st.image(image, width=160)
                if options == "Rouviere's sulcus":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Rouviere.png'
                    st.image(image, width=160)
                if options == "Shouldice hernia repair":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Shouldice.png'
                    st.image(image, width=160)
                if options == "Strasberg's critical view of safety":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Strasberg.png'
                    st.image(image, width=160)
                if options == "Takayasu's arteritis":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Takayasu.jpg'
                    st.image(image, width=160)
                if options == "Ligament of Treitz":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Treitz.png'
                    st.image(image, width=160)
                if options == "Whipple's operation":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Whipple.png'
                    st.image(image, width=160)
                if options == "Foramen of Winslow":
                    image = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/x_Winslow.png'
                    st.image(image, width=160)

                if df_ep_info['journal_name'].any(): st.write(journal, unsafe_allow_html=True)
                else: pass
                if df_ep_info['year_str'].any():st.write('_When_:',df_ep_info['year_str'].to_string(index=False))
                else: pass
                if df_ep_info['Who'].any():st.write('_Who_:',df_ep_info['Who'].to_string(index=False))
                else: pass
                if df_ep_info['Ref'].any():
                    st.markdown("---")
                    st.write('<u>References</u>', unsafe_allow_html=True)
                    st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
                else: pass
                
                #if df_ep_info2['Description'].any():
                #    st.markdown(description, unsafe_allow_html=True)
                #if df_ep_info2['History'].any():
                #    st.write('**_History_**:', history)


#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Surgical Operations (5)                                                                        #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_operation():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.markdown(
        """<style type="text/css" media="screen">.hovertext text {font-size: 20px !important;}
        </style>""",unsafe_allow_html=True,)

    st.title("Find eponyms relevant to your operation") 
    #Page
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
    df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int,})
    df2 = df1.sort_values(by=['Year'],ascending=True)
    df3 = df2.sort_values(by=['Operation'],ascending=True)  #Gives eponyms by operation alphabetically
    df4 = df3['Operation'].dropna()
    string = df4.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    eponymByOp = st.multiselect('Step 1) Select from operations:',options=list(U),
                                format_func=lambda x: ' ' if x == '1' else x)
    new_df = df1.loc[df1['Operation'].str.contains('|'.join(eponymByOp)) == True]
    new_df2 = new_df.sort_values(by=['Eponym'],ascending=True)
 
    if eponymByOp:
        options = st.selectbox('Step 2) Search list:', new_df2['Eponym_easy'].unique(),
                                  format_func=lambda x: ' ' if x == '1' else x)
        df_ep_info = new_df[new_df['Eponym_easy'].str.match(options)]
        ep_yr = df_ep_info['Year'].to_string(index=False)




        if df_ep_info['Description'].any():
            st.markdown("---")

        description = df_ep_info['Description'].to_string(index=False)

        if df_ep_info['Description'].any():
            st.markdown(description, unsafe_allow_html=True)
        else:pass

        if df_ep_info['Ref'].any():
            st.markdown("---")
            st.write('<u>References</u>', unsafe_allow_html=True)
            st.write(df_ep_info['Ref'].to_string(index=False), unsafe_allow_html=True)
        else: pass

        if df_ep_info['Pubmed'].any() or df_ep_info['Ref_site'].any() or df_ep_info['Wiki_link'].any() or df_ep_info['WNI_link'].any():
            st.markdown("---")
            st.write('<u>External Links</u>', unsafe_allow_html=True)

        ref_site = df_ep_info['Ref_site'].to_string(index=False)
        if df_ep_info['Ref_site'].any(): st.markdown(f"* **Primary Paper** [webpage]({ref_site})")
        else:pass
        pub_link = df_ep_info['Pubmed'].to_string(index=False)
        if df_ep_info['Pubmed'].any(): st.markdown(f"* **Pubmed** [webpage]({pub_link})")
        else:pass
        wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
        if df_ep_info['Wiki_link'].any(): st.markdown(f"* **Wikipedia** [webpage]({wiki_link})")
        else:pass
        wni_link = df_ep_info['WNI_link'].to_string(index=False)
        if df_ep_info['WNI_link'].any(): st.markdown(f"* **Whonamedit** [webpage]({wni_link})")
        else:pass


#-------------------------------------------------------------------------------------------#

main()

#if __name__ == "__main__":
#    main()
