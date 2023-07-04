package fr.ac6.api.controller;

import fr.ac6.api.model.LicenseModel;
import fr.ac6.api.service.LicenseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.MediaType;

import java.util.List;
import java.util.NoSuchElementException;

@RestController
@RequestMapping(path = "api/license", produces = MediaType.APPLICATION_JSON_VALUE)
public class LicenseController {
    @Autowired
    LicenseService service;

    public LicenseController(LicenseService service) {
        this.service = service;
    }

    @PostMapping
    public List<LicenseModel> listAllLicense() {
        return service.listAllLicense();
    }
}