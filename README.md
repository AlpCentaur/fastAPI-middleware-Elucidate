# fastAPI-middleware-Elucidate

## How to start the containers

go to the directory 

    dc/compose 
    
and issue 

    docker-compose up


Then go to 

    localhost:8000


Or for documentation of the api, go to 

    localhost:8000/docs


## Further understanding of the directory structure

The Dockerfile, documenting the installations and the 
commands is located under 

    ProxyAPI/dc/build/elucidate-api-middleware/Dockerfile

The server is located under

    ProxyAPI/dc/overlay/opt/main.py
    
This means: 
With the running docker container, and 
by modifying the dockerfile uvicorn command to reload,
(with the --reload flag)
you could change the code on your base system in the graphical
editor of your choice.
