launching


accessing containers 
docker run -it --name test-container alpine:3.12.7
docker start container-name 
docker exec container-name command-to-run
docker exec -it test-container sh

docker cp local/path test-container:container/path

docker stop name
docker container prune (-a)
docker stats

создание images и контейнеров 
```
docker build . -t tg_bot # билдим образ из докерфайла
docker run -dt --name name tg_bot # создаем контейнер по нашему образу

docker run -it --name a-container --rm alpine:3.12.7  # запускаемся в интерактивном режиме
docker run -dt --restart on-failure --name b-container alpine:3.7.12 # запускаем контейнер в бэкграунде 

docker start container_name # запускаем остановленный контейнер
docker stop container_name # останавливаем контейнер 

docker image ls # показать все активные имеджи
docker image ls -a # показать все имеджи
docker container ls # показать все активные контейнеры 
docker container ls -a # показать все контейнеры 
docker image rm image_name # удалить image
docker system prune # почистить систему
```