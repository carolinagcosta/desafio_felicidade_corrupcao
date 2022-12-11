import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
import statsmodels

# CORPO
## CORPO - Título da Aplicação
st.markdown("""
            # Projeto de Visualização de Dados 🔎
            ### *Análise sobre o efeito da corrupção na felicidade de pessoas ao redor do mundo.*
            ---
            
            O presente projeto tem como objetivo efetuar uma busca exploratória em uma base de dados que utiliza diversos fatores (variáveis) para calcular o índice mundial da felicidade.

            Projeto de cunho avaliativo, componente do quarto Módulo - Técnicas de Programação II, do programa **[Diversidade TECH](https://letscode.com.br/processos-seletivos/suzano-diversidade-tech)**, desenvolvido a partir de uma parceria entre a Let's Code by Ada e Suzano.
            
            O repositório do projeto pode ser encontrado neste link: **[GitHub](https://github.com/carolinagcosta/desafio_felicidade_corrupcao)**
            
            ---
            
            """)


## CORPO - Carregando o dataset
st.header('😁 Happiness based on cpi 💸')

df = pd.read_csv('hap_corrup.csv')

## CORPO - Info do dataset
with st.expander('Dados do Dataset'):
    st.header('Dados do Dataset')
    st.subheader('Primeiros registros')
    st.write(df.head())
    
    st.subheader('Colunas')
    st.markdown("""
                - __*Country*__: País abordado.
                - __*happiness_score*__: Média das respostas à pesquisa de índice de felicidade realizada pela Gallup World Poll (GWP) --> 0-10
                - __*gdp_per_capita*__: Influencia do PIB influencia no cálculo do índice de felicidade. 
                - __*family*__: Influência da família no cálculo do índice de felicidade.
                - __*health*__: Influência da expectativa de vida no cálculo do índice de felicidade.
                - __*freedom*__: Influência da liberdade no cálculo do índice de felicidade.
                - __*generosity*__: Um valor númerico baseado na percepção dos entrevistados em relação à generosidade no seu país.
                - __*government_trust*__: Influência da percepção da corrupção (confiança/Transparência) no cálculo do índice da felicidade. 
                - __*dystopia_residual*__: Índice baseado numa comparação hipotética com o país mais triste do mundo. 
                - __*continent*__: Continente do país. 
                """)
        
    st.subheader('Dados Faltantes')
    st.write(df.isna().sum()[df.isna().sum() > 0])

    st.subheader('Estatísticas Descritivas')
    st.write(df.describe())


## CORPO - Análise Univariada
st.header('Análise Univariada')
univar_campo =  \
    st.selectbox('Selecione o campo que deseja avaliar a distribuição:',
                 options=list((df.drop(columns='Year')).select_dtypes(include=np.number)))
    
# Adicionando análises para cada análise univariada.

if univar_campo == 'happiness_score':
    st.plotly_chart(px.histogram(data_frame=df, x=univar_campo))
    st.plotly_chart(px.box(data_frame=df, y=univar_campo))
    
    with st.expander("Análise da equipe"):
        st.write("""
            Verificamos que o score de felicidade apresenta mediana de 5.5. A maior parte dos dado está próximo a média. 
            
            Os menores scores são valores entre 2 e 3 e os mais altos scores chegam próximo a 8.
        """)

elif univar_campo == 'gdp_per_capita':
    st.plotly_chart(px.histogram(data_frame=df, x=univar_campo))
    st.plotly_chart(px.box(data_frame=df, y=univar_campo))
    
    with st.expander("Análise da equipe"):
        st.write("""
            Nesta análise univariada verificamos Produto Interno Bruto per capita, que varia de 0 a 2.1 possui mediana igual a 1.  
            
            Podemos visualmente verificar que 75% dos países apresentam gdp menor que 1.25
        """)

elif univar_campo == 'family':
    st.plotly_chart(px.histogram(data_frame=df, x=univar_campo))
    st.plotly_chart(px.box(data_frame=df, y=univar_campo))
    
    with st.expander("Análise da equipe"):
        st.write("""
            Na origem dos dados do dataframe, a pessoa responsável preencheu os vazios com "0",. Logo escolhemos desconsiderar a variável "família" da análise pela grande massa de vazios.
        """)
        
