package fr.ac6.api.model;

import jakarta.persistence.*;

@Entity
@Table(name = "LICENSES")
public class License {
    private int record;
    private String mac;
    private String email;
    private String type;
    private String feature;
    private String until;
    private String key;

    public License() {
    }

    public License(int record, String mac, String email, String type, String feature, String until, String key) {
        this.record = record;
        this.mac = mac;
        this.email = email;
        this.type = type;
        this.feature = feature;
        this.until = until;
        this.key = key;
    }

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    public int getRecord() {
        return record;
    }

    public void setRecord(int record) {
        this.record = record;
    }

    public String getMac() {
        return mac;
    }

    public void setMac(String mac) {
        this.mac = mac;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }

    public String getUntil() {
        return until;
    }

    public void setUntil(String until) {
        this.until = until;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
}
