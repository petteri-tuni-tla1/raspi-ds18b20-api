
# 19.4.2026 - System tools

sudo apt install tree

# 19.4.2026 - Web server for temperature readings ...

sudo apt install apache2

sudo a2enmod proxy
sudo a2enmod proxy_http
sudo systemctl restart apache2


# To read new service files in /etc/systemd/system: 

sudo systemctl daemon-reload

# 19.4.2026 - Flask application for DS18B20 sensor readings

sudo systemctl start flask-temp.service
sudo systemctl enable flask-temp.service

# 19.4.2026 - The ssh tunneling services

sudo systemctl start autossh-flask-tammerkoski.service
sudo systemctl enable autossh-flask-tammerkoski.service

sudo systemctl enable tammerkoski-autossh.service
sudo systemctl start tammerkoski-autossh.service

