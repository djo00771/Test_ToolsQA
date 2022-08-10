from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    """ Локаторы для страницы Text Box"""
    # add person
    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # check output
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    """ Локаторы для страницы CheckBox """

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class RadioButtonPageLocators:
    """ Локаторы для страницы Radio Button """

    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:
    """ Локаторы для страницы Web Table """

    # add new person
    ADD_BUTTON = (By.CSS_SELECTOR, '#addNewRecordButton')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#userEmail')
    AGE_INPUT = (By.CSS_SELECTOR, '#age')
    SALARY_INPUT = (By.CSS_SELECTOR, '#salary')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, '#department')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')

    # check output
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.ID, 'searchBox')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

