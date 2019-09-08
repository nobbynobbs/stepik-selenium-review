import pytest
from selenium import webdriver

cases = [
    ("es", "Añadir al carrito",),
    ("fr", "Ajouter au panier",),
    ("ru", "Добавить в корзину",),
    ("en", "Add to basket",),
]

ids = [x[0] for x in cases]

@pytest.mark.parametrize("language, want", cases, ids=ids)
def test_add_to_cart_button(language, want, browser: webdriver.Chrome, user_language):
    if language != user_language:
        pytest.skip(f"skip {language} language")
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    got = button.text
    assert  want == got, f"want '{want}', got '{got}'"
