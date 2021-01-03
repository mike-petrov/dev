# cron

## Основные команды

#### Управление активными задачами:
```
crontab -e
```

#### Логи:
```
grep CRON /var/log/syslog
```

#### Включить выполнение задач:
```
sudo systemctl enable cron
```

#### Пример cron задачи:
```
1 * * * * curl -X POST -H "Content-Type: application/json" -d '{"token": "123"}' https://google.com/api/
```

#### Отчеты о выполненных кроном задачах:
```
MAILTO="mike@mikepetrov.ru"
```

#### Если ошибка `(CRON) info (No MTA installed, discarding output)`, необходимо указать адрес для отчетов, можно оставить пустым:
```
MAILTO=""
```
