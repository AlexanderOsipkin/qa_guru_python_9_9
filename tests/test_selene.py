from selene import browser, have, be, by
import os


def test_registration():
    browser.open('/automation-practice-form')
    browser.element('.main-header').should(have.text('Practice Form'))

    browser.element('#firstName').should(be.blank).type('Alexander')
    browser.element('#lastName').should(be.blank).type('Osipkin')
    browser.element('#userEmail').should(be.blank).type('alex-test.qaguru@test.com')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('June')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1996')).click()
    browser.element('.react-datepicker__day--011').click()
    browser.element('#subjectsInput').should(be.blank).type('English').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('tests/pictures/kot-kartinka.jpg'))
    browser.element('#currentAddress').should(be.blank).type('Saint-Petersburg, Pushkin street 42')
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(
        have.text(
            'Alexander Osipkin'
            and 'alex-test.qaguru@test.com'
            and 'Male'
            and '1234567890'
            and '11 June,1996'
            and 'English'
            and 'Sports'
            and 'kot-kartinka.jpeg'
            and 'Saint-Petersburg, Pushkin street 42'
            and 'Uttar Pradesh Agra'
        )
    )

    browser.element('#closeLargeModal').press_enter()
