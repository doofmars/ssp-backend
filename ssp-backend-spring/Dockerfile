# dockerfile to conteainerize the java application
FROM eclipse-temurin:21

# copy the jar file to the container
COPY target/*.jar app.jar

# run the jar file
ENTRYPOINT ["java","-jar","/app.jar"]
