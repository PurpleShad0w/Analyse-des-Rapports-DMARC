package fr.ac6.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * The main class of the API. Used to launch the application. <br>
 * This API's purpose is to link System Workbench for Linux with a MySQL database that contains a record of all licenses and their details. <br>
 * SW4L will make an HTTP request to the API in order to retrieve the Status and Date of Validity of the license, and then proceed with software authentification. <br>
 * The nature of the call and its parameters are detailled in the MAIN mapping function of the Controller.
 * 
 * @see fr.ac6.api.controller.LicenseController
 * @author Octave
 */

@SpringBootApplication
public class LicenseApiApplication {

	public static void main(String[] args) {
		SpringApplication.run(LicenseApiApplication.class, args);
	}
}
