import logging
import random
import threading
import time

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Change this to DEBUG for more detailed logs
)

# Simulate downloading a file by sleeping for a random amount of time
def download_file(file_id):
    try:
        download_time = random.randint(1, 5)
        logging.info(f"Starting download of file {file_id}... It will take {download_time} seconds.")
        time.sleep(download_time)
        logging.info(f"Download of file {file_id} completed in {download_time} seconds.")
    except Exception as e:
        logging.error(f"An error occurred while downloading file {file_id}: {e}")

# Simulate doing another task while downloads are in progress
def perform_other_task(task_id):
    try:
        task_time = random.randint(2, 4)
        logging.info(f"Starting task {task_id}... It will take {task_time} seconds.")
        time.sleep(task_time)
        logging.info(f"Task {task_id} completed in {task_time} seconds.")
    except Exception as e:
        logging.error(f"An error occurred while performing task {task_id}: {e}")

# Function to create and start threads for downloading files
def start_download_threads(file_ids):
    download_threads = []
    for file_id in file_ids:
        try:
            thread = threading.Thread(target=download_file, args=(file_id,))
            download_threads.append(thread)
            thread.start()
        except Exception as e:
            logging.error(f"An error occurred while creating thread for downloading file {file_id}: {e}")
    return download_threads

# Function to create and start threads for performing other tasks
def start_task_threads(task_ids):
    task_threads = []
    for task_id in task_ids:
        try:
            thread = threading.Thread(target=perform_other_task, args=(task_id,))
            task_threads.append(thread)
            thread.start()
        except Exception as e:
            logging.error(f"An error occurred while creating thread for task {task_id}: {e}")
    return task_threads

# Function to wait for threads to complete
def wait_for_threads(threads, thread_type):
    for thread in threads:
        try:
            thread.join()
        except Exception as e:
            logging.error(f"An error occurred while waiting for {thread_type} thread to finish: {e}")

# Main function orchestrating downloads and tasks
def main():
    try:
        # List of file IDs to simulate downloads
        file_ids = [1, 2, 3, 4, 5]

        # List of task IDs for the other tasks
        task_ids = [1, 2, 3]

        # Start download threads
        download_threads = start_download_threads(file_ids)

        # Start task threads
        task_threads = start_task_threads(task_ids)

        # Wait for all threads to complete
        wait_for_threads(download_threads, "download")
        wait_for_threads(task_threads, "task")

        logging.info("All downloads and tasks are completed.")
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
