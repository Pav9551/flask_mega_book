# flask_mega_book
На базе архитектуры flaskmegabook

- pip install -r requirements.txt
- git fetch --all
- git reset --hard
- git pull
## создаем сертификат безопасности
- root@ubuntu
- wget https://go.dev/dl/go1.21.4.linux-amd64.tar.gz -O go.tar.gz
- sudo tar -xzvf go.tar.gz -C /usr/local
- echo export PATH=$HOME/go/bin:/usr/local/go/bin:$PATH >> ~/.profile
- source ~/.profile
- go version

- go install github.com/go-acme/lego/v4/cmd/lego@latest
- which lego
- sudo ln -s /root/go/bin/lego /usr/local/bin/lego
- sudo lego --email="mail@gmail.com" --domains="gitea.example.pw" --http run
## создаем резервную копию базы данных
- docker exec -i sql pg_dump -U postgres hass > hass.dump
- docker exec -i sql psql -U postgres -d hass -c "CREATE DATABASE hass1;"
- docker exec -i sql psql -U postgres hass1 < hass.dump
- docker exec -i sql psql -U postgres -d hass -c "DROP DATABASE hass1;"


