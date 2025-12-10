
-- SQL Script for Claims Data Cleaning and Aggregation

SELECT 
    claim_id,
    patient_age,
    claim_amount,
    diagnosis_code,
    procedure_code,
    claim_status,
    days_to_process,
    risk_score
FROM claims_data
WHERE claim_amount > 0;
