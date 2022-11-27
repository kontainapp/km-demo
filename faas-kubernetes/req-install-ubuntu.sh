sudo apt-get update
# sudo apt-get install python3.6
sudo apt-get install python3 -y

sudo apt-get install nginx -y

sudo apt-get install jq -y

sudo ufw disable

sudo systemctl start nginx
sudo systemctl enable nginx

sudo apt-get install python3-pip -y
sudo pip3 install locust

