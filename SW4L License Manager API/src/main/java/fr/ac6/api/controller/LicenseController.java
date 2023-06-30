package fr.ac6.api.controller;

import fr.ac6.api.model.License;
import fr.ac6.api.service.LicenseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.NoSuchElementException;

@RestController
@RequestMapping("/licenses")
public class LicenseController {
    @Autowired
    LicenseService licenseService;

    @GetMapping("")
    public List<License> list() {
        return licenseService.listAllLicense();
    }

    @GetMapping("/{id}")
    public ResponseEntity<License> get(@PathVariable Integer id) {
        try {
            License license = licenseService.getLicense(id);
            return new ResponseEntity<License>(license, HttpStatus.OK);
        } catch (NoSuchElementException e) {
            return new ResponseEntity<License>(HttpStatus.NOT_FOUND);
        }
    }

    @PostMapping("/")
    public void add(@RequestBody License license) {
        licenseService.saveLicense(license);
    }

    @PutMapping("/{id}")
    public ResponseEntity<?> update(@RequestBody License license, @PathVariable Integer id) {
        try {
            License existLicense = licenseService.getLicense(id);
            existLicense.setRecord(id);
            licenseService.saveLicense(existLicense);
            return new ResponseEntity<>(HttpStatus.OK);
        } catch (NoSuchElementException e) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Integer id) {

        licenseService.deleteLicense(id);
    }
}