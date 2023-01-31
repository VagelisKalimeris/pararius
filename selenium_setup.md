# Selenium Setup

Install Selenium and webdriver manager, on your system by running in a shell:

    pip3 install -U selenium

    pip3 install webdriver-manager

You can check installation by opening a python interpreter and running:

    from selenium import webdriver

---
The Chrome driver for your OS, will be downloaded automatically.
Returning to the interpreter, check that Selenium is utilising the driver by
running:

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    webdriver.Chrome(service=Service(ChromeDriverManager().install()))

A new Chrome window should open, with the indication:

    Chrome is being controlled by automated software

Close the window and interpreter to exit.

---