# importation of the solution function to test
import os


def test_required_file_added():
    """This is the test for the implemented solution passing
    valid inputs"""
    
    if "firstfile.py".lower() in os.listdir("src/"):
        assert True
    else:
        assert False


def test_check_initial_tree():
    """This is the test for the implemented solution passing
    non valid inputs"""
    expected_outputs =  [ True for i in range(5) ]
    tree = os.listdir()
    espected = ['requirements.txt', 'tests', 'README.md', '.gitignore', 'src']

    outputs = []

    for item in espected:
        if item in tree:
            outputs.append(True)
        else:
            outputs.append(False)

    assert outputs == expected_outputs
