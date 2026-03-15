-- ==========================================
-- NovaParcel Database - PARCEL SUMMARY
-- ==========================================

CREATE TABLE parcels_summary
(
    delivery_id INT PRIMARY KEY,
    delivery_date DATE,
    product_id INT,
    customer_id INT,
    planet_id INT,
    product_name VARCHAR,
    product_price NUMERIC,
    vehicle_type_id INT,
    vehicle_cost NUMERIC,
    region VARCHAR,
    load_date DATE,
    process_name VARCHAR,
    user_id VARCHAR
);

INSERT INTO parcels_summary(
	delivery_id, delivery_date, product_id, customer_id, planet_id, product_name, product_price, vehicle_type_id, vehicle_cost, region, load_date, process_name, user_id)
SELECT 
	DEL.id, DEL.delivery_date, PRO.id, DEL.customer_id, CUS.country_id, PRO.name, CAST(PRO.price AS NUMERIC), PRO.vehicle_type_id, VEH.cost, PLA.region, CURRENT_DATE, 'initial load', 'GPBV'
FROM delivery DEL
INNER JOIN product PRO ON DEL.product_id = PRO.id
INNER JOIN vehicle_type VEH ON PRO.vehicle_type_id = VEH.id
INNER JOIN customer CUS ON DEL.customer_id = CUS.id
INNER JOIN planet PLA ON CUS.country_id = PLA.id;

CREATE TABLE parcels_summary_monthly
(
    yyyymm VARCHAR,
    product_name VARCHAR,
    parcel_count INT,
    region VARCHAR,
    profit NUMERIC
);

INSERT INTO parcels_summary_monthly(
	yyyymm, product_name, parcel_count, region, profit)
SELECT TO_CHAR(delivery_date, 'YYYYMM') AS YYYYMM, product_name, COUNT(delivery_id), region, SUM(product_price) - SUM(vehicle_cost)
FROM parcels_summary
GROUP BY YYYYMM, product_name, region;