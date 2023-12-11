FROM eclipse-temurin:21-jre-alpine

COPY ./build/libs/ssp-backend.jar /root/ssp-backend.jar

WORKDIR /root

CMD ["java", "-server", "-Xms4g", "-Xmx4g", "-XX:+UseG1GC", "-XX:MaxGCPauseMillis=100", "-XX:+UseStringDeduplication", "-jar", "ssp-backend.jar"]