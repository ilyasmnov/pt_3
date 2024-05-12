from selene import browser, be, have


def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('-тест').press_enter()
    browser.element('#botstuff').should(have.text('По запросу -тест ничего не найдено.'))



def test_google_should_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
