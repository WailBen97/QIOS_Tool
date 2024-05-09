import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'models')


features_column=["type_batiment_dpe","periode_construction_dpe","surface_habitable_logement",
                 "type_installation_chauffage","type_generateur_chauffage","type_energie_chauffage_appoint","chauffage_solaire",
                 "nb_generateur_chauffage","type_generateur_climatisation","type_installation_ecs","type_generateur_ecs",
                 "ecs_solaire","nb_generateur_ecs",
                 "type_ventilation","type_production_energie_renouvelable","type_vitrage","type_materiaux_menuiserie","type_gaz_lame",
                 "type_fermeture","traversant","type_isolation_mur_exterieur","type_isolation_plancher_bas","type_isolation_plancher_haut","zone_climatique"]
y_column=["conso_5_usages_ep_m2","conso_5_usages_ef_m2","emission_ges_5_usages_m2"]
