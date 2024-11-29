import logging
import multithreading
import threading
import unittest
from unittest.mock import patch


# Assuming the functions are defined in a separate file (threading_script.py)
from multithreading import download_file, perform_other_task


class TestMultithreading(unittest.TestCase):

    def test_download_file_success(self):
        # Mock logging.info to avoid unnecessary output
        with patch('logging.info') as mock_logging_info:
            # Simulate a successful download
            file_id = 1
            download_file(file_id)

            # Assert that logging.info was called with the expected messages
            expected_start_message = f"Starting download of file {file_id}..."
            expected_completion_message = f"Download of file {file_id} completed in"
            mock_logging_info.assert_any_call(expected_start_message)
            mock_logging_info.assert_any_call(expected_completion_message)

    def test_perform_other_task_success(self):
        # Mock logging.info to avoid unnecessary output
        with patch('logging.info') as mock_logging_info:
            # Simulate a successful task completion
            task_id = 2
            perform_other_task(task_id)

            # Assert that logging.info was called with the expected messages
            expected_start_message = f"Starting task {task_id}..."
            expected_completion_message = f"Task {task_id} completed in"
            # mock_logging_info.assert_any_call(expected_start_message)
            # mock_logging_info.assert_any_call(expected_completion_message)

    def test_thread_creation(self):
        # Simulate thread creation (no actual execution)
        file_ids = [1, 2, 3]
        task_ids = [1, 2]

        download_threads = []
        for file_id in file_ids:
            thread = threading.Thread(target=download_file, args=(file_id,))
            download_threads.append(thread)

        task_threads = []
        for task_id in task_ids:
            thread = threading.Thread(target=perform_other_task, args=(task_id,))
            task_threads.append(thread)

        # Assert the number of threads created is correct
        self.assertEqual(len(download_threads), len(file_ids))
        self.assertEqual(len(task_threads), len(task_ids))

if __name__ == '__main__':
    unittest.main()
