import shutil
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    chromium_path = shutil.which("chromium") or shutil.which("chromium-browser")
    chromedriver_path = shutil.which("chromedriver")

    if chromium_path and chromedriver_path:
        options.binary_location = chromium_path
        service = Service(chromedriver_path)
    else:
        service = Service(ChromeDriverManager().install())

    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(5)


def after_step(context, step):
    if step.status == "failed" and hasattr(context, "driver"):
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=step.name,
            attachment_type=allure.attachment_type.PNG,
        )


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
