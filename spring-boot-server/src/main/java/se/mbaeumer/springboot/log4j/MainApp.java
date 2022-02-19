package se.mbaeumer.springboot.log4j;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

@SpringBootApplication
@EnableWebMvc
public class MainApp {
    public static void main(String[] args){
        SpringApplication.run(MainApp.class, args);
    }
}
