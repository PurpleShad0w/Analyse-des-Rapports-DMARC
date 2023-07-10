package fr.ac6.api.repository;

import fr.ac6.api.model.License;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface LicenseRepository extends JpaRepository<License, Long> {
    List<License> findByMacAddressAndLicenseFeature(String macAddress, String licenseFeature);
}