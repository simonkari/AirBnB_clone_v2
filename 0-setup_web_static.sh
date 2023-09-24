#!/usr/bin/env bash
# sets up your web servers for the deployment
sudo apt-get update
sudo apt-get -y install nginx
echo "Best school" | sudo tee /var/www/html/index.html
new_string="server_name _;\n\trewrite ^\/redirect_me http:\/\/35.237.80.55\/some_page.html permanent;"
sudo sed -i "s/server_name _;/$new_string/" /etc/nginx/sites-available/default
string_404="server_name _;\n\terror_page 404 \/custom_404.html;\n\tlocation = \/custom_404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}"
sudo sed -i "s/server_name _;/$string_404/" /etc/nginx/sites-available/default
sudo sed -i "/server_name _;/ a\\\tadd_header X-Served-By \"\$HOSTNAME\";" /etc/nginx/sites-available/default
service nginx restart
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
<head>
</head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default
nginx -t
service nginx restart
exit 0
