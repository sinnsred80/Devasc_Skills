#!/bin/bash

mkdir tempdir

cp index.html tempdir/.

echo "FROM ubuntu" > tempdir/Dockerfile
echo "RUN apt-get update" >> tempdir/Dockerfile
echo "RUN apt-get install -y tzdata" >> tempdir/Dockerfile
echo "ENV TZ=Europe/ETC" >> tempdir/Dockerfile
echo "RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone" >> tempdir/Dockerfile
echo "RUN apt-get install -y apache2" >> tempdir/Dockerfile
echo "RUN apt-get install -y apache2-utils" >> tempdir/Dockerfile
echo "RUN apt-get clean" >> tempdir/Dockerfile
echo "RUN sed -i 's/Listen 80/Listen 8081/g' /etc/apache2/ports.conf" >> tempdir/Dockerfile
echo "RUN sed -i 's/<VirtualHost *:80>/<VirtualHost *:8081>/g' /etc/apache2/sites-enabled/000-default.conf" >> tempdir/Dockerfile
echo "COPY index.html /var/www/html/" >> tempdir/Dockerfile
echo "EXPOSE 8081" >> tempdir/Dockerfile
echo "CMD ["apache2ctl", "-D", "FOREGROUND"]" >> tempdir/Dockerfile

cd tempdir

# Build, run and verify apache Docker image and container.

echo -e "\n\n- Building Docker apache image.\n"
docker build -t apache_image .

echo -e "\n- Run apache Docker Container.\n"
docker run -t -d -p 8081:8081 --name apache_run apache_image

echo -e "\n- Verify apache Docker Container is running.\n"
docker ps