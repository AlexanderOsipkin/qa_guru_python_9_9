from selene import browser, have, be, by
import os
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Alexander Osipkin')
@allure.feature('Allure decorator')
@allure.story('test selene with allure decorator')
def test_checking_title_with_decorators():
    open_browser()
    enter_first_name()
    enter_last_name()
    enter_email()
    radio_button_click()
    enter_user_number()
    enter_date_of_birthday()
    enter_subjects()
    enter_hobby()
    upload_picture()
    enter_adress()
    enter_state()
    enter_city()
    click_submit()
    correct_form()
    close_form()


@allure.step('Открываем форму для заполнения данных и проверяем что она пуста')
def open_browser():
    browser.open('/automation-practice-form')
    browser.element('.main-header').should(have.text('Practice Form'))


@allure.step('Проверяем что поле Имя пустое и если это так то вводим значение')
def enter_first_name():
    browser.element('#firstName').should(be.blank).type('Alexander')


@allure.step('Проверяем что поле Фамилия пустое и если это так то вводим значение')
def enter_last_name():
    browser.element('#lastName').should(be.blank).type('Osipkin')


@allure.step('Проверяем что поле Email пустое и если это так то вводим значение')
def enter_email():
    browser.element('#userEmail').should(be.blank).type('alex-test.qaguru@test.com')


@allure.step('Активируем radio button')
def radio_button_click():
    browser.element('#gender-radio-1').double_click()


@allure.step('Вводим валидный номер телефона')
def enter_user_number():
    browser.element('#userNumber').should(be.blank).type('1234567890')


@allure.step('Выбираем дату рождения через элементы календаря')
def enter_date_of_birthday():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('June')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1996')).click()
    browser.element('.react-datepicker__day--011').click()


@allure.step('вводим значение в поле subjects')
def enter_subjects():
    browser.element('#subjectsInput').should(be.blank).type('English').press_enter()


@allure.step('Активируем чекбокс хобби')
def enter_hobby():
    browser.element('[for="hobbies-checkbox-1"]').click()


@allure.step('Выбираем и загружаем картинку')
def upload_picture():
    browser.element('#uploadPicture').send_keys(os.path.abspath('pictures/kot-kartinka.jpg'))


@allure.step('Проверяем что поле Адрес пустое и если это так то вводим значение')
def enter_adress():
    browser.element('#currentAddress').should(be.blank).type('Saint-Petersburg, Pushkin street 42')


@allure.step('Выбираем Штат')
def enter_state():
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()


@allure.step('Выбираем город')
def enter_city():
    browser.element('#react-select-4-input').type('Agra').press_enter()


@allure.step('Подтверждаем введеные значения')
def click_submit():
    browser.element('#submit').press_enter()


@allure.step('Проверяем что форма заполнена корректно')
def correct_form():
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


@allure.step('Закрываем форму')
def close_form():
    browser.element('#closeLargeModal').press_enter()
