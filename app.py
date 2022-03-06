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
                            ["Surgery Service Models",
                             "Design Team",])

    if page ==   "Surgery Service Models":   show_explore()
    elif page == "Design Team":              show_the_app_team()

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
    st.sidebar.subheader('Surgery Service Models')
    exp = st.sidebar.radio('Explore:',
                                ["Home",
                                 "All Emergencies",
                                 "Acute Gallbladder",
                               
                                 ])
    if   exp == "Home":                         exp_about()         #1
    elif exp == "All Emergencies":              exp_A2Z()           #2
    elif exp == "Acute Gallbladder":            exp_dis()           #3

    
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

       
  

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Journals (4)                                                                                   #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_journals():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("Find ") 
   
    
                
                
            
#-------------------------------------------------------------------------------------------#

main()

#if __name__ == "__main__":
#    main()
