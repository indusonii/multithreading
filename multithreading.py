import threading
import time
import random
import logging

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Change this to DEBUG for more detailed logs
)

# Simulate downloading a file by sleeping for a random amount of time
def download_file(file_id):
    """
    Simulates downloading a file by sleeping for a random time between 1 and 5 seconds.
    
    Args:
    file_id (int): The unique identifier for the file being downloaded.
    """
    try:
        download_time = random.randint(1, 5)  # Random time between 1 and 5 seconds
        logging.info(f"Starting download of file {file_id}... It will take {download_time} seconds.")
        time.sleep(download_time)  # Simulate download
        logging.info(f"Download of file {file_id} completed in {download_time} seconds.")
    except Exception as e:
        logging.error(f"An error occurred while downloading file {file_id}: {e}")

# Function to simulate doing some other task while downloads are in progress
def perform_other_task(task_id):
    """
    Simulates performing another task by sleeping for a random time between 2 and 4 seconds.
    
    Args:
    task_id (int): The unique identifier for the task being performed.
    """
    try:
        task_time = random.randint(2, 4)  # Random time for other task
        logging.info(f"Starting task {task_id}... It will take {task_time} seconds.")
        time.sleep(task_time)  # Simulate task work
        logging.info(f"Task {task_id} completed in {task_time} seconds.")
    except Exception as e:
        logging.error(f"An error occurred while performing task {task_id}: {e}")

# Main function to run downloads and other tasks in parallel using threads
def main():
    """
    Main function that simulates multiple file downloads and other tasks being 
    performed concurrently using threads.
    
    - Creates threads for downloading files with unique identifiers.
    - Creates threads for performing other tasks concurrently.
    - Waits for all threads to complete before finishing.
    """
    try:
        # List of file IDs to simulate downloads
        file_ids = [1, 2, 3, 4, 5]

        # List of task IDs for the other tasks
        task_ids = [1, 2, 3]

        # Create threads for downloading files
        download_threads = []
        for file_id in file_ids:
            try:
                thread = threading.Thread(target=download_file, args=(file_id,))
                download_threads.append(thread)
                thread.start()
            except Exception as e:
                logging.error(f"An error occurred while creating thread for downloading file {file_id}: {e}")

        # Create threads for performing other tasks
        task_threads = []
        for task_id in task_ids:
            try:
                thread = threading.Thread(target=perform_other_task, args=(task_id,))
                task_threads.append(thread)
                thread.start()
            except Exception as e:
                logging.error(f"An error occurred while creating thread for task {task_id}: {e}")

        # Wait for all threads to complete
        for thread in download_threads:
            try:
                thread.join()
            except Exception as e:
                logging.error(f"An error occurred while waiting for download thread to finish: {e}")

        for thread in task_threads:
            try:
                thread.join()
            except Exception as e:
                logging.error(f"An error occurred while waiting for task thread to finish: {e}")

        logging.info("All downloads and tasks are completed.")
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
