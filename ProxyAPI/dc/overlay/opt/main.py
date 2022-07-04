from fastapi import FastAPI, Response, Request

from passlib.context import CryptContext

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
    
    fullSearch = params['fullSearch']
    print('the param:')
    print(fullSearch)
    
    
    if verify_password(token, hashedBearerToken) == True:
        
        
        
    
    
    
    
    
    
    
    return None



