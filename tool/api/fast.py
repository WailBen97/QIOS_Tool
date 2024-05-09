import os
import json
from fastapi import FastAPI, HTTPException, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
import joblib
from pydantic import BaseModel
from tensorflow.keras.models import load_model
import logging
import pandas as pd

from tool.params import *

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

model_file_ep = "modele_energie_primaire_all_features.keras"
model_file_ges = "modele_ges_all_features.keras"
model_file_ef = "modele_energie_finale_all_features.keras"
model_file_prepro= "preprocessor.joblib"

model_path_ep = os.path.join(MODEL_DIR, model_file_ep)
model_path_ef= os.path.join(MODEL_DIR, model_file_ef)
model_path_ges = os.path.join(MODEL_DIR, model_file_ges)
model_path_prepro = os.path.join(MODEL_DIR, model_file_prepro)

# Charger le préprocesseur
preprocessor = joblib.load(model_path_prepro)

# Charger les modèles
model_ep = load_model(model_path_ep)
model_ges = load_model(model_path_ges)
model_ef = load_model(model_path_ef)

class PredictionInput(BaseModel):
    type_batiment_dpe: str
    periode_construction_dpe: str
    surface_habitable_logement: float
    type_installation_chauffage: str
    type_generateur_chauffage: str
    nb_generateur_chauffage: int
    type_energie_chauffage_appoint: str
    chauffage_solaire: int
    nb_generateur_chauffage: int
    type_generateur_climatisation: str
    type_installation_ecs: str
    type_generateur_ecs: str
    ecs_solaire: int
    nb_generateur_ecs: int
    type_ventilation: str
    type_production_energie_renouvelable: str
    type_vitrage: str
    type_materiaux_menuiserie: str
    type_gaz_lame: str
    type_fermeture: str
    traversant: str
    type_isolation_mur_exterieur: str
    type_isolation_plancher_bas: str
    type_isolation_plancher_haut: str
    zone_climatique: str



""" @app.post("/predict/")
async def predict(input_data: PredictionInput):
    try:
        # Convertir l'input Pydantic en DataFrame
        input_df = pd.DataFrame([input_data.dict()])

        # Appliquer le préprocesseur
        processed_data = preprocessor.transform(input_df)

        # Faire des prédictions (exemple)
        prediction_ges = model_ges.predict(processed_data)
        return {"predictions": prediction_ges.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) """
@app.post("/predict/")
async def predict(request: Request):
    try:
        # Récupérer les données JSON envoyées
        data = await request.json()
        logging.info(f"Data received: {data}")
        input_df=pd.DataFrame([data],index=[0])
        input_df.to_csv('output.csv', index=False)
        prepro_input=preprocessor.transform(input_df)
        predict_ges=model_ges.predict(prepro_input)[0]
        predict_ep=model_ep.predict(prepro_input)[0]
        predict_ef=model_ef.predict(prepro_input)[0]

        return {"conso_3_usages_ep_m2": predict_ep.tolist(),
                "conso_3_usages_ef_m2": predict_ef.tolist(),
                "emission_ges_3_usages_m2": predict_ges.tolist()
                }
    except Exception as e:
        logging.error(f"Error processing the request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/")
def root():

    return {"Welcome to Qios_Tool"}
