from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored


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

    def remove_element(self):
        """ Удалить элемент со страницы """
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")

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

    def click(self, element):
        """ Клик левой кнопкой мыши """
        action = ActionChains(self.driver)
        action.click(element)
        action.perform()

    def get_current_url(self):
        """ Получить адрес текущей страницы. """
        return self.driver.current_url

    def get_page_source(self):
        """ Выдать исходный код страницы. """
        source = ''
        try:
            source = self.driver.page_source
        except:
            print(colored('Can not get page source', 'red'))
        return source

    def switch_new_tab(self, tab_num):
        """ Переключится на новую вкладку """
        return self.driver.switch_to.window(self.driver.window_handles[tab_num])

    def switch_new_alert(self):
        """ Переключится на новое сообщение """
        return self.driver.switch_to.alert

    def switch_to_iframe(self, iframe):
        """ Переключится во фрейм """
        return self.driver.switch_to.frame(iframe)

    def switch_out_iframe(self):
        """ Выйти из фрейма. """
        self.driver.switch_to.default_content()
