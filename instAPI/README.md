# instAPI

## Пошаговая инструкция ([подробнее](https://active-vision.ru/blog/instagram-api-basic-display/) [видеоинструкция](https://www.youtube.com/watch?v=X2ndbJAnQKM))

1. Войти в аккаунт и перейти в [консоль разработчика](https://developers.facebook.com/)
2. Нажать на вкладку Мои приложения и создать новое
3. Настроить Instagram API Basic Display
4. Добавить тестировщика Instagram
5. Аутентифицировать тестировщика
6. Получить токена Instagram API Basic Display
6.1. Получение кода доступа, далее будет использоваться как code
```
https://api.instagram.com/oauth/authorize?app_id=<app_id>&redirect_uri=<client_id>&scope=user_profile,user_media&response_type=code
```
6.2. Получение access_token по коду доступа
```
curl -X POST https://api.instagram.com/oauth/access_token -H "Content-Type: application/x-www-form-urlencoded" -d "client_id=<client_id>&client_secret=<client_secret>&grant_type=authorization_code&redirect_uri=<redirect_uri>&code=<code>"
```
7. Пример получения данных
```
https://graph.instagram.com/17841404103638834?fields=id,username&access_token=<access_token>
```
```
https://graph.instagram.com/me/media?fields=id,caption&access_token=<access_token>
```
```
https://graph.facebook.com/18172496062056993?fields=like_count&access_token=<access_token>
```
