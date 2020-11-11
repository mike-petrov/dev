# JWT-Flask

[Инструкция](https://www.youtube.com/watch?v=J5bIPtEbS0Q)

## SECRET_KEY
```
app.config['SECRET_KEY'] = 'your-secret-key'
```
## /auth для выдачи JWT токена
```
@app.route('/auth', methods=['POST'])
def auth():
    id = request.json['id']
    token = jwt.encode({'user_id' : id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1)}, app.config['SECRET_KEY'])
    return jsonify({ 'token': token.decode('UTF-8') })
```
## Функция для проверки токена
```
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        header = request.headers.get('Authorization')
        token = header.split(' ')[1]

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            kwargs['jwt'] = data # передача данных в параметры
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated
```

## Защищенный роут
```
@app.route('/reg', methods=['POST'])
@token_required
def reg(jwt):
    return jsonify({'message': 'This is only available for people with valid tokens.!', 'user': jwt['user_id']})
```
