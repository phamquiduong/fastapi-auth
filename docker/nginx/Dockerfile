FROM nginx

# Install logrotate
RUN apt-get update && apt-get -y install logrotate tzdata && apt-get clean

COPY ./nginx/nginx-crontab /etc/crontab
COPY ./nginx/nginx.conf.template ./nginx/run_nginx.sh /tmp/

RUN ["chmod", "+x", "/tmp/run_nginx.sh"]
