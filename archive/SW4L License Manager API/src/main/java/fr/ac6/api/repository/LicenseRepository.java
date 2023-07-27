package fr.ac6.api.repository;

import fr.ac6.api.model.License;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * This class defines the Repository corresponding to the MySQL database. <br>
 * It is called by the controller and responds by calling it functions. <br>
 * It contains several default functions, and custom ones like the main function we use.
 * 
 * @author Octave
 */

@Repository
public interface LicenseRepository extends JpaRepository<License, Long> {

    /**
     * Uses the MAC address and license Feature to fetch the Validity Date and Status.
     * @param macAddress MAC address of the computer we are requesting from.
     * @param licenseFeature Feature found in the license file, to differenciate products sold.
     * @return Sends back the Status and Validity Date of the license, in JSON format. <br>
     * This function works automatically through the JPA Repository system via its name,
     * so it should never be renamed unless we mean to change what it does.
     */

    List<License> mainRequest(String macAddress, String licenseFeature);
}