from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="API Preditiva de NPS", description="Prevê se um cliente será Detrator, Neutro ou Promotor")

# Carrega o modelo de IA que salvamos
model = joblib.load('models/modelo_nps.pkl')

# Define o formato do JSON que a API vai receber
class CustomerData(BaseModel):
    customer_age: int
    customer_tenure_months: int
    order_value: float
    items_quantity: int
    discount_value: float
    payment_installments: int
    delivery_time_days: int
    delivery_delay_days: int
    freight_value: float
    delivery_attempts: int
    customer_service_contacts: int
    resolution_time_days: int
    complaints_count: int
    repeat_purchase_30d: int
    csat_internal_score: float
    # Regiões (One-Hot Encoding que o modelo espera)
    customer_region_Nordeste: bool = False
    customer_region_Norte: bool = False
    customer_region_Sudeste: bool = False
    customer_region_Sul: bool = False

@app.post("/predict")
def predict_nps(data: CustomerData):
    # Transforma o JSON recebido em um formato de tabela (DataFrame) que a IA vai conseguir compreender do jeito que eu quero
    df = pd.DataFrame([data.dict()])
    
    df = df[model.feature_names_in_]
    
    # Faz a previsão
    previsao = model.predict(df)[0]
    
    return {"status": "sucesso", "nps_class_prevista": previsao}