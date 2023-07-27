package fr.ac6.api.model;

import javax.persistence.Entity;
import javax.validation.constraints.NotBlank;

@Entity
public class Input {
    @NotBlank
    private String macAddress;

    @NotBlank
    private String licenseFeature;

    public String getMacAddress() {
        return macAddress;
    }

    public String getLicenseFeature() {
        return licenseFeature;
    }
}