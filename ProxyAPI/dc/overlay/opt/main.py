from fastapi import FastAPI, Response, Request

from passlib.context import CryptContext

import requests

app = FastAPI()


# initialize the hashing
    
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# verify the bearer token against the hashed_token
# generate the hash with pwd_context.hash(password) in a python shell for instance (or write a program)

hashedBearerToken = '$2b$12$DaB8hCQM3Aexv0diszCCLuDTirmDiKmc1F6EGawD7iCXm2X43IJO.'

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)




@app.get("/institutions")
async def readSearchQuery(request: Request):
    
    
    # get the bearer token
    
    tokenHeader = request.headers['Authorization']
    
    token = tokenHeader.split(' ')[1]
    
    print('the verification gives:')
    print(verify_password(token, hashedBearerToken))
    
    
    # get the fullSearch parameter
    
    params = request.query_params
    
    fullSearchParam = params['fullSearch']
    print('the param:')
    print(fullSearchParam)
    
'''   
    if verify_password(token, hashedBearerToken) == True:
        
        myHeaders = {"ACCEPT": "application/ld+json", 'Authorization': 'Bearer ' + token. 'Content-Type': 'application/ld+json'}
        
        # make the request to the elucidate api
        
        url = 'https://api.dev.elucidate.co/institutions?fullSearch=XXX'
        
        response = requests.get(url, headers = myHeaders)
        
        
        # here I do not get forward, as the JWT Token got from evi.dev.elucidate.co/login gives the error "invalid JWT Token" 
        # when trying to curl the get request --> probably the recieved token is somehow related to another cookie, or the session in another way
        print(response)
        
        # if the response is "institution not found, query the ticket"
        
        
        url = 'https://api.dev.elucidate.co/tickets'
        
        from datetime import date, datetime
        today = date.today()
        time = datetime.now()
        
        myData = {  'project': 'projects/2a9caad1-19c7-4340-949f-30b81a8a043e',  
        'title': 'missing Institution ' + fullSearchParam,  
        'description': 'add Institution ' + fullSearchParam,  
        'createdAt': today + time,  
        'updatedAt': today + time 
        }
        
        
        
        response = requests.post(url, json = myData, headers = myHeaders)

        print(response.text)
'''        
    
    
    
    
    
    
    
    return None



