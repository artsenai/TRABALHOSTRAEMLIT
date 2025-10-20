# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 18:50:28 2025

@author: LAB-08
"""

#    streamlit run TRB.py
   



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = None

aba1, aba2, aba3 = st.tabs(['INICIO','ENTRADA E SAIDA DE DADOS','DADOS DE PRUDUÇAO'])
                           
                           
                           
with aba1:
    st.title('AMBEV')
    st.write('RUTULOS')
    


with aba2:
    st.title('entrada e saida de dados')
    
    dados = st.file_uploader('carregar dados')
    if dados is not None:
        df = pd.read_csv(dados,decimal='.')
        st.success('dados carregados!')
    else:
        df =[]
        
    st.dataframe(df)
    st.header('novos dados')


    FORMULARIO = st.form('formulario')
    FORMULARIO.subheader('produçao diaria de rotulos por maquina')
    
    
    DT = FORMULARIO.date_input('data do dia:')
 
    PDPM1 = FORMULARIO.text_input("PRUDUÇAO  MAQUINA 1:")
    PDPM2 = FORMULARIO.text_input("PRUDUÇAO  MAQUINA 2:")
    PDPM3 = FORMULARIO.text_input("PRUDUÇAO  MAQUINA 3:")
    RB = FORMULARIO.text_input("ROTULOS BONS:")
    RR = FORMULARIO.text_input("ROTULOS RUINS:")
    
    MCP = FORMULARIO.text_input("ALGUMA MAQUINA COM PROBLEMA:")

    bt1 = FORMULARIO.form_submit_button('enviar')
    if bt1:
        novo = {'data do dia:': [DT],
                'PRODUÇAO  MAQUINA 1:': [PDPM1],
                'PRODUÇAO  MAQUINA 2:': [PDPM2],
                'PRODUÇAO  MAQUINA 3:': [PDPM3],
                'ROTULOS BONS:': [RB],
                'ROTULOS RUINS:': [RR],
                'ALGUMA MAQUINA COM PROBLEMA:': [MCP]
                #'idade': [int(nova_idade)]
                }
        
        
        
        x = pd.DataFrame(novo)
        DF = pd.concat([df,x],ignore_index= True)
        st.dataframe(DF)
        DF.to_csv('C:/Users/LAB-08/Desktop/WPy64-31241/artin streamlit/banco_TRB.csv',index = False)
        
     
        
with aba3:
    if df is not None:
        m1_prod = df['PRODUÇAO  MAQUINA 1:']
        m2_prod = df['PRODUÇAO  MAQUINA 2:']
        m3_prod = df['PRODUÇAO  MAQUINA 3:']
        
        rb = df['ROTULOS BONS:']
        rr = df['ROTULOS RUINS:']
        
        mcp = df['ALGUMA MAQUINA COM PROBLEMA:']
        
        dia = df['data do dia:']
        
        
        
        
        #st.write(m1_prod)
        # st.write(m1_dia)
        # st.write(m2_prod)
       
        
       
        st.title('produçao maquina 1')
       
        fig, ax = plt.subplots()
        ax.scatter(dia,m1_prod)
        st.pyplot(fig)
        
        st.title('produçao maquina 2')
        
        fig, ax = plt.subplots()
        ax.scatter(dia,m2_prod)
        st.pyplot(fig)
        
        
        st.title('produçao maquina 3')
        
        fig, ax = plt.subplots()
        ax.scatter(dia,m3_prod)
        st.pyplot(fig)
        
        st.title('rotulos bons')
        
        fig, ax = plt.subplots()
        ax.scatter(dia,rb)
        st.pyplot(fig)
        
        st.title('rotulos ruins')
        
        fig, ax = plt.subplots()
        ax.scatter(dia,rr)
        st.pyplot(fig)
        
        st.title('maquina com problema')
        
        fig, ax = plt.subplots()
        ax.scatter(dia,mcp)
        st.pyplot(fig)