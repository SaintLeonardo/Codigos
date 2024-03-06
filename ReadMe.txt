1º Passo

docker build -t database .

2º Passo

docker run -it --name sqlite-container database /bin/sh