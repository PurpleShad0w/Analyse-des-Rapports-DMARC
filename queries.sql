DROP DATABASE DMARC;
CREATE DATABASE DMARC;
CREATE TABLE RUA (
    record_id INTEGER,
    org_name VARCHAR(255),
    org_email VARCHAR(255),
    org_extra_contact_info VARCHAR(255),
    report_id VARCHAR(255),
    begin_date VARCHAR(255),
    end_date VARCHAR(255),
    domain VARCHAR(255),
    adkim VARCHAR(255),
    aspf VARCHAR(255),
    p VARCHAR(255),
    sp VARCHAR(255),
    pct INTEGER,
    fo INTEGER,
    source_ip_address VARCHAR(255),
    source_country VARCHAR(255),
    lat VARCHAR(255),
    lon VARCHAR(255),
    source_reverse_dns VARCHAR(255),
    source_base_domain VARCHAR(255),
    count INTEGER,
    spf_aligned INTEGER,
    dkim_aligned INTEGER,
    dmarc_aligned INTEGER,
    disposition VARCHAR(255),
    policy_override_reasons VARCHAR(255),
    policy_override_comments VARCHAR(255),
    envelope_from VARCHAR(255),
    header_from VARCHAR(255),
    envelope_to VARCHAR(255),
    dkim_domain VARCHAR(255),
    dkim_selector VARCHAR(255),
    dkim_result VARCHAR(255),
    spf_domain VARCHAR(255),
    spf_scope VARCHAR(255),
    spf_result VARCHAR(255),
    PRIMARY KEY (record_id)
);
INSERT INTO RUA (record_id, org_name, org_email, org_extra_contact_info, report_id, begin_date, end_date,
    domain, adkim, aspf, p, sp, pct, fo, source_ip_address, source_country, lat, lon, source_reverse_dns, source_base_domain,
    count, spf_aligned, dkim_aligned, dmarc_aligned, disposition, policy_override_reasons, policy_override_comments,
    envelope_from, header_from, envelope_to, dkim_domain, dkim_selector, dkim_result, spf_domain, spf_scope,
    spf_result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
ALTER TABLE RUA
ADD time DATE AS (CAST(begin_date AS DATE));
ALTER TABLE RUA
ADD dkim_pass INTEGER AS (CASE WHEN dkim_result = 'pass' THEN 1 * count ELSE 0 END);
ALTER TABLE RUA
ADD dkim_fail INTEGER AS (CASE WHEN dkim_result = 'fail' THEN 1 * count ELSE 0 END);
ALTER TABLE RUA
ADD spf_pass INTEGER AS (CASE WHEN spf_result = 'pass' THEN 1 * count ELSE 0 END);
ALTER TABLE RUA
ADD spf_fail INTEGER AS (CASE WHEN spf_result = 'fail' THEN 1 * count ELSE 0 END);
ALTER TABLE RUA
ADD dispo_none INTEGER AS (CASE WHEN disposition = 'none' THEN 1 * count ELSE 0 END);
ALTER TABLE RUA
ADD dispo_quarantine INTEGER AS (CASE WHEN disposition = 'quarantine' THEN 1 * count ELSE 0 END);
ALTER TABLE RUA
ADD dispo_reject INTEGER AS (CASE WHEN disposition = 'reject' THEN 1 * count ELSE 0 END);
ALTER TABLE RUA
ADD dkim_unaligned INTEGER AS (CASE WHEN dkim_aligned = 0 THEN 1 * count ELSE 0 END);
ALTER TABLE RUA
ADD spf_unaligned INTEGER AS (CASE WHEN spf_aligned = 0 THEN 1 * count ELSE 0 END);
ALTER TABLE RUA
ADD dmarc_unaligned INTEGER AS (CASE WHEN dmarc_aligned = 0 THEN 1 * count ELSE 0 END);
ALTER TABLE RUA
ADD dkim_aligned_w INTEGER AS (dkim_aligned * count);
ALTER TABLE RUA
ADD spf_aligned_w INTEGER AS (spf_aligned * count);
ALTER TABLE RUA
ADD dmarc_aligned_w INTEGER AS (dmarc_aligned * count);
SELECT * FROM RUA;