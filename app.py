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

    st.sidebar.write('''_Click **X** in top right to hide sidebar_''')
    st.sidebar.subheader('Navigator')
    page = st.sidebar.radio('Go to:',
                            ["Home",
                             "All Emergencies",
                             "Acute Gallbladder",])

    if page ==   "Home":                show_home()
    elif page == "All Emergencies":     show_emerg_all()
    elif page == "Acute Gallbladder":   show_biliary()

    st.sidebar.title("About")
        st.sidebar.info(
            """
            This web app is maintained by Alastair Hayes. You can follow me on social media:
            [LinkedIn](https://www.linkedin.com/in/alastair-hayes).
        """
        )

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

 

 

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Home - About (1)                                                                                      #
# ::: Handles                                                                                     #                                                                                              
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_home():

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
#  Emergency All (2)                                                                                     #
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
import urllib, json
import io
import requests
import time


def show_emerg_all():

    st.write('''_To show sidebar, click **>** in top left_''')
    st.title('Flow of all emergency patients')


    url = 'https://raw.githubusercontent.com/HayesAJ83/EGS/main/data/sankey_energy029.json'   #https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    fig = go.Figure(data=[go.Sankey(
        valueformat = ".0f",
        #valuesuffix = "TWh",
        node = dict(
        pad = 15,
        thickness = 15,
        line = dict(color = "black", width = 0.5),
        label =  data['data'][0]['node']['label'],
        color =  data['data'][0]['node']['color']
        ),
        link = dict(
        source =  data['data'][0]['link']['source'],
        target =  data['data'][0]['link']['target'],
        value =  data['data'][0]['link']['value'],
        label =  data['data'][0]['link']['label']
    ))])

    fig.update_layout(
        hovermode = 'x',
        title="Emergency General Surgery - Pathways<br>Designer: A.Hayes",
        font=dict(size = 10, color = 'midnight blue'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        autosize=False, width=800, height=600,
    )

    st.write(fig)


    

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Acute Gallbladder (3)                                                                                    #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_biliary():
    st.write('''_To show sidebar, click **>** in top left_''')
    st.title("Search") 
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
  

    

            
#-------------------------------------------------------------------------------------------#

main()

#if __name__ == "__main__":
#    main()
