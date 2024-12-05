import logging
import threading
import unittest
from unittest.mock import patch, MagicMock
from main import download_file, perform_other_task, start_download_threads, start_task_threads, wait_for_threads

class TestThreadedTasks(unittest.TestCase):

    @patch("main.random.randint", return_value=3)
    @patch("main.time.sleep", return_value=None)
    def test_download_file(self, mock_sleep, mock_randint):
        # Test download_file with mocked sleep and random value
        with self.assertLogs(level='INFO') as log:
            download_file(1)
        self.assertIn("Starting download of file 1... It will take 3 seconds.", log.output[0])
        self.assertIn("Download of file 1 completed in 3 seconds.", log.output[1])

    @patch("main.random.randint", return_value=4)
    @patch("main.time.sleep", return_value=None)
    def test_perform_other_task(self, mock_sleep, mock_randint):
        # Test perform_other_task with mocked sleep and random value
        with self.assertLogs(level='INFO') as log:
            perform_other_task(1)
        self.assertIn("Starting task 1... It will take 4 seconds.", log.output[0])
        self.assertIn("Task 1 completed in 4 seconds.", log.output[1])

    @patch("main.threading.Thread.start", MagicMock())
    def test_start_download_threads(self):
        # Test that download threads are created and started
        file_ids = [1, 2, 3]
        threads = start_download_threads(file_ids)
        self.assertEqual(len(threads), len(file_ids))
        for thread in threads:
            self.assertIsInstance(thread, threading.Thread)

    @patch("main.threading.Thread.start", MagicMock())
    def test_start_task_threads(self):
        # Test that task threads are created and started
        task_ids = [1, 2]
        threads = start_task_threads(task_ids)
        self.assertEqual(len(threads), len(task_ids))
        for thread in threads:
            self.assertIsInstance(thread, threading.Thread)

    @patch("main.threading.Thread.join", MagicMock())
    def test_wait_for_threads(self):
        # Test that threads are joined without issues
        mock_thread_1 = MagicMock()
        mock_thread_2 = MagicMock()
        threads = [mock_thread_1, mock_thread_2]
        wait_for_threads(threads, "test")
        for thread in threads:
            thread.join.assert_called_once()

if __name__ == "__main__":
    logging.disable(logging.CRITICAL)  # Disable logging during tests
    unittest.main()
