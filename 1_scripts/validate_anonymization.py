"""
validate_anonymization.py

This script validates the anonymization process for GDPR compliance.
Validation includes checking that PII has been anonymized and the data remains usable.
Logs and reports are saved in the 5_logs and 3_results folders.
"""

import os
import logging
import pandas as pd

# Set up logging
LOG_DIR = "5_logs"
RESULTS_DIR = "3_results"
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "validate_anonymization.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def check_anonymization(dataframe):
    """
    Checks that sensitive fields have been anonymized.

    Args:
        dataframe (pd.DataFrame): The anonymized DataFrame.

    Returns:
        dict: A dictionary with validation results.
    """
    results = {}
    results["Name_Anonymized"] = all(dataframe["Name"].astype(str).str.len() == 64)  # SHA-256 length
    results["Email_Masked"] = all(dataframe["Email"].fillna("").astype(str).str.contains("\*\*\*\*"))
    results["Phone_Masked"] = all(dataframe["Phone"].fillna("").astype(str).str.contains("\*\*\*"))
    results["Address_Generalized"] = all(dataframe["Address"].fillna("").astype(str).str.len() < 30)  # Example heuristic
    results["Birthdate_Generalized"] = all(dataframe["Birthdate"].fillna("").astype(str).str.len() == 4)
    return results

def data_utility_check(dataframe):
    """
    Performs basic utility checks to ensure anonymized data is still usable.

    Args:
        dataframe (pd.DataFrame): The anonymized DataFrame.

    Returns:
        dict: A dictionary with data utility results.
    """
    results = {}
    results["Record_Count"] = len(dataframe)
    results["Unique_Names"] = dataframe["Name"].nunique()  # Ensures diversity remains
    results["Unique_Emails"] = dataframe["Email"].nunique()
    return results

if __name__ == "__main__":
    try:
        print("Loading anonymized data...")
        logging.info("Loading anonymized data.")

        # Load anonymized data
        input_path = "2_data/anonymized_data_gdpr.csv"
        data = pd.read_csv(input_path)
        print("Data loaded successfully.")
        logging.info("Anonymized data loaded successfully from %s", input_path)

        # Perform validation checks
        print("Validating anonymization...")
        logging.info("Starting anonymization validation.")
        anonymization_results = check_anonymization(data)
        for key, value in anonymization_results.items():
            print(f"{key}: {'Passed' if value else 'Failed'}")
            logging.info("%s: %s", key, "Passed" if value else "Failed")

        # Perform data utility checks
        print("Checking data utility...")
        logging.info("Starting data utility checks.")
        utility_results = data_utility_check(data)
        for key, value in utility_results.items():
            print(f"{key}: {value}")
            logging.info("%s: %s", key, value)

        # Save validation report
        report_path = os.path.join(RESULTS_DIR, "validation_report.txt")
        with open(report_path, "w") as report_file:
            report_file.write("Anonymization Validation Results:\n")
            for key, value in anonymization_results.items():
                report_file.write(f"{key}: {'Passed' if value else 'Failed'}\n")
            report_file.write("\nData Utility Results:\n")
            for key, value in utility_results.items():
                report_file.write(f"{key}: {value}\n")

        print(f"Validation report saved to {report_path}")
        logging.info("Validation report saved to %s", report_path)

    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error("An error occurred: %s", str(e))