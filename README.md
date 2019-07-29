# FLASK-PRIME-NUMBER-CHECK

### Please follow below steps to run this project

- Clone git repository

    ``` git clone https://github.com/ckhare4992/flask-prime-number.git ```


- Pull mysql docker image

    ``` docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:latest ```

- Build application docker container

    ``` docker build -t flask-prime-check . ```

- Run the application container

    ``` docker run -v ${PWD}:/flask-prime-number/ -e MYSQL_HOSTNAME=$HOSTNAME -p 9000:9000 -d flask-prime-check ```

    This command will mount the present directory inside the container and pass system hostname as MYSQL_HOSTNAME as env variable to be used by application for connecting mysql server



