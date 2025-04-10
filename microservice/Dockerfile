FROM openjdk:17
EXPOSE 8081
ADD target/microservice-0.0.1-SNAPSHOT.jar microservice.jar
LABEL authors="AZIZ LAAROUSSI"
ENTRYPOINT ["java", "-jar", "/microservice.jar"]