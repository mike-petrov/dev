# Docker

[Составление dockerfile](https://gist.github.com/GeorgeKanchev/31c331148ad10203719beecb725af912)

## Основные команды
### build:
```
docker build -t project_name .
```

### tag:
```
docker tag project_name user_id/project_name
```

### push:
```
docker push user_id/project_name
```

### run:
```
docker run -p 5000:3000 project_name
```

## Пример для разработки на react

### Структура проекта
```
/project_name
—/web
—.dockerignore
—Dockerfile
```

### dockerfile
```
FROM node:latest
WORKDIR /web
COPY package*.json ./
RUN npm install --silent
COPY /web /web
CMD ["npm", "start"]
```

### dockerignore
```
.git
build
node_modules
```

## Удаление мусора

### Остановить все Docker контейнеры
```
docker stop $(docker ps -a -q)
```
### Удалить все Docker контейнеры
```
docker rm $(docker ps -a -q)
```
### Удалить неиспользованные Docker образы:
```
docker image prune -a -f
```
