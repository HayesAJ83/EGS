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
    elif page == "Obstruction":         show_obstruction()

    st.sidebar.subheader("About")
    st.sidebar.info(
        """
            This web app was built by General Surgeon and Programer Alastair Hayes who also built [SurgicalNames](https://www.surgicalnames.com)
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

    st.title('''Surg-Flow''')
    st.markdown('''### _An interactive surgical patient pathway tool_''')
    st.markdown('''_A Web App from Excision Ltd_''')
    st.markdown("---")
    with st.beta_expander('Introduction'):
        st.write('''This web app was made to experiment with visualisation methods for patient pathways.''')
        
    with st.beta_expander('Quick Start'):
        st.write('''Navigate with the sidebar on the left. If sidebar is not shown, **click > in top left** to display.''')

    with st.beta_expander('Disclaimer'):
        st.write('''The data on this site is artificial and created to allow development of tools.''')

    st.write('''<br>Surg-Flow | Copyright © 2022 Excision Ltd | All rights reserved''', unsafe_allow_html=True)


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

    st.title('''All emergency general surgery patients''')
    st.write(
        '''Click and drag elements of the Sankey diagram to best see how parts of the pathway communicate. 
        '''
        )

    url = 'https://raw.githubusercontent.com/HayesAJ83/EGS_old/main/data/sankey_energy029.json'   #https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    fig_all = go.Figure(data=[go.Sankey(
        valueformat = ".0f",
        #valuesuffix = "TWh",
        node = dict(
        pad = 15,
        thickness = 15,
        line = dict(color = "black", width = 0.5),
        label =  data['data'][0]['node']['label'],
        customdata = [  "A&E referals", 
                        "GP referals", 
                        "Referals from other departments", 
                        "Number going to surgical assessment unit",
                        "Number having surgery", 
                        "Number going to HDU",
                        "Number going to Surgical ward",
                        "Number going to ITU", 
                        "Number discharged home", 
                        "Number died in hospital",
                    ],
            
        hovertemplate='%{customdata} = %{value}<extra></extra>',

        color =  data['data'][0]['node']['color']
        ),
        link = dict(
        source =  data['data'][0]['link']['source'],
        target =  data['data'][0]['link']['target'],
        value =   data['data'][0]['link']['value'],
        label =   data['data'][0]['link']['label'],
        #color =  data['data'][0]['link']['color']
            
    ))])

    fig_all.update_layout(
        hovermode = 'x',
        font=dict(size = 11, color = 'midnight blue'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        autosize=False, height=650,
    )

    st.write(fig_all)
    st.write('''<br>Surg-Flow | Copyright © 2022 Excision Ltd | All rights reserved''', unsafe_allow_html=True)


#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Acute Gallbladder (3)                                                                                    #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_biliary():
    st.title('''Acute gallbladder patients''')
    st.write(
        '''Click and drag elements of the Sankey diagram to best see how parts of the pathway communicate. 
        '''
        )

    url = 'https://raw.githubusercontent.com/HayesAJ83/EGS/main/Data/sankey_energyGB24.json'   #https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    fig_gb = go.Figure(data=[go.Sankey(
        valueformat = ".0f",
        node = dict(
        pad = 15,
        thickness = 15,
        line = dict( color = "black", width = 0.5),
        label =  data['data'][0]['node']['label'],
        color =  data['data'][0]['node']['color']
        ),
        link = dict(
        source =  data['data'][0]['link']['source'],
        target =  data['data'][0]['link']['target'],
        value =   data['data'][0]['link']['value'],
        label =   data['data'][0]['link']['label']
    ))])

    fig_gb.update_layout(
        hovermode = 'x',
        font=dict(size = 11, color = 'midnight blue'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        autosize=False, height=650,
    )

    st.write(fig_gb)
    st.write('''<br>Surg-Flow | Copyright © 2022 Excision Ltd | All rights reserved''', unsafe_allow_html=True)
    

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Obstruction (4)                                                                                    #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_biliary():
    st.title('''Obstructed patients''')
    st.write(
        '''Click and drag elements of the Sankey diagram to best see how parts of the pathway communicate. 
        '''
        )

    url = 'https://raw.githubusercontent.com/HayesAJ83/EGS/main/Data/sankey_energyObs01.json'   #https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    fig_gb = go.Figure(data=[go.Sankey(
        valueformat = ".0f",
        node = dict(
        pad = 15,
        thickness = 15,
        line = dict( color = "black", width = 0.5),
        label =  data['data'][0]['node']['label'],
        color =  data['data'][0]['node']['color']
        ),
        link = dict(
        source =  data['data'][0]['link']['source'],
        target =  data['data'][0]['link']['target'],
        value =   data['data'][0]['link']['value'],
        label =   data['data'][0]['link']['label']
    ))])

    fig_gb.update_layout(
        hovermode = 'x',
        font=dict(size = 11, color = 'midnight blue'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        autosize=False, height=650,
    )

    st.write(fig_gb)
    st.write('''<br>Surg-Flow | Copyright © 2022 Excision Ltd | All rights reserved''', unsafe_allow_html=True)
    
            
#-------------------------------------------------------------------------------------------#

main()

#if __name__ == "__main__":
#    main()
