package fr.ac6.api.repository;

import fr.ac6.api.model.LicenseModel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface LicenseRepository extends JpaRepository<LicenseModel, Integer> {
}