package fr.ac6.api.model;

import javax.persistence.Entity;
import javax.validation.constraints.NotBlank;

@Entity
public class Output {
    @NotBlank
    private String validUntil;

    @NotBlank
    private String status;
}