package fr.ac6.api.controller;

import fr.ac6.api.exception.ResourceNotFoundException;
import fr.ac6.api.model.License;
import fr.ac6.api.repository.LicenseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.HttpStatus;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("/api")
public class LicenseController {

    @Autowired
    LicenseRepository LicenseRepository;


    // REST Mappings

    @GetMapping("/licenses")
    public List<License> getAllLicenses() {
        return LicenseRepository.findAll();
    }

    @PostMapping("/licenses")
    public License createLicense(@Valid @RequestBody License License) {
        return LicenseRepository.save(License);
    }

    @GetMapping("/licenses/{id}")
    public License getLicenseById(@PathVariable(value = "id") Long LicenseId) {
        return LicenseRepository.findById(LicenseId)
                .orElseThrow(() -> new ResourceNotFoundException("License", "id", LicenseId));
    }

    @PutMapping("/licenses/{id}")
    public License updateLicense(@PathVariable(value = "id") Long LicenseId,
                                           @Valid @RequestBody License LicenseDetails) {

        License License = LicenseRepository.findById(LicenseId)
                .orElseThrow(() -> new ResourceNotFoundException("License", "id", LicenseId));

        License.setMacAddress(LicenseDetails.getMacAddress());
        License.setLicenseFeature(LicenseDetails.getLicenseFeature());
        License.setLicenseType(LicenseDetails.getLicenseType());
        License.setLicenseKey(LicenseDetails.getLicenseKey());
        License.setValidUntil(LicenseDetails.getValidUntil());
        License.setStatus(LicenseDetails.getStatus());

        License updatedLicense = LicenseRepository.save(License);
        return updatedLicense;
    }

    @DeleteMapping("/licenses/{id}")
    public ResponseEntity<?> deleteLicense(@PathVariable(value = "id") Long LicenseId) {
        License License = LicenseRepository.findById(LicenseId)
                .orElseThrow(() -> new ResourceNotFoundException("License", "id", LicenseId));

        LicenseRepository.delete(License);

        return ResponseEntity.ok().build();
    }


    // POST Mappings

    @GetMapping("")
    public ResponseEntity<List<License>> getLicenseByMacAddressAndLicenseFeature(@RequestParam String macAddress, @RequestParam String licenseFeature) {
		return new ResponseEntity<List<License>>(LicenseRepository.findByMacAddressAndLicenseFeature(macAddress, licenseFeature), HttpStatus.OK);
	}
}