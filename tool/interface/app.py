import streamlit as st
from params_app import *
from tool.preprocessing.data import obtenir_zone_climatique

def main():
    st.set_page_config(layout="wide")
    st.title("Entrée de données pour l'analyse DPE")

    # Création de widgets pour l'entrée des données
    with st.container():
        st.subheader("Données Bâtiment")
        col1, col2, col3,col16,col17 = st.columns(5)
        with col1:
            type_batiment_dpe = st.selectbox("Type de bâtiment DPE", list(type_batiment_dpe_options.keys()))
        with col2:
            periode_construction_dpe = st.selectbox("Période de construction DPE", list(periode_construction_dpe_options.keys()))
        with col3:
            surface_habitable_logement = st.number_input("Surface habitable du logement (en m²)", min_value=0.0, step=0.1)
        with col16:
            traversant = st.selectbox("Type de bâtiment DPE", list(traversant_options.keys()))
        with col17:
            code_postal = st.number_input("Code Postal", min_value=1, max_value=95, value=1, step=1, format="%d")
    with st.container():
        st.subheader("Chauffage")
        col4, col5, col6,col7,col8 = st.columns(5)
        with col4:
            type_installation_chauffage = st.selectbox("Type installation de chauffage", list(type_options.keys()))
        with col5:
            type_generateur_chauffage = st.selectbox("Generateur de chauffage", list(generateur_chauffage_options.keys()))
        with col6:
            nb_generateur_chauffage = st.number_input("Nombre de générateurs Chauffage", min_value=1, value=1, step=1)
        with col7:
            type_energie_chauffage_appoint = st.selectbox("Type énergie appoint", list(energie_appoint_options.keys()))
        with col8:
            chauffage_solaire_checkbox = st.checkbox("Chauffage solaire")
            chauffage_solaire = 1 if chauffage_solaire_checkbox else 0
    with st.container():
        st.subheader("ECS")
        col9, col10, col11,col12= st.columns(4)
        with col9:
            type_installation_ecs = st.selectbox("Type installation de ecs", list(type_options.keys()))
        with col10:
            type_generateur_ecs = st.selectbox("Generateur de ecs", list(generateur_ecs_options.keys()))
        with col11:
            nb_generateur_ecs = st.number_input("Nombre de générateurs ECS", min_value=1, value=1, step=1)
        with col12:
            ecs_solaire_checkbox = st.checkbox("Ecs solaire")
            ecs_solaire = 1 if ecs_solaire_checkbox else 0
    with st.container():
        st.subheader("Climatisation/Enr/Ventilation")
        col13,col14,col15= st.columns(3)
        with col13:
            type_generateur_climatisation = st.selectbox("Generateur de climatisation", list(generateur_climatisation_options.keys()))
        with col14:
            type_production_energie_renouvelable= st.selectbox("Type production energie renouvelable", list(type_energie_renouvelable_options.keys()))
        with col15:
            type_ventilation= st.selectbox("Type de ventillation", list(systeme_ventilation_options.keys()))
    with st.container():
        st.subheader("Type Menuiserie")
        col18,col19,col20,col21= st.columns(4)
        with col18:
            type_vitrage = st.selectbox("Type de vitrage", list(type_vitrage_options.keys()))
        with col19:
            type_materiaux_menuiserie = st.selectbox("Type materiaux menuiserie", list(type_materiaux_menuiserie_options.keys()))
        with col20:
            type_gaz_lame = st.selectbox("Type gaz lame", list(type_gaz_lame_options.keys()))
        with col21:
            type_fermeture = st.selectbox("Type fermeture menuiserie", list(type_fermeture_options.keys()))
    with st.container():
        st.subheader("Isolation Enveloppe")
        col22,col23,col24= st.columns(3)
        with col22:
            type_isolation_mur_exterieur = st.selectbox("Type isolation mur exterieur", list(type_isolation_options.keys()))
        with col23:
            type_isolation_plancher_bas = st.selectbox("Type isolation plancher bas", list(type_isolation_options.keys()))
        with col24:
            type_isolation_plancher_haut = st.selectbox("Type isolation plancher haut", list(type_isolation_options.keys()))
    # Un bouton pour traiter les entrées
    zone_climatique=obtenir_zone_climatique(code_postal)
    st.write(f"La zone climatique pour le code postal {code_postal} est {zone_climatique}.")

    if st.button("Calculer"):
        # Ici, vous pourriez appeler une fonction qui traite ces données,
        # comme faire une prédiction avec un modèle ML déjà entraîné
        st.write("Résultats à venir...")  # Remplacez cela par votre logique de calcul ou prédiction

if __name__ == "__main__":
    main()
