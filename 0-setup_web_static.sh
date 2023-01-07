#!/usr/bin/env bash
# Sets up webserver for deployment

apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "HELLO WORLD!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
sed -i "24 a location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tadd_header X-Served-By $HOSTNAME;\n" /etc/nginx/sites-available/default
service nginx restart
