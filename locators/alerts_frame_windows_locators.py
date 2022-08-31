from selenium.webdriver.common.by import By


class BrowserWindowsLocators:

    NEW_TAB = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, 'button[id="messageWindowButton"]')

    TITLE_NEW_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class AlertsLocators:

    ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FrameLocators:
    
    FRAME1 = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    FRAME2 = (By.CSS_SELECTOR, 'iframe[id="frame2"')
    TEXT_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class NestedFrameLocators:

    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


