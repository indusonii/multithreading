import threading
import time
import random
import unittest

def download_file(file_id):
    download_time = random.randint(1, 5)  # Random time between 1 and 5 seconds
    print(f"Starting download of file {file_id}... It will take {download_time} seconds.")
    time.sleep(download_time)  # Simulate download
    print(f"Download of file {file_id} completed in {download_time} seconds.")
    return file_id  # Return the file ID to indicate completion

def perform_other_task(task_id):
    task_time = random.randint(2, 4)  # Random time for other task
    print(f"Starting task {task_id}... It will take {task_time} seconds.")
    time.sleep(task_time)  # Simulate task work
    print(f"Task {task_id} completed in {task_time} seconds.")
    return task_id  # Return the task ID to indicate completion

def run_threads():
    file_ids = [1, 2, 3, 4, 5]
    task_ids = [1, 2, 3]

    download_threads = []
    for file_id in file_ids:
        thread = threading.Thread(target=download_file, args=(file_id,))
        download_threads.append(thread)
        thread.start()

    task_threads = []
    for task_id in task_ids:
        thread = threading.Thread(target=perform_other_task, args=(task_id,))
        task_threads.append(thread)
        thread.start()
    
    # Collect results from threads
    download_results = [thread.join() or thread for thread in download_threads]  # If join returns None, the thread itself is stored.
    task_results = [thread.join() or thread for thread in task_threads]
    
    print("All downloads and tasks are completed.")
    
    # Return results for verification
    return download_results, task_results


class TestMultithreading(unittest.TestCase):
    def test_thread_execution(self):
        download_results, task_results = run_threads()
        # Added assertions to check if all files were downloaded
        self.assertEqual(sorted([result.result() for result in download_results]), [1, 2, 3, 4, 5]) 
        # Added assertions to check if all other tasks were completed
        self.assertEqual(sorted([result.result() for result in task_results]), [1, 2, 3])  

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # exit=False to prevent SystemExit
