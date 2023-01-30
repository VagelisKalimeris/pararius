# Selenium Setup

First, install Selenium on your system by running in a shell:

    pip3 install -U selenium

You can check installation by opening a python interpreter and running:

    from selenium import webdriver

---
Then, download the driver for your OS and browser of choice from 
[here](https://chromedriver.chromium.org/downloads).

After downloading, unzip and move the driver file to your repo.

Test the driver file, by double-clicking it. A new terminal window should open 
with a success message. In case this step fails on macOS with a:

    ... cannot be opened because developer cannot be verified

message, remove the restriction by running:

    xattr -d com.apple.quarantine chromedriver


Returning to the interpreter, check that Selenium is utilising the driver by
running:

    browser = webdriver.Chrome('Browser_Driver')

A new Chrome window should open, with the indication:

    Chrome is being controlled by automated software

---