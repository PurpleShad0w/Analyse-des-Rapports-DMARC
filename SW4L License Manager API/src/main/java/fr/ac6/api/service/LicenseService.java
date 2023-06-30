package fr.ac6.api.service;

import fr.ac6.api.model.License;
import fr.ac6.api.repository.LicenseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import jakarta.transaction.Transactional;
import java.util.List;
@Service
@Transactional
public class LicenseService {
    @Autowired
    private LicenseRepository licenseRepository;
    public List<License> listAllLicense() {
        return licenseRepository.findAll();
    }

    public void saveLicense(License license) {
        licenseRepository.save(license);
    }

    public License getLicense(Integer id) {
        return licenseRepository.findById(id).get();
    }

    public void deleteLicense(Integer id) {
        licenseRepository.deleteById(id);
    }
}