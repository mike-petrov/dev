# Digitalocean

## Пошаговая инструкция

1. Создание дроплета
2. Вход и изменение пароля
3. Node js ([подробнее](https://www.digitalocean.com/community/tutorials/node-js-ubuntu-18-04-ru))
```
sudo apt install nodejs // установка node js
sudo apt install npm // установка пакетного менеджера

// при ошибке E: Unable to locate package npm
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```
4. Пользователи ([подробнее](https://www.8host.com/blog/sozdanie-polzovatelya-sudo-v-ubuntu))
```
adduser username // создать пользователя
deluser username // удалить пользователя
sed 's/:.*//' /etc/passwd // просмотреть всех пользователей
usermod -aG sudo username // добавить пользователя в группу sudo
su - username // перейти в сессию пользователя
```
5. Tmux ([подробнее](https://habr.com/ru/post/327630))
```
apt-get install tmux // установка
```
6. Nginx ([подробнее](https://itdeer.ru/nginx-na-ubuntu-server-18-04))
```
sudo apt install nginx // установка
sudo service nginx status // статус веб сервера
cat /var/log/nginx/access.log // логи сервера
service nginx start // старт сервера
service nginx stop // стоп сервера
service nginx restart // рестарт сервера
```
7. Firewall ([подробнее](https://losst.ru/nastrojka-ufw-ubuntu))
```
sudo ufw status // статус firewall
sudo ufw enable // включить firewall
sudo ufw enable // включить firewall
sudo ufw default deny incoming // отклонение входящих пакетов
sudo ufw default allow outgoing // разрешение исходящих пакетов
cat /var/log/ufw.log // логи firewall
```
8. Бесплатный SSL ([подробнее](https://certbot.eff.org/help))
```
sudo certbot --nginx // запуск
```
9. Flask ([подробнее](https://www.8host.com/blog/obsluzhivanie-prilozhenij-flask-s-pomoshhyu-uwsgi-i-nginx-v-ubuntu-16-04/))
```
python run.py // запуск
```
9. Mongodb ([подробнее](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-mongodb-on-ubuntu-16-04))
##### Создание пользователя
```
mongo

use admin
db.createUser(
  {
    user: "user",
    pwd: "password",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
```
##### Включение аутентификации
```
sudo nano /etc/mongod.conf

security:
  authorization: "enabled"

sudo systemctl restart mongod
```
##### Включение файервола
```
sudo ufw enable
sudo ufw status
sudo ufw allow from client_ip_address to any port 27017
```
##### Настройка публичного ip
```
sudo nano /etc/mongod.conf

net:
  port: 27017
  bindIp: 127.0.0.1, IP_of_MongoHost

sudo systemctl restart mongod
```


## Дополнение

1. Logs Nginx
```
cat /var/log/nginx/access.log // access
cat /var/log/nginx/error.log // error
```
2. Права для проекта
```
chmod 755 /folder // права для дерикторий
chmod 644 /folder // права для файлов
```
3. Активация виртуальных хостов (sites-available -> sites-enabled)
```
ln -s /etc/nginx/sites-available/file.conf /etc/nginx/sites-enabled/
```
4. Запоминание логина и пароля от github
```
git config credential.helper store
```
5. Активация env
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
6. Проверка обновлении пакетов и обновление пакета до последней версии
```
npm outdated --depth=0
```
```
npm i react@latest
```
7. Загрузка больших файлов Nginx (Увеличение максимально допустимого размера тела запроса клиента)
```
sudo nano /etc/nginx/nginx.conf
```
```
types_hash_max_size 20480;
client_max_body_size 30m;
```
