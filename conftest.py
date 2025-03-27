import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    # service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"

    # options for run in container
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
