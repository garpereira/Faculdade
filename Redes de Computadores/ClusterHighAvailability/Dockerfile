FROM php:7.4-apache

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y git

WORKDIR /var/www/html
RUN git clone https://github.com/matheuxito/NAT-Web-Server.git

RUN echo "\
<VirtualHost *:80>\n\
    ServerName localhost\n\
    DocumentRoot /var/www/html\n\
    <Directory /var/www/html>\n\
        Options Indexes FollowSymLinks MultiViews\n\
        AllowOverride All\n\
        Order allow,deny\n\
        allow from all\n\
    </Directory>\n\
    RedirectMatch ^/$ /NAT-Web-Server/\n\
</VirtualHost>\n\
" > /etc/apache2/sites-available/000-default.conf

RUN chown -R www-data:www-data /var/www/html/NAT-Web-Server

EXPOSE 80