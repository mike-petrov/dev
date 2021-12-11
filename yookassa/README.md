# yookassa

## Пошаговая инструкция ([подробнее](https://yookassa.ru/developers/payments/quick-start))

1. Создать тестовый магазин на [yookassa.ru](https://yookassa.ru/)
2. После создания узнать Идентификатор магазина и Секретный ключ, далее будут использоваться как shopId и secretKey
3. Сгенерировать платеж:
```
import uuid
from yookassa import Configuration, Payment

Configuration.account_id = <shopId>
Configuration.secret_key = <secretKey>

payment = Payment.create({
    "amount": {
        "value": "100.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://www.merchant-website.com/return_url"
    },
    "capture": True,
    "description": "Заказ №1"
}, uuid.uuid4())
```
4. В ответе получить id платежа и ссылку на оплату:
```
payment.id
payment.confirmation.confirmation_url
```
5. Проверить статус платежа:
```
Configuration.account_id = <shopId>
Configuration.secret_key = <secretKey>
payment_id = <id>
payment = Payment.find_one(payment_id)
print(payment.status) # pending / succeeded
```