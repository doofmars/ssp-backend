package de.doofmars.ssp;

import com.fasterxml.jackson.databind.Module;
import org.openapitools.jackson.nullable.JsonNullableModule;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FullyQualifiedAnnotationBeanNameGenerator;

@SpringBootApplication(
    nameGenerator = FullyQualifiedAnnotationBeanNameGenerator.class
)
@ComponentScan(
    basePackages = {"de.doofmars.ssp"},
    nameGenerator = FullyQualifiedAnnotationBeanNameGenerator.class
)
public class SSPBackend {

    public static void main(String[] args) {
        SpringApplication.run(SSPBackend.class, args);
    }

    @Bean(name = "de.doofmars.ssp.api.impl.OpenApiGeneratorApplication.jsonNullableModule")
    public Module jsonNullableModule() {
        return new JsonNullableModule();
    }

}