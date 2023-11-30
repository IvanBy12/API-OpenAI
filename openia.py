import os
import openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    expose_headers=["*"]
   
)




@app.get("/")
def root():
    return {
        "service": "Integracion back openia"
        }


@app.post("/chat")
def chat(pregunta: dict):
    
    
    print(pregunta)
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": pregunta["pregunta"]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    
    return {
        
        "respuesta": response["choices"][0]["message"]["content"]
         
    }
