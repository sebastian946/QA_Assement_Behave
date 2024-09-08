from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.XPATH, "//h2[normalize-space()='Busca en cientos de webs de vuelos a la vez.']")
    signin_button = (By.XPATH, "//div[@class='J-sA']//div[@role='button']")
    search_button = (By.XPATH, "//button[@aria-label='Buscar']//div[@class='RxNS-button-container']")
