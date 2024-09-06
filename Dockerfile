#use pyhtonimage
FROM python:3.8-slim-buster

#set working directory
WORKDIR /adam-work-dir

#copy the current directory contents into the container at /adam-work-dir
COPY index.html .

# port will run on 80080
EXPOSE 8080

#run the command set the default command to execute when the container starts
CMD ["python3", "-m", "http.server", "8080"]