from fastapi import FastAPI
import time
import requests

app = FastAPI()


@app.get("/")
def Home():
    return{"message":"URL Status Checker API"}

@app.get("/check")
def API_check(url:str,):
    start_time = time.time()
    
    try :
        response = requests.get(url,timeout=5)
        response_time = time.time()-start_time
        return{
            "url" : url,
            "status" : "UP",
            "status_code" : response.status_code,
            "response_time_ns" : round(response_time * 1000 , 2)
            
        }
    
    except requests.exceptions.RequestException:
        
        return {
            "url": url,
            "status": "DOWN",
            "message": "Website not reachable"
        }