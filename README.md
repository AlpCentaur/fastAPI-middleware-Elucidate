# fastAPI-middleware-Elucidate

## How to start the containers

go to the directory 

    dc/compose 
    
and issue 

    docker-compose up


Then go to localhost:8000

Or for documentation of the api, go to 

    localhost:8000/docs


The server is located under

    /dc/overlay/opt/main.py
    
This means, with the running docker container, and 
by modifying the dockerfile uvicorn command to reload,
you could change the code on your base system in the graphical
editor of your choice
