import unittest

def run_all_tests():
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover('tests', pattern='test_*.py')

    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)

    return result

if __name__ == '__main__':
    run_all_tests()