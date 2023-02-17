from git import Repo
import os
import pandas as pd
from matplotlib import pyplot as plot
import streamlit as st
import json
import plotly.express as px


#Repo.clone_from("https://github.com/PhonePe/pulse.git", "Phonepe data visulaisation")


def Agg_page():

    st.markdown("# Aggregate Transaction India ")
    st.sidebar.markdown("# Aggregate Transaction India ")

    # Once created the clone of GIT-HUB repository then,
    # Required libraries for the program

    st.subheader('Aggregated Transaction data Overview:')



    import os

    # Define the Path where file has stored

    path1 = "C:/Users/DELL/Desktop/Phonepe data visulaisation/Phonepe data visulaisation/data/aggregated/transaction/country/india/state/"
    Agg_state_list = os.listdir(path1)


    # This is to extract the data's to create a dataframe

    clm = {'State': [], 'Year': [], 'Quater': [], 'Transacion_type': [], 'Transacion_count': [],
           'Transacion_amount': []}
    for i in Agg_state_list:
        p_i = path1 + i + "/"
        Agg_yr = os.listdir(p_i)
        for j in Agg_yr:
            p_j = p_i + j + "/"
            Agg_yr_list = os.listdir(p_j)
            for k in Agg_yr_list:
                p_k = p_j + k
                Data = open(p_k, 'r')
                D = json.load(Data)
                for z in D['data']['transactionData']:
                    Name = z['name']
                    count = z['paymentInstruments'][0]['count']
                    amount = z['paymentInstruments'][0]['amount']
                    clm['Transacion_type'].append(Name)
                    clm['Transacion_count'].append(count)
                    clm['Transacion_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
    # Succesfully created a dataframe
    pd.DataFrame(clm)
    Agg_Trans_Ind = pd.DataFrame(clm)
    st.dataframe(Agg_Trans_Ind)

    #plotting a Graph
    agg_totl_amount = Agg_Trans_Ind.groupby('State')['Transacion_amount'].mean()
    agg_totl_amountgraph = agg_totl_amount.plot.bar('State', 'Transacion_amount', rot=90)
    st.bar_chart(agg_totl_amount)
    st.caption("plotting a bar graph with by taking overal mean of transaction amount and type")
    Agg_Trans_bar_graph = Agg_Trans_Ind.groupby('Transacion_type')['Transacion_count'].mean()
    fig1 = Agg_Trans_bar_graph.plot.bar('Transacion_type', 'Transacion_count', rot=90)
    st.bar_chart(Agg_Trans_bar_graph)
    #plotting pie chart
    #i have been yoused multiple keys so i am plotting directly.
    #user_df1 = Agg_Trans_Ind[(Agg_Trans_Ind['State'] == 'chhattisgarh') & (Agg_Trans_Ind['Year'] == 2018)]
    #Agg_Trans_graph = px.pie(user_df1['Transacion_type'], user_df1['Transacion_count'],
                             #title='Types of transaction in chhattisgarh State wise:')
    #st.plotly_chart(Agg_Trans_graph)

    #input_col, pie_col = st.columns(2)

    # top_n = input_col.text_input ('how many of the top  you want to see?',10)
    # fig4= px.pie(user_df1['Transacion_type'], user_df1['Transacion_count'],
    #                          title='Types of transaction in chhattisgarh State wise:')
    # pie_col.write(fig4, use_container_width=True)
    st.caption('for pie chart i am converting the dataframe in to csv')
    st.caption('when plotting pie graph from dataframe, not able to see image and converted to suitable format to read pie chart ')
    Agg_Trans_Ind['State'] = Agg_Trans_Ind['State'].str.title()
    Agg_df_state = Agg_Trans_Ind[(Agg_Trans_Ind['State'] == 'Chhattisgarh') & (Agg_Trans_Ind['Year'] == '2018')]
    pd.DataFrame(Agg_df_state)
    Agg_df_state.to_csv('Agg_df_state2018.csv')
    Agg_df_state = Agg_Trans_Ind[(Agg_Trans_Ind['State'] == 'Lakshadweep') & (Agg_Trans_Ind['Year'] == '2019')]
    pd.DataFrame(Agg_df_state)
    Agg_df_state.to_csv('Agg_df_state2019.csv')
    Y = st.selectbox('Select the Year', ('2018', '2019'))
    if Y == '2018':
        s = pd.read_csv('Agg_df_state2018.csv')
        pie = px.pie(s['Transacion_type'], s['Transacion_count'],
                     title='Types of transaction in chhattisgarh State wise:')
        st.plotly_chart(pie)
    elif Y == '2019' :
        s = pd.read_csv('Agg_df_state2019.csv')
        pie = px.pie(s['Transacion_type'], s['Transacion_count'],
                     title='Types of transaction in chhattisgarh State wise:')
        st.plotly_chart(pie)

def page2():

    path5 = "C:/Users/DELL/Desktop/Phonepe data visulaisation/Phonepe data visulaisation/data/top/transaction/country/india/state/"
    map_state_list = os.listdir(path5)

    # This is to extract the data's to create a dataframe
    clm = {'State': [], 'district': [], 'Year': [], 'Quarter': [], 'Metric_type': [], 'Metric_count': [],
           'Metric_amount': []}
    for i in map_state_list:
        p_i = path5 + i + "/"
        Agg_yrs = os.listdir(p_i)
        for j in Agg_yrs:
            p_j = p_i + j + "/"
            Agg_yrs_list = os.listdir(p_j)
            for k in Agg_yrs_list:
                p_k = p_j + k
                with open(p_k, 'r') as f:
                    data = json.load(f)
                    clm['district'].append(data['data']["districts"][0]['entityName'])
                    clm['Metric_type'].append(data['data']["districts"][0]['metric']['type'])
                    clm['Metric_count'].append(data['data']["districts"][0]['metric']['count'])
                    clm['Metric_amount'].append(data['data']["districts"][0]['metric']['amount'])
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))

    df_top_C = pd.DataFrame(clm)
    df_top_C['State'].value_counts()

    st.caption("Plotting the bar graph with selected columns: ")
    st.caption("Please enter the right column name check the dataframe")
    st.caption('By doing groupby and taking mean,plotting the bar graph')

    # print(df_top_C)
    df_top_C['State'] = df_top_C['State'].str.title()
    df_top_C['State'] = df_top_C['State'].replace({'Andhra-Pradesh': 'Andhra Pradesh',
                                                   "Madhya-Pradesh": 'Madhya Pradesh',
                                                   'Tamil-Nadu': 'Tamil Nadu',
                                                   'Andaman-&-Nicobar-Islands': 'Andaman & Nicobar Island',
                                                   'Delhi': 'NCT of Delhi',
                                                   'Dadra-&-Nagar-Haveli-&-Daman-&-Diu': 'Dadara & Nagar Havelli',
                                                   'Jammu-&-Kashmir': 'Jammu & Kashmir',
                                                   'Arunachal-Pradesh': 'Arunanchal Pradesh',
                                                   'Himachal-Pradesh': 'Himachal Pradesh',
                                                   'Uttar-Pradesh': 'Uttar Pradesh',
                                                   'West-Bengal': 'West Bengal'})

    df_top_C = df_top_C.drop([340, 341, 342, 343, 344, 345,
                              346, 347, 348, 349, 350,
                              351, 352, 353, 354, 355,
                              356, 357, 358, 359])
    import numpy as np
    df_top_C['Metric_countscale'] = np.log10(df_top_C['Metric_count'])

    # Now i am plotting the graph
    import plotly.express as px

    india_states = json.load(open("/Users/DELL/Desktop/Phonepe data visulaisation/Phonepe data visulaisation/states2_india .geojson", "r"))

    state_id_map = {}
    for feature in india_states['features']:
        feature['id'] = feature['properties']['state_code']
        state_id_map[feature['properties']['st_nm']] = feature['id']


    df_top_C['id'] = df_top_C['State'].apply(lambda x: state_id_map[x])

    fig = px.choropleth(df_top_C,
                        locations='id',
                        geojson=india_states,
                        color='Metric_countscale',
                        hover_name='State',
                        hover_data=['Metric_amount'],
                        title='Transactions')
    fig.update_geos(fitbounds='locations', visible=False)
    st.write(fig)

    #plotting overall count bar gropth for all the stated
    st.caption("Below graph we can see the overall Metric count for each state: ")
    #i am taking the mean for each state by taking Metric column
    dataset = df_top_C.groupby('State')['Metric_count'].mean()
    #state_graph = dataset.plot.bar('State', 'Metric_count', rot=90)
    st.bar_chart(dataset)



    State = st.text_input("enter state name: ")



    #creating the dataframe of specific states
    State_df1 = df_top_C[df_top_C['State'] == f'{State}']

    st.dataframe(State_df1)

    #Displaying the dataframe with Particular ##State## and Particular Year
    st.caption('Enter the year to display particular state data in particular year ')

    year = st.text_input("enter since Year: ")

    State_df2 = df_top_C[(df_top_C['State'] == f'{State}') & (df_top_C['Year'] == f'{year}')]

    st.dataframe(State_df2)

