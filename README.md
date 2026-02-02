# Module 2 Homework: Workflow Orchestration

This folder contains the Kestra flows and solutions for the Module 2 homework.

## Project Structure

- `flows/`: Contains the YAML flow definitions for Kestra.
  - `06_gcp_taxi_scheduled.yaml`: Main ETL flow with Backfill and Schedule triggers.
- `docker-compose.yml`: Configuration to run Kestra locally.

## Setup & Execution

1. **Start Kestra:**
   ```bash
   docker compose up -d
   ```
2. **Access UI:** Go to `http://localhost:8080`.
3. **Create Flow:** Copy the content of `flows/06_gcp_taxi_scheduled.yaml` into the Kestra editor.
4. **Backfill:** Execute the flow using the "Backfill" button for the year 2021 (Jan-Jul) as requested.

---

## Quiz Solutions

### Question 1. Uncompressed file size for Yellow Taxi 2020-12
*Answer:* `128.3 MiB`

### Question 2. Rendered value of the variable file
*Answer:* `green_tripdata_2020-04.csv`

### Question 3. Rows for Yellow Taxi data (2020)
*Answer:* `24,648,499`

### Question 4. Rows for Green Taxi data (2020)
*Answer:* `1,734,051`

### Question 5. Rows for Yellow Taxi data (March 2021)
*Answer:* `1,925,152`

### Question 6. Timezone configuration
*Answer:* `Add a timezone property set to America/New_York in the Schedule trigger configuration`
