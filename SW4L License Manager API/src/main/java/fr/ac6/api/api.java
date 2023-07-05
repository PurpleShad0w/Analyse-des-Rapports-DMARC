package fr.ac6.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@SpringBootApplication
@EnableJpaAuditing
public class API {

	public static void main(String[] args) {
		SpringApplication.run(API.class, args);
	}

}
