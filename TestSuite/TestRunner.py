from unittest import TestLoader, TestSuite, TextTestRunner
from Scripts.test_home_page import YouTubeHomePage
from Scripts.test_list_of_video import ListVideo
from Scripts.test_python_search import PythonSearch
from Scripts.test_video import SelectedVideo


if __name__ == "__main__":
    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(YouTubeHomePage),
        test_loader.loadTestsFromTestCase(PythonSearch),
        test_loader.loadTestsFromTestCase(ListVideo),
        test_loader.loadTestsFromTestCase(SelectedVideo)
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
