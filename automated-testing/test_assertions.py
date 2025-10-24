from text_analysis import calculate_text_attributes
import pytest
# Section: The `assert` Statement

# Uncoment the following lines to see the assertion failure
# x: int = 5
# assert x == 5
# assert x == 6, 'x should be 5'

# Section: Pytest and `assert`

def test_string_equality() -> None:
    expected_status = "SUCCESS"
    actual_status = "success".upper()

    assert expected_status == actual_status, f'Expected "{expected_status}" but got "{actual_status}"'

def test_word_count() -> None:
    text =  "Deploying microservice to the Kubernetes cluster"
    text_empty = ""
    assert (calculate_text_attributes(text)["word_count"]) == 6
    assert (calculate_text_attributes(text_empty)["word_count"]) == 0

def test_unique_words() -> None:
    text =  "Deploying microservice to the Kubernetes cluster"
    text_with_duplicates = "Deploying deploying"
    text_empty = ""

    text_results = calculate_text_attributes(text)
    text_results_duplicates = calculate_text_attributes(text_with_duplicates)
    text_results_empty = calculate_text_attributes(text_empty)
   

    assert (len(set(text_results["unique_words"]))) == 6
    assert (len(set(text_results_duplicates["unique_words"]))) == 1
    assert (len(set(text_results_empty["unique_words"]))) == 0
def test_average_word_length() -> None:
    text =  "Deploying microservice to Kubernetes cluster" # 40 / 5 = 8.0
    text_with_duplicates = "Deploying deploying"  # 18 / 2 = 9.0
    text_empty = "" # 0 / 0 = 0.0

    text_results = calculate_text_attributes(text)
    text_results_duplicates = calculate_text_attributes(text_with_duplicates)
    text_results_empty = calculate_text_attributes(text_empty)
   

    assert (text_results["average_word_length"]) == 8.0
    assert (text_results_duplicates["average_word_length"]) == 9.0
    assert (text_results_empty["average_word_length"]) == 0.0

def test_longest_word() -> None:
    text =  "Deploying microservice to Kubernetes cluster" # microservice
    text_with_duplicates = "Deploying deploying"  # Deploying
    text_empty = "" # 0 / 0 = 0.0

    text_results = calculate_text_attributes(text)
    text_results_duplicates = calculate_text_attributes(text_with_duplicates)
    text_results_empty = calculate_text_attributes(text_empty)
   

    assert (text_results["longest_word"].lower()) == "microservice"
    assert (text_results_duplicates["longest_word"].lower()) == "deploying"
    assert (text_results_empty["longest_word"]) == ""   


# Section: Pytest’s Rich Failure Output

def test_string_mismatch() -> None:
    expected = "HEllo WOrlD"
    actual = "hello world"

    assert expected == actual, f'Expected "{expected}" but got "{actual}"'

# Section: Asserting Floating-Point Numbers (`pytest.approx`)

def test_float_approximation() -> None:
    calculated_val = 0.1 + 0.2
    expected_val = 0.3

    assert calculated_val == pytest.approx(expected_val), "Expected value does not match"  # approx used to compare floating point numbers

# Section: Asserting Exceptions (`pytest.raises`)

def test_raises_exception() -> None:
    with pytest.raises(ZeroDivisionError):
        _division = 1 / 0 


#######################################################  pytest commands ###############################
# commands to run the tests
# pytest 

# pytest -v # to see the verbose output

# pytest -r # to show failed tests

# pytest -ra # to show all tests, including skipped ones

# pytest -rA # to show all tests, including skipped ones, and show their source code 

# pytest -ra -s  # to show all tests and also the print statements

#######################################################################################################