# This is a list of useful commands for the analysis
# Since the endgoal is an automated ressource, those commands only serve for manual usage and debugging

# SETUP
# NOT ALL STEPS ARE NECESSARY, only those marked with ***

# Enable Systemd
sudo -e /etc/wsl.conf

# Add the following, save and exit
[boot]
systemd=true

# Restart WSL2

# Install Docker ***
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=arm64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt install docker-ce

# Install Docker Compose ***
mkdir -p ~/.docker/cli-plugins/
curl -SL https://github.com/docker/compose/releases/download/v2.3.3/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
chmod +x ~/.docker/cli-plugins/docker-compose
sudo mkdir -p /usr/local/lib/docker/cli-plugins
sudo mv ~/.docker/cli-plugins/docker-compose /usr/local/lib/docker/cli-plugins/docker-compose

# Install Elastic Search
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update
sudo apt install elasticsearch

# Configure Elastic Search
sudo nano /etc/elasticsearch/elasticsearch.yml

# Uncomment and change this line, save and exit
network.host: localhost

# Start Elastic Search
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch

# Navigate to subfolder ***
cd ../..
cd /mnt/c/Users/User/Downloads/dmarc-visualizer-master

# Create necessary folders and copy templates ***
mkdir dmarc-visualizer-master/files
mkdir dmarc-visualizer-master/output_files
sudo cp -a output_template/. dmarc-visualizer-master/output_files/

# Run ***
sudo docker compose -f ./docker-compose.yml up -d

# Stop ***
sudo docker compose down

# Results at http://localhost:3000/


# SQL

# Navigate to binaries directory
cd C:\Program Files\MySQL\MySQL Server 8.0\bin

# Connect to 'dmarc' database using root user
mysql -u root -p dmarc

# GRAFANA

# Generate Dashboard
generate-dashboard -o dmarc.json dmarc.dashboard.py

# DEBUGGING

# List active Docker containers
sudo docker container ls

# Shutdown one Docker container
sudo docker container stop <ID>

# Remove all Docker containers
sudo docker ps -qa | xargs -n1 sudo docker rm

# Restart Docker
sudo systemctl restart docker

# Restart Elastic Search
sudo service elasticsearch restart

# Reinstall Elastic Search
sudo apt-get remove --purge elasticsearch
sudo apt-get install elasticsearch=7.10.1
sudo systemctl start elasticsearch
curl http://localhost:9200/

# Reinstall WSL2 Ubuntu
wsl --shutdown
wsl --unregister Ubuntu
wsl --install Ubuntu