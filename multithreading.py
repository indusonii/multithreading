import threading
import time
import random

# Simulate downloading a file by sleeping for a random amount of time
def download_file(file_id):
    download_time = random.randint(1, 5)  # Random time between 1 and 5 seconds
    print(f"Starting download of file {file_id}... It will take {download_time} seconds.")
    time.sleep(download_time)  # Simulate download
    print(f"Download of file {file_id} completed in {download_time} seconds.")

# Function to simulate doing some other task while downloads are in progress
def perform_other_task(task_id):
    task_time = random.randint(2, 4)  # Random time for other task
    print(f"Starting task {task_id}... It will take {task_time} seconds.")
    time.sleep(task_time)  # Simulate task work
    print(f"Task {task_id} completed in {task_time} seconds.")

# Main function to run downloads and other tasks in parallel using threads
def main():
    # List of file IDs to simulate downloads
    file_ids = [1, 2, 3, 4, 5]

    # List of task IDs for the other tasks
    task_ids = [1, 2, 3]

    # Create threads for downloading files
    download_threads = []
    for file_id in file_ids:
        thread = threading.Thread(target=download_file, args=(file_id,))
        download_threads.append(thread)
        thread.start()

    # Create threads for performing other tasks
    task_threads = []
    for task_id in task_ids:
        thread = threading.Thread(target=perform_other_task, args=(task_id,))
        task_threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in download_threads:
        thread.join()

    for thread in task_threads:
        thread.join()

    print("All downloads and tasks are completed.")

if __name__ == "__main__":
    main()
