import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link_promo = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
link_basket = "http://selenium1py.pythonanywhere.com/"



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru or es or fr")

@pytest.fixture(scope="function")
def browser(request):
    global user_language
    user_language = request.config.getoption('language')
    global link_login
    link_login = f"http://selenium1py.pythonanywhere.com/{user_language}/accounts/login/"
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser..')
    browser.quit()

def log():
    if user_language == 'en':
        return f"http://selenium1py.pythonanywhere.com/{user_language+'-gb'}/accounts/login/"
    else:
        return f"http://selenium1py.pythonanywhere.com/{user_language}/accounts/login/"
