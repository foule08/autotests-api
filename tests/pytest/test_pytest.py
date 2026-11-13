import allure


@allure.title("First Try")
def test_first_try():
    print("test_first_try")

@allure.title("Assert Positive Case")
def test_assert_positive_case():
    assert (2+2) == 4

@allure.title("Assert Negative Case")
def test_assert_negative_case():
    assert (2+2) == 5