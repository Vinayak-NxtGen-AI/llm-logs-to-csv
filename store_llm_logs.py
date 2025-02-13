"""
This module provides functionality for logging API interactions to an Excel file.

It includes a single function, `store_llm_log`, which takes in log data and writes it to 
an Excel file. The log data is expected to be a dictionary containing information about 
the API interaction, such as the endpoint, request method, and status code.

The module uses pandas for handling and manipulating the Excel file.
"""

from datetime import datetime
import pandas as pd
import pytz

# File path to which the logs will be stored
DEFAULT_LOG_FILE_PATH = 'ECI_hindi_rag_logs.csv'

# LLM model being used in our RAG
LLM_MODEL = 'meta/llama-3.1-70b-instruct'

def store_llm_log(log_data, file_path = DEFAULT_LOG_FILE_PATH):
    """
    Store API log data in an Excel file.

    Args:
        log_data (dict): Dictionary containing API log data.
        file_path (str): Path to the Excel file.

    Returns:
        None
    """

    # Define the headers for the Excel file
    headers = [
        'Timestamp', 
        'Username', 
        'User Message', 
        'Assistant Message', 
        'Retrieved Docs', 
        'Final Doc Output', 
        'LLM Model'
    ]

    # Create a new row with the log data and headers
    new_row = pd.DataFrame({
        headers[0]: [datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d-%m-%Y %I:%M:%S %p')],
        headers[1]: [log_data.get('username', '')],
        headers[2]: [log_data.get('user_message', '')],
        headers[3]: [log_data.get('assistant_message', '')],
        headers[4]: [log_data.get('retrieved_docs', '')],
        headers[5]: [log_data.get('final_doc_output', '')],
        headers[6]: [log_data.get('llm_model', LLM_MODEL)]
    })

    # Check if the file exists
    try:
        # If the file exists, load it into a pandas DataFrame and append the new row
        df = pd.read_csv(file_path)
        df = pd.concat([df, new_row], ignore_index=True)

    except FileNotFoundError:
        # If the file does not exist, use the new row as the DataFrame
        df = new_row

    print("Ran bro")
    # Write the DataFrame to the Excel file
    df.to_csv(file_path, index=False)
