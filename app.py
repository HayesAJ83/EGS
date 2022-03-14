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
import streamlit.components.v1 as components

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
                             "Acute Gallbladder",
                             "GI Obstruction",
                             "RIF pain",
                             "Network Flow",
                             
                             ])

    if page ==   "Home":                show_home()
    elif page == "All Emergencies":     show_emerg_all()
    elif page == "Acute Gallbladder":   show_biliary()
    elif page == "GI Obstruction":      show_obstruct()
    elif page == "RIF pain":            show_RIF()
    #elif page == "Network Flow - curved":       show_networkflowcurve()
    elif page == "Network Flow":        show_networkflow()

    st.sidebar.subheader("About")
    st.sidebar.info(
        """
            This web app was built by General Surgeon and Programer Alastair Hayes who also built [SurgicalNames.com](https://www.surgicalnames.com)
        """
        )


#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Home - About (1)                                                                                      #
# ::: Handles                                                                                     #                                                                                              
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_home():

    st.title('''Surg-Flow''')
    st.markdown('''### _An interactive surgical pathway tool_''')
    st.markdown('''_A Web App from Excision Ltd_''')
    st.write("#")

    st.info(
        """
            This web app was made to experiment with visualisation methods for patient pathways. 
            Use the sidebar on the left to navigate.
        """
        )
    st.write("#")

    components.html(
        """
        <div style="text-align: center; font-family:sans-serif; font-size: 20px">Emergency General Surgery - Categories</div>
        """,
        height=35,
    )

    fig2 = go.Figure(go.Sunburst(
        labels=
[ "Surgical Abdomen", 
                "Bleeding", 
                    "GI tract",
                        "Upper",
                             "Benign ulcer","UGI cancer","Dieulafoy lesion","Varices",
                        "Lower",
                             "Diverticular bleed","Haemorrhoids","Colorectal Cancer",
                    "Mesentery",
                        "Trauma",
                             "Blunt","Penetrating",
                    "Solid organ",
                         "Liver",
                             "Liver injury",
                         "Spleen",
                             "Splenic injury",
                         "Kidney",
                             "Kidney injury",
                    "Vascular",
                        "AAA rupture",
            
                "Ischaemia", 
                    "Mesenteric",
                    "Ischaemic colitis",
                    
                "Obstruction", 
                    "Bile duct",
                        "CBD stones",
                        "Mirizzi synd.",
                    "Small bowel", 
                        "Adhesions",
                        "Hernia",
                            "Groin",
                                "Femoral",
                                "Inguinal",
                                    "Direct",
                                    "Indirect",
                                "Obturator",
                            "Internal hernia",
                                 "Band adhesion","Mesenteric defect",
                            "Ventral",
                                 "Incisional","Umbilical",
                        "Blockage",
                            "Gallstone ileus",
                     "Colonic",
                        "Volvulus",
                        "Stricture",
                     "Gastric",
                        "Cancer",
                        "Gastric volvulus",
                     "Urinary",
                         "Retention","Stone",
                     "Rectum",
                         "Foreign body ",
                     
                "Peritonitis", 
                    "Appendicitis",
                        "Complicated",
                        "Simple",
                    "Colitis",
                        "Diverticulitis",
                        "Ischaemic",
                        "Stercoral colitis",
                        "Ulcerative colitis",
                    "Gallbladder",
                        "Cholecystitis",
                        "Gallbladder pain",
                    "Pancreatitis",
                        "Biliary",
                        "Non-biliary",
                    "Perforation",
                        "Upper GI",
                             "Duodenal ulcer","Gastric ulcer","Gastroscope",
                        "Lower GI",
                             "Colonoscope","Diverticular","Foreign body","Stercoral",
                ],
    
        parents=[ "",    
                    "Surgical Abdomen",  
                        "Bleeding",
                             "GI tract",
                                 "Upper","Upper","Upper","Upper",
                             "GI tract",
                                 "Lower","Lower","Lower",
                        "Bleeding",
                             "Mesentery",
                                 "Trauma","Trauma",
                        "Bleeding",
                             "Solid organ",
                                 "Liver",
                             "Solid organ",
                                 "Spleen",
                             "Solid organ",
                                 "Kidney",
                        "Bleeding",
                             "Vascular",
                    
                    "Surgical Abdomen",  
                        "Ischaemia",
                        "Ischaemia",
                
                    "Surgical Abdomen",  
                            "Obstruction",
                                "Bile duct","Bile duct",
                            "Obstruction", 
                                "Small bowel",
                                "Small bowel",
                                    "Hernia",
                                         "Groin",
                                         "Groin",
                                             "Inguinal",
                                             "Inguinal",
                                         "Groin",
                                    "Hernia",
                                        "Internal hernia","Internal hernia",
                                    "Hernia",
                                         "Ventral","Ventral",
                                "Small bowel",
                                    "Blockage",
                                
                             "Obstruction",
                                "Colonic","Colonic",
                             "Obstruction",
                                "Gastric","Gastric",
                             "Obstruction",
                                "Urinary","Urinary",
                             "Obstruction",
                                 "Rectum",
                            
                    "Surgical Abdomen",  
                        "Peritonitis",
                            "Appendicitis",
                            "Appendicitis",
                        "Peritonitis",
                            "Colitis",
                            "Colitis",
                            "Colitis",
                            "Colitis",
                        "Peritonitis",
                            "Gallbladder",
                            "Gallbladder",
                        "Peritonitis",
                            "Pancreatitis",
                            "Pancreatitis",
                        "Peritonitis",
                            "Perforation",
                                "Upper GI","Upper GI","Upper GI",
                            "Perforation",
                                "Lower GI","Lower GI","Lower GI","Lower GI",
                ],
    
        branchvalues="total",
        maxdepth=3,
        insidetextorientation='radial'
    ))

    fig2.update_layout(
    margin = dict(t=10, l=0, r=0, b=0))

    st.write(fig2)
    st.write("#")
    st.write("#")

    components.html(
        """
        <div style="text-align: center; font-family:sans-serif; font-size: 20px">Non-Specific Abdominal Pain - Categories</div>
        """,
        height=35,
    )

    fig3 = go.Figure(go.Sunburst(
              labels=
            [ "Non-Surgical Abdomen", 
                "GI tract", 
                    "Coeliac",
                    "Diverticulitis",
                    "Functional GI",
                        "Functional abdo pain synd.",
                        "Functional dyspepsia",
                        "IBS",
                    "Gallstones",
                    "Gastroenteritis",
                    "Peptic ulcer dis.",
                        "H. Pylori",
                        "Non-HP",
                    "IBD",   
                
                "Gynaecology", 
                    "Endometriosis",
                    "Ovarian",
                    "PID",
                  
                "Haematological", 
                    "Sickle Cell","Lymphoma", 
                 
                "Malignancy", 
                    "Pancreatic Ca",
                    "Neuroendocrine",
                    "Stomach Ca",
                    "Ovarian Ca","Liver mets",
                     
                "Metabolic",
                    "Hypercalcaemia",

                "Urinary",
                    "Infection",
                
                "Musculoskeletal",
                   
                "Ischaemia",
                   "Mesenteric angina",
                   "Solid organ",
         
                "Non-Specific AP",
            
               ],
    
        parents=[ "",    
                    "Non-Surgical Abdomen",  
                        "GI tract",
                        "GI tract",
                        "GI tract",
                             "Functional GI",
                             "Functional GI",
                             "Functional GI",
                        "GI tract",
                        "GI tract",
                        "GI tract",
                             "Peptic ulcer dis.",
                             "Peptic ulcer dis.",
                        "GI tract",
                  
                    "Non-Surgical Abdomen",  
                        "Gynaecology",
                        "Gynaecology",
                        "Gynaecology",
                 
                    "Non-Surgical Abdomen",  
                         "Haematological",
                         "Haematological",
                       
                    "Non-Surgical Abdomen",  
                        "Malignancy",
                        "Malignancy",
                        "Malignancy",
                        "Malignancy",
                        "Malignancy",
                    
                    "Non-Surgical Abdomen",  
                        "Metabolic",
                 
                    "Non-Surgical Abdomen",  
                        "Urinary",

                    "Non-Surgical Abdomen",  
                        
                 
                    "Non-Surgical Abdomen",  
                        "Ischaemia",
                        "Ischaemia",
                    
                    "Non-Surgical Abdomen",
                 
                ],
    
        branchvalues="total",
        maxdepth=3,
        insidetextorientation='radial'
    ))

    fig3.update_layout(
    margin = dict(t=10, l=0, r=0, b=0))

    st.write(fig3)
    st.write("#")

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
        autosize=False, height=600,
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
        autosize=False, height=600,
    )

    st.write(fig_gb)
    st.write('''<br>Surg-Flow | Copyright © 2022 Excision Ltd | All rights reserved''', unsafe_allow_html=True)
    

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  GI Obstruction (4)                                                                                    #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_obstruct():
    st.title('''Obstructed patients''')
    st.write(
        '''Click and drag elements of the Sankey diagram to best see how parts of the pathway communicate. 
        '''
        )

    url = 'https://raw.githubusercontent.com/HayesAJ83/EGS/main/Data/sankey_Obs22.json'   #https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
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
        autosize=False, height=600,
    )

    st.write(fig_gb)
    st.write('''<br>Surg-Flow | Copyright © 2022 Excision Ltd | All rights reserved''', unsafe_allow_html=True)
    

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  RIF (5)                                                                                    #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_RIF():
    st.title('''RIF pain patients''')
    st.write(
        '''Click and drag elements of the Sankey diagram to best see how parts of the pathway communicate. 
        '''
        )

    url = 'https://raw.githubusercontent.com/HayesAJ83/EGS/main/Data/sankey_RIF19.json'   #https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
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



