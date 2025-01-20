# flask_mega_book
На базе архитектуры flaskmegabook

pip install -r requirements.txt
git fetch --all
git reset --hard
git pull


wget https://go.dev/dl/go1.21.4.linux-amd64.tar.gz -O go.tar.gz
sudo tar -xzvf go.tar.gz -C /usr/local
echo export PATH=$HOME/go/bin:/usr/local/go/bin:$PATH >> ~/.profile
source ~/.profile
go version

cd flask_docker/go install github.com/go-acme/lego/v4/cmd/lego@latest
sudo lego --email="mail@gmail.com" --domains="gitea.example.pw" --http run

