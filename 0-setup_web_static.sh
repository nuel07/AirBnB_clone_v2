#!/usr/bin/env bash
# setup web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
sudo echo "<html>
     <head>
     </head>
     <body>
	Holberton School
     </body>
     </html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

printf %s "server {
       listen 80 default_server;
       listen [::]:80 default_server;
       add_header X-Served-By $HOSTNAME;
       root /var/www/html;
       index index.html index.htm;

       location /hbnb_static {
       		alias /data/web_static/current;
		index index.html index.htm;
       }

       location /redirect_me {
       		return 301 http://nba.com/;
       }
       error_page 404 /404.html;
       location /404 {
       		root /var/www/html;
		internal;
       }
}" > /etc/nginx/sites-available/default
service nginx restart
