import streamlit as st

def main():
    st.set_page_config(layout="wide")
    st.title("Entrée de données pour l'analyse DPE")

    type_batiment_dpe_options = {
        "Maison": "maison",
        "Appartement": "appartement",
        "Immeuble": "immeuble"
    }
    periode_construction_dpe_options = {
        'Avant 1948': 'avant 1948', '1948-1974': '1948-1974',
        '1975-1977': '1975-1977', '1978-1982': '1978-1982',
        '1983-1988': '1983-1988', '1989-2000': '1989-2000','2001-2005': '2001-2005', '2006-2012': '2006-2012', '2013-2021': '2013-2021',
        'Après 2021': 'après 2021'
    }
    type_options = {
        "Collectif": "collectif",
        "Individuel": "individuel"
    }
    generateur_chauffage_options = {
    "Chaudière Gaz Condensation": "chaudiere gaz condensation",
    "PAC Air/Air": "pac air/air",
    "Générateurs à Effet Joule": "generateurs a effet joule",
    "Chaudière Fioul Basse Température": "chaudiere fioul basse temperature",
    "Poêle ou Insert Bois": "poele ou insert bois",
    "Chaudière Fioul Standard": "chaudiere fioul standard",
    "PAC Air/Eau": "pac air/eau",
    "Chaudière Bois": "chaudiere bois",
    "Chaudière Gaz Standard": "chaudiere gaz standard",
    "Chaudière Électrique": "chaudiere electrique",
    "Chaudière Gaz Basse Température": "chaudiere gaz basse temperature",
    "Chaudière Fioul Condensation": "chaudiere fioul condensation",
    "PAC Géothermique": "pac geothermique",
    "Chaudière GPL/Butane/Propane Condensation": "chaudiere gpl/butane/propane condensation",
    "Réseau de Chaleur": "reseau de chaleur",
    "Radiateurs Gaz": "radiateurs gaz",
    "Chaudière GPL/Butane/Propane Basse Température": "chaudiere gpl/butane/propane basse temperature",
    "Chaudière GPL/Butane/Propane Standard": "chaudiere gpl/butane/propane standard",
    "Poêle ou Insert Fioul": "poele ou insert fioul",
    "PAC Eau/Eau": "pac eau/eau",
    "Poêle ou Insert Charbon": "poele ou insert charbon",
    "Générateur Air Chaud Combustion": "generateur air chaud combustion",
    "Chauffage Solaire": "chauffage solaire",
    "Poêle ou Insert GPL/Butane/Propane": "poele ou insert gpl/butane/propane",
    "Chaudière Charbon Standard": "chaudiere charbon standard",
    "Chaudière Charbon Basse Température": "chaudiere charbon basse temperature",
    "PAC Gaz": "pac gaz"
    }
    energie_appoint_options = {
    "Aucun": "aucun",
    "Bois": "bois",
    "Électricité": "electricite",
    "Gaz": "gaz",
    "Fioul": "fioul",
    "GPL/Butane/Propane": "gpl/butane/propane",
    "Charbon": "charbon",
    "Réseau de Chaleur": "reseau de chaleur"
    }
    # Création de widgets pour l'entrée des données
    with st.container():
        st.subheader("Données Bâtiment")
        col1, col2, col3 = st.columns(3)
        with col1:
            type_batiment_dpe = st.selectbox("Type de bâtiment DPE", list(type_batiment_dpe_options.keys()))
        with col2:
            periode_construction_dpe = st.selectbox("Période de construction DPE", list(periode_construction_dpe_options.keys()))
        with col3:
            surface_habitable_logement = st.number_input("Surface habitable du logement (en m²)", min_value=0.0, step=0.1)
    with st.container():
        st.subheader("Chauffage")
        col4, col5, col6,col7 = st.columns(4)
        with col4:
            type_installation_chauffage = st.selectbox("Type installation de chauffage", list(type_options.keys()))
        with col5:
            type_generateur_chauffage = st.selectbox("Generateur de chauffage", list(generateur_chauffage_options.keys()))
        with col6:
            type_energie_chauffage_appoint = st.selectbox("Type énergie appoint", list(energie_appoint_options.keys()))
        with col7:
            chauffage_solaire_checkbox = st.checkbox("Chauffage solaire")
            chauffage_solaire = 1 if chauffage_solaire_checkbox else 0

    # Ajoutez ici des widgets pour les autres caractéristiques...

    # Un bouton pour traiter les entrées
    if st.button("Calculer"):
        # Ici, vous pourriez appeler une fonction qui traite ces données,
        # comme faire une prédiction avec un modèle ML déjà entraîné
        st.write("Résultats à venir...")  # Remplacez cela par votre logique de calcul ou prédiction

if __name__ == "__main__":
    main()
