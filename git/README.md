# git

## Хранение учетных данных
### GCM Core ([Подробнее](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git))
```
brew tap microsoft/git
brew install --cask git-credential-manager-core
// если ошибка
git config --global credential.credentialStore cache
```

### Обновление конфига
```
git config --global user.name "<name>"
git config --global user.email "<email>"
git config --global user.password "<password>"
```

### Запоминание логина и пароля от github
```
git config credential.helper store
```

## Основные команды
### Откатить коммиты и залить
```
git reset --hard <hash>
git push --force
```

### Переключаться на ветку
```
git checkout <branch_name>
```

### Насильно обновить локальный репозиторий
```
git fetch --all
git reset --hard
git pull
```

### Слить ветки master и dev
```
git checkout master
git merge dev
git push
```
