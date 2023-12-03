from selene import browser, have, be, by
import os
import allure


def test_registration_with_allure_steps():
    with allure.step("Открываем форму для заполнения данных"):
        browser.open('/automation-practice-form')

    with allure.step("Проверяем что форма, которую мы открыли верная"):
        browser.element('.main-header').should(have.text('Practice Form'))

    with allure.step("Проверяем что поле Имя пустое и если это так то вводим " "значение"):
        browser.element('#firstName').should(be.blank).type('Alexander')

    with allure.step("Проверяем что поле Фамилия пустое и если это так то вводим значение"):
        browser.element('#lastName').should(be.blank).type('Osipkin')

    with allure.step("Проверяем что поле Email пустое и если это так то вводим " "значение"):
        browser.element('#userEmail').should(be.blank).type('alex-test.qaguru' '@test.com')

    with allure.step("Активируем radio batton"):
        browser.element('#gender-radio-1').double_click()

    with allure.step("Вводим валидный номер телефона"):
        browser.element('#userNumber').should(be.blank).type('1234567890')

    with allure.step("Выбираем дату рождения через элементы календаря"):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text('June')).click()
        browser.element('.react-datepicker__year-select').click().element(by.text('1996')).click()
        browser.element('.react-datepicker__day--011').click()

    with allure.step("вводим значение в поле subjects"):
        browser.element('#subjectsInput').should(be.blank).type('English').press_enter()

    with allure.step("Активируем чекбокс хобби"):
        browser.element('[for="hobbies-checkbox-1"]').click()

    with allure.step("Выбираем и загружаем картинку"):
        browser.element('#uploadPicture').send_keys(os.path.abspath('pictures/kot-kartinka.jpg'))

    with allure.step("Проверяем что поле Адрес пустое и если это так то вводим " "значение"):
        browser.element('#currentAddress').should(be.blank).type(
            'Saint-Petersburg, Pushkin street 42'
        )

    with allure.step("Выбираем Штат"):
        browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()

    with allure.step("Выбираем город"):
        browser.element('#react-select-4-input').type('Agra').press_enter()

    with allure.step("Подтверждаем введеные значения"):
        browser.element('#submit').press_enter()

    with allure.step("Проверяем что форма заполнена корректно"):
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

    with allure.step("Закрываем форму"):
        browser.element('#closeLargeModal').press_enter()
