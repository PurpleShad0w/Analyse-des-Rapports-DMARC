package fr.ac6.api.controller;

import fr.ac6.api.model.License;
import fr.ac6.api.repository.LicenseRepository;
import fr.ac6.api.service.LicenseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.MediaType;

import java.util.List;
import java.util.NoSuchElementException;

@RestController
@RequestMapping(path = "/api")
public class LicenseController {

    @Autowired
    LicenseRepository licenseRepository;

    @GetMapping("/licenses")
    public List<License> listAllLicenses() {
        return licenseRepository.findAll();
    }
}