elif univar_campo == 'health':
    st.plotly_chart(px.histogram(data_frame=df, x=univar_campo))
    st.plotly_chart(px.box(data_frame=df, y=univar_campo))
    
    with st.expander("Análise da equipe"):
        st.write("""
            Nesta análise verificamos que a a expectativa de vida das pessoas apresenta score mediano de 0.7. A maioria dos dados estão concentrados entre 0.5 e 0.8.
        """)

elif univar_campo == 'freedom':
    st.plotly_chart(px.histogram(data_frame=df, x=univar_campo))
    st.plotly_chart(px.box(data_frame=df, y=univar_campo))
    
    with st.expander("Análise da equipe"):
        st.write("""
            Neste inicie de liberdade, que varia entre 0 e chega próximo a 0.8 a mediana é por volta de 0.45.
            
            A maioria dos dados (até terceiro quartil) está próximo de 0.55
        """)

elif univar_campo == 'government_trust':
    st.plotly_chart(px.histogram(data_frame=df, x=univar_campo))
    st.plotly_chart(px.box(data_frame=df, y=univar_campo))
    
    with st.expander("Análise da equipe"):
        st.write("""
            A partir deste gráfico, podemos observar que a confiança no governo pode variar de 0 a 0.5. 
            
            Constatamos mais de 75% dos dados estão avaixo de 0.2. Países com alta confiança no governo são outliers.
        """)
        
elif univar_campo == 'generosity':
    st.plotly_chart(px.histogram(data_frame=df, x=univar_campo))
    st.plotly_chart(px.box(data_frame=df, y=univar_campo))
    
    with st.expander("Análise da equipe"):
        st.write("""
                Embora a percepção da generosidade seja uma variável sem grandes problemas na massa de dados, notamos em uma análise prévia que a mesma não influencia tanto no Índice de felicidade, sendo descartada nas análises a seguir.
        """)

elif univar_campo == 'cpi_score':
    st.plotly_chart(px.histogram(data_frame=df, x=univar_campo))
    st.plotly_chart(px.box(data_frame=df, y=univar_campo))
    
    with st.expander("Análise da equipe"):
        st.write("""
            Neste indice de percepção de corrupção, um indicativo de coorrupção nos países, podemos verificar que p score varia de 10 a 90.
            
            Quanto maior o score menos corrupto o governo é percebido e quanto menor o score, mais corrupto é o governo
            
            A mediana desta medida está próximo de 40, e mais de 75% dos dados está abaixo de 60.
        """)
        
elif univar_campo == 'dystopia_residual' or univar_campo == 'social_support':
    st.plotly_chart(px.histogram(data_frame=df, x=univar_campo))
    st.plotly_chart(px.box(data_frame=df, y=univar_campo))
    
    with st.expander("Análise da equipe"):
        st.write("""
            Neste indice notamos o mesmo problema do índice familiar, logo, decidimos desconsiderá-lo.
        """)

## CORPO - Análise Bivariada
st.header('Análise Bivariada')
st.subheader('Análise temporal')
st.write('Decidimos abordar algumas análises de variáveis em relação ao tempo (anual)')
bivar_option = \
    st.selectbox('Escolha uma variável:',
            options=['happiness_score', 'gdp_per_capita', 'health', 'freedom'])

