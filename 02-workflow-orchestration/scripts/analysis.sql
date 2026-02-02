-- Module 2 Homework Verification Queries

-- Question 3: Count rows for Yellow Taxi 2020
SELECT COUNT(*) 
FROM yellow_tripdata 
WHERE filename LIKE 'yellow_tripdata_2020-%';

-- Question 4: Count rows for Green Taxi 2020
SELECT COUNT(*) 
FROM green_tripdata 
WHERE filename LIKE 'green_tripdata_2020-%';

-- Question 5: Count rows for Yellow Taxi March 2021
SELECT COUNT(*) 
FROM yellow_tripdata 
WHERE filename = 'yellow_tripdata_2021-03.csv';
