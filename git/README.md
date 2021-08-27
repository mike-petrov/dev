# git


Откатить коммиты и залить
git reset --hard <hash>
git push --force

Переключаться на ветку
git checkout <branch_name>

Насильно обновить локальный репозиторий
git fetch --all
git reset --hard origin/master
git pull origin master

Авторизация
git config --global user.name "<логин>"
git config --global user.email "<почта>"
git config --global user.password "<пароль>"

Слить ветки master и dev
git checkout master
git merge dev
git push

git-credential-manager-core
если ошибка
git config --global credential.credentialStore cache
