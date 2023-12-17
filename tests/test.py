from time import sleep
from selene.support.shared import browser
from selene import be, have, command
import os


def test_fill_and_submit_form(set_options_in_browser):
    browser.open('automation-practice-form')
    browser.config.hold_browser_open = True

    # ACT():
    browser.element('#firstName').type('Sviatlana').click()
    browser.element('#lastName').type('Stroke').click()
    browser.element('#userEmail').type('name@example.com').click()
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').should(be.blank).type('1234567890').click()
    sleep(3)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').should(be.clickable).click()
    browser.element('[value="1986"]').click()
    browser.element('.react-datepicker__month-select').should(be.clickable).click()
    browser.element('[value="0"]').click()
    browser.element('.react-datepicker__day--008').click()
    sleep(3)

    browser.element('#subjectsInput').type('Arts').press_enter()

    browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
    browser.element('[for=hobbies-checkbox-2]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../photo.jpg'))

    browser.element('#currentAddress').type('Bruzdowa str.').click()

    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).press_enter()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Agra')).press_enter()

    browser.element('.table').all('td').even.should(have.texts(
        "Sviatlana Stroke",
        'name @ example.com',
        'Female',
        '1234567890',
        '8 January, 1986',
        'Arts',
        'Reading',
        'photo.jpg',
        'Bruzdowa str.',
        'NCR',
        'Agra'
    ))
