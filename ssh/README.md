# ssh

## SSH Commands ([Подробнее](https://www.ssh.com/academy/ssh))
Store path macos: `/Users/<username>/.ssh`
### Добавить ключ в агента
```
ssh-agent -s
ssh-add /Users/mikepetrov/.ssh/id_rsa_syntax
ssh -T git@github.com
```
### Удалить все ключи из агента
```
ssh-add -D  
```
### Хранение нескольких ключей
`config` файл:
```
Host <name1>
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_<path1>
Host <name2>
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_<path2>
```