### CORPO - Análise Bivariada - Análise temporal
if bivar_option == 'happiness_score':
    x_line = df.groupby('Year')['happiness_score'].mean().index
    y_line = df.groupby('Year')['happiness_score'].mean().values 
    fig = px.line(data_frame=df, 
                x=x_line,
                y=y_line,
                markers=True)
    fig.update_layout(
        xaxis_title={
            'text': 'Ano',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Média do Índice de felicidade',
            'font_size': 14,
            'font_color': 'white'
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Média do Índice de felicidade por Ano',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
    )       
    st.plotly_chart(fig)
    with st.expander("Análise da equipe"):
        st.write("""
            Neste gráfico, verificamos a média anual de felicidade no mundo. Verificamos que a média de felicidade anual se mantém estável de 2015 a 2020, apresentando variação mínima.
        """)

elif bivar_option == 'gdp_per_capita':
    x_line = df.groupby('Year')['gdp_per_capita'].mean().index
    y_line = df.groupby('Year')['gdp_per_capita'].mean().values
    fig = px.line(data_frame=df, 
                x=x_line,
                y=y_line,
                markers=True)
    fig.update_layout(
        xaxis_title={
            'text': 'Ano',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Média do Índice do PIB',
            'font_size': 14,
            'font_color': 'white'
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Média do Índice do PIB por Ano',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
    )        
    st.plotly_chart(fig)
    with st.expander("Análise da equipe"):
        st.write("""
            Neste gráfico, é possível verificar uma queda do PIB per capita de 2015 a 2016, possivelmente reflexo da crise econômica mundial em 2016, e sua subsequente lenta recuperação nos demais anos analisados.
        """)
        
elif bivar_option == 'health':
    fig = px.histogram(data_frame=df, 
                x='Year',
                y='health',
                histfunc='avg',
                color='Year')
    fig.update_layout(
        xaxis_title={
            'text': 'Ano',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Média do Índice de estimativa de vida',
            'font_size': 14,
            'font_color': 'white'
        },
        legend_title={
        'text': 'Anos',
        'font_color': 'white',
        'font_size': 12
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Média do Índice de estimativa de vida por Ano',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
    )   
    st.plotly_chart(fig)
    with st.expander("Análise da equipe"):
        st.write("""
            Neste gráfico podemos verificar a estimativa de vida das pessoas ao longo de cinco anos. A estimativa média de 2017 e 2020 foram as maiores.
        """)

elif bivar_option == 'freedom':
    x_line = df.groupby('Year')['freedom'].mean().index
    y_line = df.groupby('Year')['freedom'].mean().values
    line = px.line(data_frame=df, 
                x=x_line,
                y=y_line,
                markers=True)
    line.update_layout(
        xaxis_title={
            'text': 'Ano',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Média do Índice de Liberdade',
            'font_size': 14,
            'font_color': 'white'
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Média do Índice de Liberdade por Ano',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
    )       
    st.plotly_chart(line)
    with st.expander("Análise da equipe"):
        st.write("""
            A sensação de liberdade em 2019 apresentou uma queda. Segundo pesquisa realizada no "The Global Expression Report 2019/2020", a principal causa para as pessoas terem essa percepção foi devido ao início da pandemia no final deste ano. No final de 2019, muitos governos, como medida essencial para conter a propagação do vírus, proibiram seus cidadões de circular livremente nas ruas, o que afetou esta percepção das pessoas. Apesar de ter sido uma medida necessária, muitos governos autoritários usaram esta crise de saúde como um pretexto para controlar a liberdade de expressão nas ruas e mídias online.
        """)


st.subheader('Análise Geográfica')
st.write('E algumas análises relacionadas ao continente.')
bivar2_option = \
    st.selectbox('Escolha uma variável:',
            options=['government_trust', 'cpi_score'])
    
if bivar2_option == 'government_trust': 
    fig = px.histogram(data_frame=df, 
                x='continent',
                y='government_trust',
                histfunc='avg',
                color='continent')
    fig.update_layout(
        xaxis_title={
            'text': 'Continente',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Média do Índice de confiança no Governo',
            'font_size': 14,
            'font_color': 'white'
        },
        legend_title={
        'text': 'Continentes',
        'font_color': 'white',
        'font_size': 12
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Média do Índice de confiança no Governo por Continente',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
    )  
    st.plotly_chart(fig)
    with st.expander("Análise da equipe"):
        st.write("""
            Neste gráfico Verificamos na Oceania, onde se localiza a Austrália, é o local onde há maior confiança no governo. Em seguida temos a América do Norte e a Europa. Os países da América do Sul são os que apresentam menor confiança no governo.
        """)

if bivar2_option == 'cpi_score':
    fig = px.histogram(data_frame=df, 
                x='continent',
                y='cpi_score',
                histfunc='avg',
                color='continent')
    fig.update_layout(
        xaxis_title={
            'text': 'Continente',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Média do Índice de percepção da corrupção',
            'font_size': 14,
            'font_color': 'white'
        },
        legend_title={
        'text': 'Continentes',
        'font_color': 'white',
        'font_size': 12
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Média do Índice de percepção da corrupção por Continente',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
    )   
    st.plotly_chart(fig)
    with st.expander("Análise da equipe"):
        st.write("""
                A partir deste dado podemos verificar que nos continentes da Austrália, a América do Norte e Europa são percebidos como menos corruptos. Da mesma forma, Os paíeses da América do Sul, África e Asia, possuem governos percebidos como mais corruptos.
            """)

### CORPO - Análise Multivariada - Análise temporal        
st.header('Análise Multivariada')

multivar_option = \
        st.radio('Selecione um gráfico:',
                options=['linha', 'dispersão'])
        
if multivar_option == 'linha':
    df_mean=df.groupby(['continent','Year'])['happiness_score'].mean().reset_index()
    fig = px.line(data_frame=df_mean,
                  x='Year', 
                  y='happiness_score', 
                  color='continent'
    )
    fig.update_layout(
        xaxis_title={
            'text': 'Continente',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Média do Índice de felicidade',
            'font_size': 14,
            'font_color': 'white'
        },
        legend_title={
        'text': 'Continentes',
        'font_color': 'white',
        'font_size': 12
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Média do Índice de felicidade continental por Ano',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
    )   
    
    st.plotly_chart(fig)
    with st.expander("Análise da equipe"):
        st.write("""
                De acordo com a base de dados, o continente mais feliz é a Australia (Oceania) e o menos feliz é a África. Esses scores parecem se manter estáveis ao longo do tempo.
            """)

elif multivar_option == 'dispersão':
    multivar_campo =  \
    st.selectbox('Selecione o campo que deseja avaliar a distribuição:',
                 options=['gdp_per_capita', 'health', 'freedom', 'government_trust', 'cpi_score'])
            
    if multivar_campo == 'gdp_per_capita':
        fig = px.scatter(data_frame=df, x='gdp_per_capita', y='happiness_score', color='continent', trendline='ols', width=750, height=540)
        fig.update_layout(
        xaxis_title={
            'text': 'Índice do PIB',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Índice da felicidade',
            'font_size': 14,
            'font_color': 'white'
        },
        legend_title={
        'text': 'Continentes',
        'font_color': 'white',
        'font_size': 12
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Relação dos Índices PIB e Felicidade por Continente',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
        )      
        st.plotly_chart(fig)
        with st.expander("Análise da equipe"):
            st.write("""
                Aqui conseguimos identificar correlações positivas. Quanto maior o PIB maior a felicidade das pessoas.
                
                Na Europa, temos o mínimo de gdp_per_capita já mais elevado que os demais continentes. 
                
                Na África, uma maior gdp_per_capita não parece influenciar no grau de felicidade 
            """)
        
    elif multivar_campo == 'health':
        fig = px.scatter(data_frame=df, x='health', y='happiness_score', color='continent', trendline='ols', width=750, height=540)
        fig.update_layout(
        xaxis_title={
            'text': 'Índice de Qualidade de vida',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Índice da felicidade',
            'font_size': 14,
            'font_color': 'white'
        },
        legend_title={
        'text': 'Continentes',
        'font_color': 'white',
        'font_size': 12
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Relação dos Índices Qualidade de Vida e Felicidade por Continente',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
        )    
        st.plotly_chart(fig)
        with st.expander("Análise da equipe"):
            st.write("""
                No geral, podemos perceber que quanto maior a expectativa de vida, mais as pessoas são felizes. É interessante observar que continentes com maior índice de felicidade têm maior índice de saúde. Entretanto, o aumento, ainda que pequeno, nas condições de saúde na África não parece impactar a felicidade. 
                
                Esses dados fazem crer que é necessário ter um índice mínimo de saúde para que ocorra impacto na felicidade.
            """)
        
    elif multivar_campo == 'freedom':
        fig = px.scatter(data_frame=df, x='freedom', y='happiness_score', color='continent', trendline='ols', width=750, height=540)
        fig.update_layout(
        xaxis_title={
            'text': 'Índice de Liberdade',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Índice da felicidade',
            'font_size': 14,
            'font_color': 'white'
        },
        legend_title={
        'text': 'Continentes',
        'font_color': 'white',
        'font_size': 12
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Relação dos Índices Liberdade e Felicidade por Continente',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
        )    
        st.plotly_chart(fig)
        with st.expander("Análise da equipe"):
            st.write("""
                Neste gráfico podemos verificar que, no geral, quanto mais liberdade mais felizes são as pessoas. No continente africano, com baixo score de felicidade, e na Austrália, com alto score de felicidade, verificamos que essa correlação é neutra
            """)
        
    elif multivar_campo == 'government_trust':
        fig = px.scatter(data_frame=df, x='government_trust', y='happiness_score', color='continent', trendline='ols', width=750, height=540)
        fig.update_layout(
        xaxis_title={
            'text': 'Índice de Confiança no Governo',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Índice da felicidade',
            'font_size': 14,
            'font_color': 'white'
        },
        legend_title={
        'text': 'Continentes',
        'font_color': 'white',
        'font_size': 12
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Relação dos Índices Confiança no Governo e Felicidade por Continente',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
        )    
        st.plotly_chart(fig)
        with st.expander("Análise da equipe"):
            st.write("""
                Aqui conseguimos ver que essa não é uma relação absoluta. 
                
                Na América do Sul, a confiança no governo é baixa, mas o score de felicidade varia bastante, ocupando patamares altos. 
                Já na África, nos locais onde a confiança no governo é mais alta, o score de felicidade continua baixo, havendo uma correlação negativa.
            """)
        
    elif multivar_campo == 'cpi_score':
        fig = px.scatter(data_frame=df, x='cpi_score', y='happiness_score', color='continent', trendline='ols', width=750, height=540)
        fig.update_layout(
        xaxis_title={
            'text': 'Índice de Percepção da Corrupção',
            'font_size': 14,
            'font_color': 'white'
        },
        yaxis_title={
            'text': 'Índice da felicidade',
            'font_size': 14,
            'font_color': 'white'
        },
        legend_title={
        'text': 'Continentes',
        'font_color': 'white',
        'font_size': 12
        },
        font_color='grey',
        font_size=10,
        title={
            'text': 'Relação dos Índices Percepção da Corrupção e Felicidade por Continente',
            'font_family': 'Verdana',
            'font_color': 'white',
            'font_size': 16
        },
        template='presentation'
        )    
        st.plotly_chart(fig)
        with st.expander("Análise da equipe"):
            st.write("""
                É possível perceber que esta é uma relação positiva na maioria dos continentes. 
                
                Quanto maior o score de CPI, ou seja, menos corrupto o governo aparenta ser, mais as pessoas são felizes. Já na África, nos locais onde o índice de CPI é mais alta, o score de felicidade continua baixo.
            """)

st.markdown("""
            ---
            ## Conclusões Finais
            """)

with st.expander('Conclusões Finais'):
    st.write("""
            Neste estudo verificamos que diversos fatores, como PIB per capita, expectativa de vida, liberdade, confiança no governo e a perceção de ausência ou baixa corrupção no governo impactam diretamente na felicidade das pessoas.

            Verificamos que mesmo em países com menor corrupção e mais confiança no governo, se não há PIB per capita alto, boa expectativa de vida e liberdade de expressão, as pessoas não são felizes.

            Desta forma, concluímos que a corrupção impacta na felicidade das pessoas, embora diversas variáveis relacionadas a qualidade de vida são essenciais para atingir a felicidade.
            """)
    
