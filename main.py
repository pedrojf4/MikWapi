from fastapi import FastAPI, HTTPException
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# URL de la API externa (cámbiala por la real)
API_URL = "https://jsonplaceholder.typicode.com/posts/"

URL = f'https://graph.facebook.com/{os.getenv("API_VERSION")}/{os.getenv("FROM_PHONE_NUMBER_ID")}/messages'
HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'}

@app.get("/fetch")
def fetch_data(id: int):
    

    print("id: ",id)
    

    if id == 10:
    # Enviar solicitud GET a la API externa con el ID
        data = {
                "messaging_product": "whatsapp",
                "to": "3158376046",
                "type": "text",
                "text":{
                "body": "Evento 1 ok gachantiva Santa barbara"
    }
    }
        data = json.dumps(data)
        response = requests.post(url=URL,headers=HEADERS, data=data)
        print(response)

      
       


