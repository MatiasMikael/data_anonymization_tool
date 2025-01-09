"""
anonymize_data_gdpr.py

This script anonymizes data according to GDPR requirements.
Anonymized data is saved in the 2_data folder.
Logs are saved in the 5_logs folder.
"""

import os
import logging
import pandas as pd
import hashlib

# Set up logging
LOG_DIR = "5_logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "anonymize_data_gdpr.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def hash_value(value):
    """
    Hashes a value using SHA-256.

    Args:
        value (str): The value to hash.

    Returns:
        str: The hashed value.
    """
    return hashlib.sha256(value.encode()).hexdigest()

def mask_email(email):
    """
    Masks an email address by hiding part of it.

    Args:
        email (str): The email address to mask.

    Returns:
        str: The masked email address.
    """
    try:
        name, domain = email.split("@")
        masked_name = name[:2] + "****"
        return f"{masked_name}@{domain}"
    except Exception as e:
        logging.error("Error masking email: %s", str(e))
        return None

def mask_phone(phone):
    """
    Masks a phone number by hiding part of it.

    Args:
        phone (str): The phone number to mask.

    Returns:
        str: The masked phone number.
    """
    return phone[:3] + "-***-****"

def generalize_address(address):
    """
    Generalizes an address by keeping only the city name.

    Args:
        address (str): The address to generalize.

    Returns:
        str: The generalized address.
    """
    try:
        city = address.split("\n")[-1].split(",")[0]
        return city
    except Exception as e:
        logging.error("Error generalizing address: %s", str(e))
        return "Unknown"

def generalize_birthdate(birthdate):
    """
    Generalizes a birthdate to only include the year.

    Args:
        birthdate (str): The birthdate to generalize.

    Returns:
        str: The generalized birthdate (year only).
    """
    return birthdate[:4]

def anonymize_data(dataframe):
    """
    Applies GDPR-compliant anonymization techniques to a DataFrame.

    Args:
        dataframe (pd.DataFrame): The DataFrame to anonymize.

    Returns:
        pd.DataFrame: The anonymized DataFrame.
    """
    dataframe["Name"] = dataframe["Name"].apply(hash_value)
    dataframe["Email"] = dataframe["Email"].apply(mask_email)
    dataframe["Phone"] = dataframe["Phone"].apply(mask_phone)
    dataframe["Address"] = dataframe["Address"].apply(generalize_address)
    dataframe["Birthdate"] = dataframe["Birthdate"].astype(str).apply(generalize_birthdate)
    return dataframe

if __name__ == "__main__":
    try:
        print("Loading synthetic data...")
        logging.info("Loading synthetic data.")

        # Load the synthetic data
        input_path = "2_data/synthetic_data.csv"
        data = pd.read_csv(input_path)
        print("Data loaded successfully.")
        logging.info("Synthetic data loaded successfully from %s", input_path)

        # Apply anonymization
        print("Anonymizing data according to GDPR requirements...")
        logging.info("Starting GDPR-compliant data anonymization.")
        anonymized_data = anonymize_data(data)
        print("Data anonymized successfully.")
        logging.info("Data anonymized successfully.")

        # Save the anonymized data
        output_path = "2_data/anonymized_data_gdpr.csv"
        anonymized_data.to_csv(output_path, index=False)
        print(f"Anonymized data saved to {output_path}")
        logging.info("Anonymized data saved to %s", output_path)

    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error("An error occurred: %s", str(e))