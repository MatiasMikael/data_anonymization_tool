"""
generate_synthetic_data.py

This script generates synthetic data for testing data anonymization tools.
The generated data includes names, emails, phone numbers, addresses, and birthdates.
Logs are saved in the 5_logs folder.
"""

import os
import logging
from faker import Faker
import pandas as pd

# Set up logging
LOG_DIR = "5_logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "generate_synthetic_data.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def generate_synthetic_data(num_records=100):
    """
    Generates synthetic data using the Faker library.

    Args:
        num_records (int): Number of records to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the synthetic data.
    """
    fake = Faker()
    data = {
        "Name": [fake.name() for _ in range(num_records)],
        "Email": [fake.email() for _ in range(num_records)],
        "Phone": [fake.phone_number() for _ in range(num_records)],
        "Address": [fake.address() for _ in range(num_records)],
        "Birthdate": [fake.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(num_records)],
    }
    return pd.DataFrame(data)

def save_data_to_csv(dataframe, file_path):
    """
    Saves a DataFrame to a CSV file.

    Args:
        dataframe (pd.DataFrame): The DataFrame to save.
        file_path (str): Path to the CSV file.
    """
    dataframe.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")
    logging.info("Data successfully saved to %s", file_path)

if __name__ == "__main__":
    try:
        print("Generating synthetic data...")
        logging.info("Starting synthetic data generation.")
        
        # Generate synthetic data
        num_records = 100
        synthetic_data = generate_synthetic_data(num_records)
        
        print(f"{num_records} records generated successfully.")
        logging.info("%d records generated successfully.", num_records)

        # Save the data to a CSV file
        output_path = "2_data/synthetic_data.csv"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        save_data_to_csv(synthetic_data, output_path)

    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error("An error occurred: %s", str(e))