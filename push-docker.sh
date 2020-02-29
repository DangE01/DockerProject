#!/usr/bin/env bash
# This tags and uploads an image to Docker Hub

#Assumes this is built
#docker build --tag=app .


dockerpath="edang1/diceroll"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag diceroll:1.7 $dockerpath

# Push Image
docker image push $dockerpath 