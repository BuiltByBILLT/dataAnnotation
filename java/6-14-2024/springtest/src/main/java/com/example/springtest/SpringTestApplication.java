package com.example.springtest;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class SpringTestApplication {

    public static void main(String[] args) {
        ApplicationContext context = SpringApplication.run(SpringTestApplication.class, args);
        ContentLocaliser contentLocaliser = context.getBean(ContentLocaliser.class);

        // Print the localeGroupMap to verify it is correctly injected
        // System.out.println(contentLocaliser.getLocaleGroupMap());
    }
}
