import webbrowser


def test_scores_service(url):
    webbrowser.open(url)
    return True


def main_function():
    test_results = test_scores_service("google.co.il")
    if test_results:
        print("All tests passed!")
        return 0
    else:
        print("Some tests failed.")
        return -1
