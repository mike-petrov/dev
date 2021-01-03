# YandexAPI

## Пошаговая инструкция ([подробнее](https://yandex.ru/dev/oauth/doc/dg/concepts/about.html))

1. Зарегистрировать приложение на [Яндекс.OAuth](https://oauth.yandex.ru)
2. После создания запомнить ID и Пароль, далее будут использоваться как client_id и client_secret
3. Получить код доступа, далее будут использоваться как code:
```
https://oauth.yandex.ru/authorize?response_type=code&client_id=<client_id>
```
4. Получить токен по коду доступа:
```
POST
https://oauth.yandex.ru/token
Content-type: application/x-www-form-urlencoded
Authorization: Basic <закодированная строка с помощью base64 client_id:client_secret>
grant_type=authorization_code&client_id=<client_id>&client_secret=<client_secret>&code=<code>
```
##### В ответе `access_token`, `expires_in`, `refresh_token`, `token_type`