#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Flow (6)                                                                                    #
# ::: Handles the                                                                                             #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_networkflowcurve():
    st.title('''Network Flow - Curved connectors''')
    components.html(
        """
        <head>
            <style> body { margin: 5; } </style>

            <script src="//unpkg.com/force-graph"></script>
            <!--<script src="../../dist/force-graph.js"></script>-->
        </head>

        <body>
            <div id="graph"></div>

            <script>
                const gData = {

                nodes: [...Array(9).keys()].map(i => ({ id: i })),
                
                links: [
                    { source: 1, target: 4, curvature: 0,    "value": 1 },
                    { source: 1, target: 4, curvature: 0.5,  "value": 2 },
                    { source: 1, target: 4, curvature: -0.5, "value": 5 },
                    { source: 5, target: 2, curvature: 0.3,  "value": 2 },
                    { source: 2, target: 5, curvature: 0.3,  "value": 6 },
                    { source: 0, target: 3, curvature: 0,    "value": 7 },
                    { source: 3, target: 3, curvature: 0.5,  "value": 3 },
                    { source: 0, target: 4, curvature: 0.2,  "value": 2 },
                    { source: 4, target: 5, curvature: 0.5,  "value": 1 },
                    { source: 5, target: 6, curvature: 0.7,  "value": 2 },
                    { source: 6, target: 7, curvature: 1,    "value": 8 },
                    { source: 7, target: 8, curvature: 2,    "value": 5 },
                    { source: 8, target: 0, curvature: 0.5,  "value": 1 }
                ]
                };

                const Graph = ForceGraph()
                (document.getElementById('graph'))
                    .linkDirectionalParticles("value")
                    .linkCurvature('curvature')
                    .graphData(gData);
            </script>
        </body>
        """, 
        height=500,
    )
   
    st.write('''<br>Surg-Flow | Copyright © 2022 Excision Ltd | All rights reserved''', unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Flow (7)                                                                                    #
# ::: Handles the                                                                                             #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_networkflow():
    st.title('''Network Flow''')
    st.info(
        """
            Grab the large dots to pull them apart. This is experimental and actively under development.
        """
        )
    components.html(
        """
        <head>
            <style> body { margin: 10; } </style>
            <script src="//unpkg.com/force-graph"></script>
            <!--<script src="../../dist/force-graph.js"></script>-->
        </head>

        <body>
            <div class="row justify-content-center">
                <div id="graph"></div>
            </div>

            <script>
                fetch("https://raw.githubusercontent.com/HayesAJ83/EGS/main/Data/networkflow.json").then(res => res.json()).then(data => {
                const Graph = ForceGraph()
                (document.getElementById('graph'))
                    .graphData(data)
                    .nodeLabel('id')
                    .linkCurvature('curvature')
                    .nodeAutoColorBy('group')
                    .linkDirectionalParticles("value")
                    .linkDirectionalParticleSpeed(d => d.value * 0.001);
                
                    .onEngineStop(() => Graph.zoomToFit(400));

                });
            </script>
        </body>

        """, 
        height=350, width=500,
    )

    components.html(
        """
        <head>
            <style> body { margin: 10; } </style>
            <script src="//unpkg.com/force-graph"></script>
            <!--<script src="../../dist/force-graph.js"></script>-->
        </head>

        <body>
            <div class="row justify-content-center">
                <div id="graph1"></div>
            </div>

            <script>
                fetch("https://raw.githubusercontent.com/HayesAJ83/EGS/main/Data/networkflow.json").then(res => res.json()).then(data => {
                const Graph = ForceGraph()
                (document.getElementById('graph1'))
                    .graphData(data)
                    .nodeId('id')
                    .linkCurvature('curvature')
                    .nodeAutoColorBy('group')
                 
                    .nodeCanvasObject((node, ctx, globalScale) => {
                    const label = node.id;
                    const fontSize = 12/globalScale;
                    ctx.font = `${fontSize}px Sans-Serif`;
                    const textWidth = ctx.measureText(label).width;
                    const bckgDimensions = [textWidth, fontSize].map(n => n + fontSize * 0.2); // some padding

                    ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                    ctx.fillRect(node.x - bckgDimensions[0] / 2, node.y - bckgDimensions[1] / 2, ...bckgDimensions);

                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    ctx.fillStyle = node.color;
                    ctx.fillText(label, node.x, node.y);

                    node.__bckgDimensions = bckgDimensions; // to re-use in nodePointerAreaPaint
                    })
                    .nodePointerAreaPaint((node, color, ctx) => {
                    ctx.fillStyle = color;
                    const bckgDimensions = node.__bckgDimensions;
                    bckgDimensions && ctx.fillRect(node.x - bckgDimensions[0] / 2, node.y - bckgDimensions[1] / 2, ...bckgDimensions);
                    });

                Graph.d3Force('center', null);

                // fit to canvas when engine stops
                Graph.onEngineStop(() => Graph.zoomToFit(400));
                });
            </script>
        </body>

        """, 
        height=350, width=500,
    )

    st.write('''<br>Surg-Flow | Copyright © 2022 Excision Ltd | All rights reserved''', unsafe_allow_html=True)
    
#-------------------------------------------------------------------------------------------#

main()

#if __name__ == "__main__":
#    main()
