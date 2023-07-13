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

/**
 * This class is the controller of the API, it manages the HTTP requests we can send it.
 * The requests under REST Mappings are the classical methods to be used in case we need to modify the database without going through MySQL,
 * as a safeguard. The request under MAIN Mapping is the one to be called for general use. 
 * 
 * @author Octave
 */

@RestController
@RequestMapping("/api")
public class LicenseController {

    @Autowired
    LicenseRepository LicenseRepository;


    // REST Mappings

    /**
     * Request called at {host}/api/licenses.
     * No input required.
     * @return All registered licenses in the database.
     */

    @GetMapping("/licenses")
    public List<License> getAllLicenses() {
        return LicenseRepository.findAll();
    }

    /**
     * Request called at {host}/api/licenses.
     * @param License JSON-formatted license data.
     * @return Adds the given license to the database.
     */

    @PostMapping("/licenses")
    public License createLicense(@Valid @RequestBody License License) {
        return LicenseRepository.save(License);
    }

    /**
     * Request called at {host}/api/licenses/{api}.
     * @param LicenseId ID of the desired license.
     * @return License corresponding to the ID in JSON format.
     * @exception ResourceNotFoundException ID does not match any in database.
     * @see ResourceNotFoundException
     */

    @GetMapping("/licenses/{id}")
    public License getLicenseById(@PathVariable(value = "id") Long LicenseId) {
        return LicenseRepository.findById(LicenseId)
                .orElseThrow(() -> new ResourceNotFoundException("License", "id", LicenseId));
    }

    /**
     * Request called at {host}/api/licenses/{api}.
     * @param LicenseId ID of the license we wish to update.
     * @param LicenseDetails License we wish to update in JSON format.
     * @return Details of the updated license if successful.
     * @exception ResourceNotFoundException ID does not match any in database.
     * @see ResourceNotFoundException
     */

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

    /**
     * Request called at {host}/api/licenses/{api}.
     * @param LicenseId ID of the license we wish to delete.
     * @return Deletes the license corresponding to the ID in the database.
     * @exception ResourceNotFoundException ID does not match any in database.
     * @see ResourceNotFoundException
     */

    @DeleteMapping("/licenses/{id}")
    public ResponseEntity<?> deleteLicense(@PathVariable(value = "id") Long LicenseId) {
        License License = LicenseRepository.findById(LicenseId)
                .orElseThrow(() -> new ResourceNotFoundException("License", "id", LicenseId));

        LicenseRepository.delete(License);

        return ResponseEntity.ok().build();
    }


    // MAIN Mapping

    /**
     * Request called at {host}/api.
     * Expected input format:
     * {macAddress:###, licenseFeature:###}
     * Expected output format:
     * [{validUntil:###, status:###}, {}]
     * Returns list as a safeguard, should only ever contain one license.
     * @param macAddress MAC address of the computer we are requesting from.
     * @param licenseFeature Feature found in the license file, to differenciate products sold.
     * @return Sends back the Status and Validity Date of the license, in JSON format.
     */

    @GetMapping("")
    public ResponseEntity<List<License>> getLicenseByMacAddressAndLicenseFeature(@RequestParam String macAddress, @RequestParam String licenseFeature) {
		return new ResponseEntity<List<License>>(LicenseRepository.findByMacAddressAndLicenseFeature(macAddress, licenseFeature), HttpStatus.OK);
	}
}