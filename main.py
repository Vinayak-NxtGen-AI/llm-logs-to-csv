from store_llm_logs import store_llm_log

# Example usage:
if __name__ == "__main__":
    log_data = {
        'username': 'Cool Doe',
        'user_message': 'Sup?',
        'assistant_message': 'I am doing well, thank you for asking.',
        'retrieved_docs': ['doc1', 'doc2'],
        'final_doc_output': 'This is the final output.',
    }

    store_llm_log(log_data)
