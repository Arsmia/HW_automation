from operator import and_
from time import sleep
from selene.support.shared import browser
from selene import be, have
import os
from selenium.webdriver.common.keys import Keys


def test_fill_and_submit_form(set_options_in_browser):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.hold_browser.open = True
    browser.element('#firstName').type('Sviatlana').press_enter()
    browser.element('#lastName').type('Stroke').press_enter()
    browser.element('#userEmail').type('sviatastr@gmail.com').press_enter()
    browser.element('[for=gender-radio-2]').should(be.visible).click()
    browser.element('#userNumber').should(be.blank).type('1234567890').press_enter()
    sleep(3)
    browser.element('[value="1986"]').should(be.clickable).click()
    browser.element('[value="0"]').should(be.clickable).click()
    browser.element('[.aria-label="Choose Wednesday, January 8th, 1986"]').click()
    browser.element('[.subjects-auto-complete__value-container.subjects-auto-complete__value-container--is-multi.css'
                    '-1hwfws3]').type('QA').press_enter()



