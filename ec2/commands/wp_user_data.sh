#!/bin/bash

sudo add-apt-repository ppa:ondrej/php -y
sudo apt update
sudo apt install apache2 apache2-utils mariadb-client \
    php7.4 libapache2-mod-php7.4 php7.4-mysql php-common php7.4-cli \
    php7.4-common php7.4-json php7.4-opcache php7.4-readline \
    php7.4-curl php7.4-fpm php7.4-gd php7.4-xml php7.4-mbstring \
    php7.4-bcmath unzip -y

sudo echo "<?php phpinfo();" | sudo tee /var/www/html/info.php

sudo systemctl restart apache2

wget -c http://wordpress.org/latest.tar.gz
tar -xzvf latest.tar.gz
sudo mv wordpress/* /var/www/html/
sudo mv /var/www/html/index.html /var/www/html/apache.html
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
