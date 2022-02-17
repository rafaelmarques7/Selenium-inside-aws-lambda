from selenium import webdriver
from tempfile import mkdtemp


def instantiate_browser():
    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/chrome/chrome'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")

    # use this to point to local the chromedriver location
    # driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    # use this when running as docker
    driver = webdriver.Chrome("/opt/chromedriver", options=options)
    return driver


def handler(event=None, context=None):
    print("inside handler")
    driver = instantiate_browser()

    driver.get("https://example.com")
    print(driver.page_source)
