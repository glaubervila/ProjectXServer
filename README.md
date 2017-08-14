# ProjectXServer

### Install Docker and Docker-Compose

TODO: link to install_docker_compose

### Up Containers

To create an .env file with the variables, and edit the file to change the default values if needed.
```
# cat env_template >> .env
```

Build and run app with Compose
```
# sudo docker-compose build
# sudo docker-compose up
```

Tip:
you want to run your services in the background, you can pass the -d flag (for “detached” mode) to docker-compose up and use docker-compose ps to see what is currently running:
```
# sudo docker-compose up -d
```
