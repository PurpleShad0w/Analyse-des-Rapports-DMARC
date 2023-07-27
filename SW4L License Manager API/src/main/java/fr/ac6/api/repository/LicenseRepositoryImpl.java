package fr.ac6.api.repository;

import org.springframework.stereotype.Component;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.List;
import fr.ac6.api.model.Input;
import javax.persistence.PersistenceContext;
import javax.persistence.EntityManager;
import javax.persistence.TypedQuery;

@Component
public class LicenseRepositoryImpl {

    @PersistenceContext
    private EntityManager entityManager;

    @Autowired
    LicenseRepository LicenseRepository;

    @SuppressWarnings("unused")
    public List<Input> mainRequest(String macAddress, String licenseFeature) {
        String hql = "SELECT e FROM Input e WHERE e.mac_address = :mac_address AND e.license_feature = :license_feature";
        TypedQuery<Input> query = entityManager.createQuery(hql, Input.class);
        query.setParameter("mac_address", macAddress);
        query.setParameter("license_feature", licenseFeature);
        return query.getResultList();
    }
}
