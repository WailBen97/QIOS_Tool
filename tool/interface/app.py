import streamlit as st
from params_app import *
from tool.preprocessing.data import obtenir_zone_climatique
import requests

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

    if st.button("Calculer"):
        # Ici, vous pourriez appeler une fonction qui traite ces données,
            # Préparer les données pour l'API
        data_to_send = {
            "type_batiment_dpe": type_batiment_dpe_options[type_batiment_dpe],
            "periode_construction_dpe": periode_construction_dpe_options[periode_construction_dpe],
            "surface_habitable_logement": surface_habitable_logement,
            "type_installation_chauffage": type_options[type_installation_chauffage],
            "type_generateur_chauffage": generateur_chauffage_options[type_generateur_chauffage],
            "nb_generateur_chauffage": nb_generateur_chauffage,
            "type_energie_chauffage_appoint": energie_appoint_options[type_energie_chauffage_appoint],
            "chauffage_solaire": chauffage_solaire,
            "nb_generateur_chauffage": nb_generateur_chauffage,
            "type_generateur_climatisation": generateur_climatisation_options[type_generateur_climatisation],
            "type_installation_ecs": type_options[type_installation_ecs],
            "type_generateur_ecs": generateur_ecs_options[type_generateur_ecs],
            "ecs_solaire": ecs_solaire,
            "nb_generateur_ecs": nb_generateur_ecs,
            "type_ventilation": systeme_ventilation_options[type_ventilation],
            "type_production_energie_renouvelable": type_energie_renouvelable_options[type_production_energie_renouvelable],
            "type_vitrage": type_vitrage_options[type_vitrage],
            "type_materiaux_menuiserie": type_materiaux_menuiserie_options[type_materiaux_menuiserie],
            "type_gaz_lame": type_gaz_lame_options[type_gaz_lame],
            "type_fermeture": type_fermeture_options[type_fermeture],
            "traversant": traversant_options[traversant],
            "type_isolation_mur_exterieur": type_isolation_options[type_isolation_mur_exterieur],
            "type_isolation_plancher_bas": type_isolation_options[type_isolation_plancher_bas],
            "type_isolation_plancher_haut": type_isolation_options[type_isolation_plancher_haut],
            "zone_climatique": zone_climatique,
        }

        url ="http://127.0.0.1:8000/predict/"
        response = requests.post(url, json=data_to_send)

        if response.status_code == 200:
            results = response.json()
            # Extraire les valeurs spécifiques
            conso_ep = results.get("conso_3_usages_ep_m2", [0])[0]  # Présume une liste, prend le premier élément
            conso_ef = results.get("conso_3_usages_ef_m2", [0])[0]
            emission_ges = results.get("emission_ges_3_usages_m2", [0])[0]
          # Formatage sécurisé avec vérification du type pour éviter les erreurs de formatage
            if isinstance(conso_ep, (int, float)) and isinstance(conso_ef, (int, float)) and isinstance(emission_ges, (int, float)):
                st.write(f"La consommation d'énergie primaire est de {conso_ep:.2f} kWh/m².")
                st.write(f"L'énergie finale est de {conso_ef:.2f} kWh/m².")
                st.write(f"L'émission de GES est de {emission_ges:.2f} kg CO₂/m².")
            else:
                st.write("Les données reçues ne sont pas dans le format attendu.")
        else:
            st.error("Erreur de réponse de l'API : {}".format(response.status_code)) # Afficher un message d'erreur

if __name__ == "__main__":
    main()
