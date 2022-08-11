from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """ Открыть """

        self.driver.get(self.url)

    def is_visible(self, locator, timeout=5):
        """ Видимость элемента """

        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_all_visible(self, locator, timeout=5):
        """ Видимость всех элементов """

        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def is_present(self, locator, timeout=5):
        """ Элемент представлен на странице """

        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def is_all_present(self, locator, timeout=5):
        """ Все элементы представлены на странице """

        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def is_not_visible(self, locator, timeout=5):
        """ Элемент не виден """

        return Wait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def is_clickable(self, locator, timeout=5):
        """ Элемент кликабелен """

        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element):
        """ Скролить до элемента """

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def double_click(self, element):
        """ Двойной клик """

        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def right_click(self, element):
        """ Клик правой кнопкой мыши """

        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()
