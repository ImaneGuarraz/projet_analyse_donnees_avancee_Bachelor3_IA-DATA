import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

# CHARGEMENT DES DONNÉES

df = pickle.load(open("df.pkl", "rb"))

# CONFIGURATION

st.set_page_config(page_title="Dashboard Marketing", layout="wide")
st.title("Dashboard Marketing – Segmentation & KPI")
st.markdown("Dashboard décisionnel basé sur la segmentation client et les KPI marketing.")

# VUE SYNTHÉTIQUE

st.header("Vue synthétique du portefeuille clients")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Nombre total de clients", len(df))
col2.metric("Dépense moyenne (€)", round(df["Total_Spending"].mean(), 1))
col3.metric("Taux de réponse global", f"{round(df['Response'].mean()*100,1)} %")
col4.metric("Score de valeur moyen", round(df["Score_Valeur"].mean(), 1))

seg_counts = df["Segment"].value_counts().sort_index()
fig_pie = px.pie(values=seg_counts.values, names=seg_counts.index,
                 title="Répartition des segments")
st.plotly_chart(fig_pie, use_container_width=True)

# VUE SEGMENTATION

st.header("🧩 Vue segmentation")

# Sélection des colonnes numériques uniquement
num_cols = df.select_dtypes(include="number").columns

seg_profile = df.groupby("Segment")[num_cols].mean().round(1)

st.subheader("Profil moyen par segment")
st.dataframe(seg_profile)

fig_heatmap = px.imshow(
    seg_profile,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="Blues",
    title="Heatmap des profils moyens"
)
st.plotly_chart(fig_heatmap, use_container_width=True)

# PERFORMANCE MARKETING

st.header("Performance marketing / campagnes")

taux_par_segment = df.groupby("Segment")["Response"].mean() * 100
fig_bar = px.bar(
    taux_par_segment,
    title="Taux de réponse par segment (%)",
    labels={"value": "Taux de réponse (%)", "Segment": "Segment"}
)
st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("Nombre moyen de campagnes acceptées par segment")
st.dataframe(df.groupby("Segment")["Total_Accepted_Campaigns"].mean().round(2))

# KPI EXÉCUTIFS

st.header("KPI exécutifs")

colA, colB = st.columns(2)

with colA:
    fig_income = px.bar(df.groupby("Segment")["Income"].mean(),
                        title="Revenu moyen par segment")
    st.plotly_chart(fig_income, use_container_width=True)

with colB:
    fig_spend = px.bar(df.groupby("Segment")["Total_Spending"].mean(),
                       title="Dépense moyenne par segment")
    st.plotly_chart(fig_spend, use_container_width=True)

fig_score = px.bar(df.groupby("Segment")["Score_Valeur"].mean(),
                   title="Score de valeur moyen par segment")
st.plotly_chart(fig_score, use_container_width=True)

# RECOMMANDATIONS

st.header("Recommandations & alertes")

st.markdown("""
### Segment 1 – Premium  
- Très forte valeur  
- Très réactifs  
- Priorité absolue pour les campagnes personnalisées  

### Segment 2 – Digitaux à potentiel  
- Forte activité web  
- Dépense élevée  
- À développer via campagnes digitales ciblées  

### Segment 3 – Seniors faible valeur  
- Faible réactivité  
- À cibler avec parcimonie  

### Segment 0 – Jeunes / ménages modestes  
- Faible valeur actuelle  
- Potentiel long terme  
""")

