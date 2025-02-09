from fastapi import FastAPI
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()



URL = f'https://graph.facebook.com/{os.getenv("API_VERSION")}/{os.getenv("FROM_PHONE_NUMBER_ID")}/messages'
HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'}

def send_message(message):
    data = {
                "messaging_product": "whatsapp",
                "to": "3158376046",
                "type": "text",
                "text":{
                "body": message
    }
    }
    data = json.dumps(data)
    response = requests.post(url=URL,headers=HEADERS, data=data)
    print(response)



@app.get("/fetch")
def fetch_data(id: int):
    

    print("id: ",id)
    

    if id == 10:
        message = "Fallo energia Mirador"
        send_message(message)
    elif id == 20:
        message = "Se restablece energia Mirador"
        send_message(message)
    elif id == 30:
        message = "Fallo energia Santa Barbara"
        send_message(message)
    elif id == 40:
        message = "Se restablece energia Santa Barbara"
        send_message(message)



    # Enviar solicitud GET a la API externa con el ID
        

      
       


