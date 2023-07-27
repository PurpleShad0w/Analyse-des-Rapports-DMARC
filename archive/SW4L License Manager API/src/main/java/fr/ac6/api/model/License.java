package fr.ac6.api.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import javax.persistence.*;
import javax.validation.constraints.NotBlank;
import java.util.Date;

/**
 * This class defines the model of what a "License" is, such as each of its features (also called Details). <br>
 * Within the definition of a License also resides simple functions meant to allow each feature to become a variable. <br>
 * As such, individual functions do not need to be documented here, and as a rule of thumb,
 * each feature is defined once, has one function to input a value and one function to output a value.
 * 
 * @author Octave
 */

@Entity
@Table(name = "licenses")
@EntityListeners(AuditingEntityListener.class)
@JsonIgnoreProperties(value = {"validUntil"}, allowGetters = true)
public class License {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank
    private String macAddress;

    @NotBlank
    private String licenseFeature;

    @NotBlank
    private String licenseType;

    @NotBlank
    private String licenseKey;

    @Column(nullable = false)
    @Temporal(TemporalType.TIMESTAMP)
    private Date validUntil;

    @NotBlank
    private String status;


    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getMacAddress() {
        return macAddress;
    }

    public void setMacAddress(String macAddress) {
        this.macAddress = macAddress;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getLicenseType() {
        return licenseType;
    }

    public void setLicenseType(String licenseType) {
        this.licenseType = licenseType;
    }

    public String getLicenseFeature() {
        return licenseFeature;
    }

    public void setLicenseFeature(String licenseFeature) {
        this.licenseFeature = licenseFeature;
    }

    public Date getValidUntil() {
        return validUntil;
    }

    public void setValidUntil(Date validUntil) {
        this.validUntil = validUntil;
    }

    public String getLicenseKey() {
        return licenseKey;
    }

    public void setLicenseKey(String licenseKey) {
        this.licenseKey = licenseKey;
    }
}
