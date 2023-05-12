sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
sudo wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key

sudo apt update
sudo apt install python3 python3-pip grafana
pip3 install -r requirements.txt

mkdir -p dmarc-reports/rua/attachment
mkdir -p dmarc-reports/rua/mail
mkdir -p dmarc-reports/rua/report
mkdir -p dmarc-reports/ruf/attachment
mkdir -p dmarc-reports/ruf/mail
mkdir -p dmarc-reports/ruf/report

sudo /bin/systemctl start grafana-server