def page3():
    st.markdown("# Transaction by user ")
    st.sidebar.markdown("# Transaction by user ")

    st.subheader("Top Transaction Registered Users")


    # Extracting the data from pulse-->data-->top-->user-->country-->india-->state to see the transaction users
    path6 = "C:/Users/DELL/Desktop/Phonepe data visulaisation/Phonepe data visulaisation/data/top/user/country/india/state/"
    map_state_list = os.listdir(path6)

    # This is to extract the data's to create a dataframe
    clm = {'State': [], 'district': [], 'Year': [], 'Quarter': [], 'No of Regi_user': []}
    for i in map_state_list:
        p_i = path6 + i + "/"
        Agg_yrs = os.listdir(p_i)
        for j in Agg_yrs:
            p_j = p_i + j + "/"
            Agg_yrs_list = os.listdir(p_j)
            for k in Agg_yrs_list:
                p_k = p_j + k
                with open(p_k, 'r') as f:
                    data = json.load(f)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
                    clm['district'].append(data['data']['districts'][0]['name'])
                    clm['No of Regi_user'].append(data['data']['districts'][0]['registeredUsers'])
    top_user_df = pd.DataFrame(clm)
    st.dataframe(top_user_df)

    st.caption("Plotting overall registrered users bay using barplot")
    dataset = top_user_df.groupby('district')['No of Regi_user'].mean()
    #df_district = pd.DataFrame(dataset)
    user_graph = dataset.plot.bar('district', 'No of Regi_user', rot=90)
    plot.title("Totoal Registerged Users")
    st.bar_chart(dataset)
    # Change font so, it can match with geojson map
    # replace the state word those, doesn't match after changing the font

    top_user_df['State'] = top_user_df['State'].str.title()
    top_user_df['State'] = top_user_df['State'].replace({'Andhra-Pradesh': 'Andhra Pradesh',
                                                         "Madhya-Pradesh": 'Madhya Pradesh',
                                                         'Tamil-Nadu': 'Tamil Nadu',
                                                         'Andaman-&-Nicobar-Islands': 'Andaman & Nicobar Island',
                                                         'Delhi': 'NCT of Delhi',
                                                         'Dadra-&-Nagar-Haveli-&-Daman-&-Diu': 'Dadara & Nagar Havelli',
                                                         'Jammu-&-Kashmir': 'Jammu & Kashmir',
                                                         'Arunachal-Pradesh': 'Arunanchal Pradesh',
                                                         'Himachal-Pradesh': 'Himachal Pradesh',
                                                         'Uttar-Pradesh': 'Uttar Pradesh',
                                                         'West-Bengal': 'West Bengal'})

    #Need to match the index and geo map states these indexes are not matching,so dropping the follwing index
    top_user_df = top_user_df.drop([340, 341, 342, 343, 344, 345,
                              346, 347, 348, 349, 350,
                              351, 352, 353, 354, 355,
                              356, 357, 358, 359])



    import numpy as np
    top_user_df['No of Regi_user_scale'] = np.log10(top_user_df['No of Regi_user'])

    india_states = json.load(open('C:/Users/DELL/Desktop/Phonepe data visulaisation/states2_india.geojson', "r"))

    state_id_map = {}
    for feature in india_states['features']:
        feature['id'] = feature['properties']['state_code']
        state_id_map[feature['properties']['st_nm']] = feature['id']

    top_user_df['id'] = top_user_df['State'].apply(lambda x: state_id_map[x])

    fig = px.choropleth(top_user_df,
                        locations='id',
                        geojson=india_states,
                        color='No of Regi_user_scale',
                        hover_name='State',
                        title='Transactions_Users')
    fig.update_geos(fitbounds='locations', visible=False)

    Geo_Map = st.selectbox('View the Map',('0','1'))
    if Geo_Map == '1':
        fig.update_geos(fitbounds='locations', visible=False)
        st.write(fig)
