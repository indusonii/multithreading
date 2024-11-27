import unittest
from unittest.mock import patch
import threading
import time
import random

# The existing code with functions `download_file`, `perform_other_task`, and `main` goes here.

# Test cases for the multi-threaded download and task simulation
class TestMultithreading(unittest.TestCase):
    
    @patch('random.randint')
    @patch('time.sleep', return_value=None)  # Mock time.sleep to avoid real delays
    def test_download_file(self, mock_sleep, mock_randint):
        """
        Test the download_file function by mocking random.randint and time.sleep.
        This ensures the function simulates file downloading correctly.
        """
        # Test with a known random time
        mock_randint.return_value = 3
        file_id = 1
        with self.assertLogs(level='INFO') as log:
            download_file(file_id)
            self.assertIn(f"Starting download of file {file_id}... It will take 3 seconds.", log.output)
            self.assertIn(f"Download of file {file_id} completed in 3 seconds.", log.output)
    
    @patch('random.randint')
    @patch('time.sleep', return_value=None)  # Mock time.sleep to avoid real delays
    def test_perform_other_task(self, mock_sleep, mock_randint):
        """
        Test the perform_other_task function by mocking random.randint and time.sleep.
        This ensures the function simulates performing tasks correctly.
        """
        # Test with a known random time
        mock_randint.return_value = 2
        task_id = 1
        with self.assertLogs(level='INFO') as log:
            perform_other_task(task_id)
            self.assertIn(f"Starting task {task_id}... It will take 2 seconds.", log.output)
            self.assertIn(f"Task {task_id} completed in 2 seconds.", log.output)
    
    @patch('random.randint')
    @patch('time.sleep', return_value=None)  # Mock time.sleep to avoid real delays
    def test_main(self, mock_sleep, mock_randint):
        """
        Test the main function which runs the download and task threads.
        We patch `random.randint` to ensure predictable results.
        """
        mock_randint.return_value = 3  # Make both download and task times predictable
        
        # Mocking print to capture output
        with patch('builtins.print') as mock_print:
            main()

            # Check if the output mentions starting and completing downloads and tasks
            for i in range(1, 6):  # Checking files 1 to 5
                mock_print.assert_any_call(f"Starting download of file {i}... It will take 3 seconds.")
                mock_print.assert_any_call(f"Download of file {i} completed in 3 seconds.")
            
            for i in range(1, 4):  # Checking tasks 1 to 3
                mock_print.assert_any_call(f"Starting task {i}... It will take 3 seconds.")
                mock_print.assert_any_call(f"Task {i} completed in 3 seconds.")
    
    @patch('random.randint')
    @patch('time.sleep', return_value=None)
    def test_error_handling_in_download(self, mock_sleep, mock_randint):
        """
        Test the error handling in the download_file function.
        We simulate an error during file downloading.
        """
        mock_randint.return_value = 3
        file_id = 1
        with patch('builtins.print') as mock_print:
            # Simulate an exception during download
            def side_effect(*args, **kwargs):
                raise Exception("Download failed")
            mock_print.side_effect = side_effect
            download_file(file_id)
            mock_print.assert_called_with(f"An error occurred while downloading file {file_id}: Download failed")
    
    @patch('random.randint')
    @patch('time.sleep', return_value=None)
    def test_error_handling_in_task(self, mock_sleep, mock_randint):
        """
        Test the error handling in the perform_other_task function.
        We simulate an error during task performance.
        """
        mock_randint.return_value = 3
        task_id = 1
        with patch('builtins.print') as mock_print:
            # Simulate an exception during task performance
            def side_effect(*args, **kwargs):
                raise Exception("Task failed")
            mock_print.side_effect = side_effect
            perform_other_task(task_id)
            mock_print.assert_called_with(f"An error occurred while performing task {task_id}: Task failed")

if __name__ == "__main__":
    # Create a test suite and add the tests
    suite = unittest.TestSuite()
    
    # Add individual test methods
    suite.addTest(TestMultithreading('test_download_file'))
    suite.addTest(TestMultithreading('test_perform_other_task'))
    suite.addTest(TestMultithreading('test_main'))
    suite.addTest(TestMultithreading('test_error_handling_in_download'))
    suite.addTest(TestMultithreading('test_error_handling_in_task'))

    # Create a test runner and run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)
