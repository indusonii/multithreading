import unittest
from unittest.mock import patch
import logging
import threading
import time
import random

# Import the functions from the original script
# Assuming the script is named 'threading_script.py'
# from threading_script import download_file, perform_other_task, main

class TestMultithreading(unittest.TestCase):
    
    @patch('time.sleep', return_value=None)  # Mocking time.sleep to avoid actual delays
    @patch('logging.info')  # Mocking logging.info to capture info logs
    @patch('logging.error')  # Mocking logging.error to capture error logs
    def test_thread_creation_and_completion(self, mock_logging_error, mock_logging_info, mock_sleep):
        """
        Test that threads for downloading files and performing tasks are correctly created, started, and finished.
        """
        file_ids = [1, 2, 3, 4, 5]
        task_ids = [1, 2, 3]

        download_threads = []
        task_threads = []

        # Create threads for downloading files
        for file_id in file_ids:
            thread = threading.Thread(target=download_file, args=(file_id,))
            download_threads.append(thread)
            thread.start()

        # Create threads for performing other tasks
        for task_id in task_ids:
            thread = threading.Thread(target=perform_other_task, args=(task_id,))
            task_threads.append(thread)
            thread.start()

        # Join threads to ensure they have finished
        for thread in download_threads:
            thread.join()

        for thread in task_threads:
            thread.join()

        # Assert that the number of threads created is correct
        self.assertEqual(len(download_threads), len(file_ids))
        self.assertEqual(len(task_threads), len(task_ids))

        # Check if logging.info was called for each file download and task completion
        mock_logging_info.assert_any_call("Starting download of file 1...")  # Example for file 1
        mock_logging_info.assert_any_call("Starting task 1...")  # Example for task 1

        # Ensure logging of task completion and download completion
        mock_logging_info.assert_any_call("Download of file 1 completed in")  # Example for download
        mock_logging_info.assert_any_call("Task 1 completed in")  # Example for task

        # Verify that no errors occurred
        mock_logging_error.assert_not_called()

    @patch('time.sleep', return_value=None)  # Mocking time.sleep to avoid actual delays
    @patch('logging.error')  # Mocking logging.error to capture error logs
    def test_download_file_error_handling(self, mock_logging_error, mock_sleep):
        """
        Test that errors during file download are properly logged.
        """
        # Simulate an error during the download
        def download_file_with_error(file_id):
            raise Exception(f"Error downloading file {file_id}")

        file_id = 1  # Test with one file ID
        thread = threading.Thread(target=download_file_with_error, args=(file_id,))
        
        # Start and join the thread
        thread.start()
        thread.join()

        # Assert that logging.error was called with the appropriate message
        mock_logging_error.assert_called_with("An error occurred while downloading file 1: Error downloading file 1")

    @patch('time.sleep', return_value=None)  # Mocking time.sleep to avoid actual delays
    @patch('logging.error')  # Mocking logging.error to capture error logs
    def test_perform_other_task_error_handling(self, mock_logging_error, mock_sleep):
        """
        Test that errors during performing other tasks are properly logged.
        """
        # Simulate an error during the task
        def perform_other_task_with_error(task_id):
            raise Exception(f"Error performing task {task_id}")

        task_id = 1  # Test with one task ID
        thread = threading.Thread(target=perform_other_task_with_error, args=(task_id,))
        
        # Start and join the thread
        thread.start()
        thread.join()

        # Assert that logging.error was called with the appropriate message
        mock_logging_error.assert_called_with("An error occurred while performing task 1: Error performing task 1")

if __name__ == "__main__":
    unittest.main()
