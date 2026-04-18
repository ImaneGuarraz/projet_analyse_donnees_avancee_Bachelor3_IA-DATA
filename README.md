# **Advanced Marketing Analytics**
## _Decision Intelligence • Segmentation • Scoring • BI_

<p align="center"> <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python"> <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-orange?style=for-the-badge&logo=pandas"> <img src="https://img.shields.io/badge/Scikit--Learn-ML-yellow?style=for-the-badge&logo=scikit-learn"> <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"> </p>

---

### 💡 Vue d’ensemble du projet

Ce projet vise à transformer un dataset marketing en un véritable système de décision (Decision Intelligence).

L’objectif est de passer de données brutes à des insights actionnables permettant :

- d’améliorer la segmentation client
- d’optimiser le ciblage marketing
- d’augmenter le ROI des campagnes
- et de mettre en place un scoring prédictif

--- 

### Comment transformer un dataset marketing en un système décisionnel capable d’éclairer la segmentation, le ciblage, la performance campagne et la feuille de route analytique de l’entreprise ?

---

### 💿 Description du dataset
_2240 lignes & 29 colonnes_ 

Le dataset contient des informations détaillées sur les clients : 
- Données socio-démographiques (âge, revenu, éducation)
- Comportement d’achat (dépenses par catégorie, fréquence)
- Interactions marketing (réponses aux campagnes)
- **Variable cible : Response (réponse à la dernière campagne)**

---

### 🧹 Nettoyage du dataset

Le Dataset a été nettoyé avant l'analyse de données pour limiter le bruit inutile. 

Les points majeurs de ce nettoyage : 
- Gestion des doublons et des valeurs nulles ;
- Visualisation et nettoyage des outliers ;
- Traitement des dates ;
- Calcule de features sur base d'analyse, comme l'age, l'ancienneté, le total des dépenses et le total de campagnes précédemment acceptées ; 
- Suppressions des variables à valeur unique ou sans utilité dans nnotre cas.     

---

### 📉 Analyse des données

L’analyse exploratoire met en évidence plusieurs insights clés :
- Une forte relation entre revenu et niveau de dépenses
- Les clients les plus dépensiers sont les plus susceptibles de répondre
- La récence influence fortement l’engagement
- L’historique des campagnes est un excellent prédicteur

_Retrouvez toutes les informations complémentaires directement dans le script Notebook ou dans le rapport de synthèse._

**Robustesse analytique** : Des analyses complémentaires ont été réalisées.

- vérification de la multicolinéarité (VIF)
- matrice de corrélation
- analyse des outliers
- validation du modèle

Ces étapes garantissent la fiabilité des résultats.

---

### 🎯 Segmentation client

Une segmentation a été réalisée afin d’identifier 4 différents profils (kmeans, test Elbow et Silhouette Score) :

**Segment 1 — Les Premium**

- Très haut revenu
- Très forte dépense
- Très bon taux de réponse
- Activité digitale correcte

Ce sont tes clients VIP. Ils génèrent la majorité de la valeur et réagissent très bien aux campagnes.
C’est le segment à prioriser dans toutes les actions marketing.

**Segment 2 — Les Digitaux à fort potentiel**

- Revenu élevé
- Dépense élevée
- Activité web forte
- Taux de réponse moyen

Ils ont un potentiel énorme. Avec un meilleur engagement, ils pourraient rejoindre les Premium.
C’est un segment à travailler, notamment via des campagnes digitales personnalisées.

**Segment 3 — Les Seniors à faible valeur**

- Revenu moyen
- Dépense faible
- Taux de réponse très faible
- Activité web modérée

Segment peu rentable. Il ne faut pas les cibler massivement.
À privilégier pour des actions de fidélisation douce, pas pour des campagnes coûteuses.

**Segment 0 — Les Jeunes / ménages modestes**

- Revenu faible
- Dépense faible
- Taux de réponse moyen
- Activité web élevée

Faible valeur actuelle, mais potentiel long terme. Ce sont souvent des clients en début de cycle de vie.
À nourrir progressivement, sans investissement marketing lourd.
Cette segmentation permet d’adapter les stratégies marketing à chaque profil.

---

### 🎯 KPI métier

Le projet introduit plusieurs indicateurs clés :

- Taux de réponse aux campagnes
- Dépense moyenne par client
- Performance par segment
- Score client

Ces KPI permettent un pilotage data-driven.

---

### 📊 Modélisation prédictive

Un modèle de machine learning a été développé pour prédire la réponse client.

Variables utilisées :
- Revenu
- Dépenses
- Récence
- Engagement marketing

**Résultat : Un score de propension (probabilité de réponse)** qui permet : 

- un meilleur ciblage
- une réduction des coûts
- une optimisation du ROI

**Segment 1 — Score 48.6**
**Segment 2 — Score 40.1**
**Segment 3 — Score 20.5**
**Segment 0 — Score 19.0**

---

### 📈 Dashboard

Un dashboard interactif (Streamlit) a été développé pour :

- suivre les KPI
- analyser les segments
- visualiser les performances marketing
- identifier les clients à cibler

---

### 🏭 Industrialisation

Le projet est structuré sous forme de pipeline reproductible :
- préparation des données
- transformation
- modélisation
- scoring

_Il peut être intégré dans un environnement réel (CRM, BI)._

---

### 📊 Recommandations business

Les principaux leviers identifiés sont :
- cibler les clients à fort score
- concentrer les efforts sur les segments à forte valeur
- réactiver les clients inactifs
- suivre les performances via des KPI

---

### 💻 Technologies utilisées
- Python 3.12.7
- Pandas / NumPy
- Matplotlib / Seaborn
- Scikit-learn
- Statsmodels
- Streamlit

_Retrouver tout le détail des libairies exploitées dans le script Python._ 

---

### 🚀 Lancer le projet

pip install -r requirements.txt
streamlit run app.py

---

### 📁 Ressources et liens utiles 

- README (document exploré actuellement)
- PDF de présentation du projet et des attendus transmis par le professeur Alioune Sambe
- PDF de notre rapport d'activité, également disponible via le lien CANVA : https://canva.link/sd1hpyy8s0bgec0
- Notebook Python
- Lien du Dataset : https://www.kaggle.com/datasets/rodsaldanha/arketing-campaign

---

### 👩🏽‍💻👩🏿‍💻 Cheffes de projet 
- Olympe DOTSU
- Imane GUARRAZ

---

### Conclusion

Ce projet démontre comment transformer des données marketing en un outil stratégique de décision, permettant de passer d’une approche intuitive à une approche data-driven.
