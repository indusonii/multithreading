import logging
import random
import threading
import time

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Change this to DEBUG for more detailed logs
)

def download_file(file_id):
    """
    Simulates downloading a file by sleeping for a random amount of time.
    
    Args:
    file_id (int): The unique identifier for the file being downloaded.
    
    Simulates a file download by waiting for a random period (1 to 5 seconds), 
    then logs the start and completion of the download process.
    """
    try:
        download_time = random.randint(1, 5)
        logging.info(f"Starting download of file {file_id}... It will take {download_time} seconds.")
        time.sleep(download_time)
        logging.info(f"Download of file {file_id} completed in {download_time} seconds.")
    except Exception as e:
        logging.error(f"An error occurred while downloading file {file_id}: {e}")

def perform_other_task(task_id):
    """
    Simulates performing another task by sleeping for a random amount of time.
    
    Args:
    task_id (int): The unique identifier for the task being performed.
    
    Simulates an additional task by waiting for a random period (2 to 4 seconds), 
    then logs the start and completion of the task.
    """
    try:
        task_time = random.randint(2, 4)
        logging.info(f"Starting task {task_id}... It will take {task_time} seconds.")
        time.sleep(task_time)
        logging.info(f"Task {task_id} completed in {task_time} seconds.")
    except Exception as e:
        logging.error(f"An error occurred while performing task {task_id}: {e}")

def start_download_threads(file_ids):
    """
    Creates and starts threads to download files concurrently.
    
    Args:
    file_ids (list): A list of file IDs that will be used to simulate downloading files.
    
    Returns:
    list: A list of threads that were started for the download tasks.
    
    This function will start a thread for each file in the file_ids list to simulate the file downloading.
    """
    download_threads = []
    for file_id in file_ids:
        try:
            thread = threading.Thread(target=download_file, args=(file_id,))
            download_threads.append(thread)
            thread.start()
        except Exception as e:
            logging.error(f"An error occurred while creating thread for downloading file {file_id}: {e}")
    return download_threads

def start_task_threads(task_ids):
    """
    Creates and starts threads to perform other tasks concurrently.
    
    Args:
    task_ids (list): A list of task IDs that will be used to simulate performing other tasks.
    
    Returns:
    list: A list of threads that were started for the tasks.
    
    This function will start a thread for each task in the task_ids list to simulate performing other tasks.
    """
    task_threads = []
    for task_id in task_ids:
        try:
            thread = threading.Thread(target=perform_other_task, args=(task_id,))
            task_threads.append(thread)
            thread.start()
        except Exception as e:
            logging.error(f"An error occurred while creating thread for task {task_id}: {e}")
    return task_threads

def wait_for_threads(threads, thread_type):
    """
    Waits for a list of threads to complete.
    
    Args:
    threads (list): A list of threads that need to be joined.
    thread_type (str): A string that specifies the type of thread (e.g., 'download' or 'task').
    
    This function will call `join()` on each thread to ensure the main program waits for all threads to finish.
    """
    for thread in threads:
        try:
            thread.join()
        except Exception as e:
            logging.error(f"An error occurred while waiting for {thread_type} thread to finish: {e}")

def main():
    """
    Main function to simulate file downloads and other tasks using threads.
    
    - Creates threads for downloading files with unique identifiers.
    - Creates threads for performing other tasks concurrently.
    - Waits for all threads to complete before finishing.
    
    This function orchestrates the process by first starting download and task threads, 
    and then waiting for them to finish before logging that all tasks are completed.
    """
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

