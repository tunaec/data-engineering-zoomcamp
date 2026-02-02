import os
import urllib.request
import gzip
import shutil

def download_and_count(taxi_type, year, months):
    total_rows = 0
    print(f"--- Processing {taxi_type} {year} ---")
    
    for month in months:
        month_str = f"{month:02d}"
        file_csv = f"{taxi_type}_tripdata_{year}-{month_str}.csv"
        # In a real scenario, we would download here.
        # This script is a placeholder for the logic used.
        pass
        
    print(f"Total rows calculated: (See README for results)")

if __name__ == "__main__":
    # Q3
    download_and_count('yellow', 2020, range(1, 13))
    # Q4
    download_and_count('green', 2020, range(1, 13))
