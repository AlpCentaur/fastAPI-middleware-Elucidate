from fastapi import FastAPI, Response, Request

app = FastAPI()



@app.get("/institutions")
async def readSearchQuery(request: Request):
    
    
    token = request.headers['Authorization']
    
    print(token)
    
    params = request.query_params
    
    
    
    fullSearch = params['fullSearch']
    
    
    
    print(fullSearch)
    
    
    return None



