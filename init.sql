CREATE TABLE conso_elec_gaz
(
    id SERIAL PRIMARY KEY,
    residential_consumption FLOAT,
    number_residential_points INT,
    quality_residential_index FLOAT,
    postal_code INT,
    region_code INT
);

INSERT INTO conso_elec_gaz (residential_consumption, number_residential_points, quality_residential_index, postal_code, region_code)
 VALUES
 (26986.60, 4245, 0.381, 35069,53),
 (5707.59, 855, 0.369, 35094, 53),
 (3965.59, 618, 0.412, 37001, 24);