from selenium import webdriver
from selenium.common import TimeoutException, InvalidArgumentException, \
    NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from json import load
import ascii_art

print(ascii_art.greeting)
# Default speed between user steps
SPEED = 1
# Load personal credentials to memory
creds, cred_keys = load(open('creds.json')), \
    ['message', 'first_name', 'last_name', 'email', 'phone']
assert all([k in creds.keys() for k in cred_keys]), \
    'Error! Missing information from credentials file!'

# Retrieve target URL
HOMEPAGE = input('Please enter the listing\'s URL:\n')
# Create browser window
ChromeWindow = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Visit valid URL
try:
    ChromeWindow.get(HOMEPAGE)
except InvalidArgumentException:
    print('\n\tERROR! The listing\'s URL appears incorrect!')
    ChromeWindow.quit()
    exit()
# Wait for redirection/page load
try:
    WebDriverWait(ChromeWindow, 25).until(
        EC.presence_of_element_located((By.CLASS_NAME,
            'agent-summary__agent-contact-request')))
except TimeoutException:
    print('Waiting for contact request button timed out!')
    ChromeWindow.quit()
    exit()

# Press contact agent button
lmnt = ChromeWindow.find_element(By.CLASS_NAME,
    'agent-summary__agent-contact-request')
ChromeWindow.execute_script("arguments[0].click();", lmnt)

# Fill credential fields
for cred in cred_keys:
    sleep(SPEED)
    ChromeWindow.find_element(By.NAME,
        'listing_contact_agent_form[' + cred + ']').send_keys(creds[cred])

# Move to the bottom of the page
sleep(SPEED)
ChromeWindow.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# Press submit button
sleep(SPEED)
ChromeWindow.find_element(By.CLASS_NAME, 'form__button--submit').click()

# Bypass Captcha, in case of repeated use and detection
sleep(5)
success = False
while not success:
    try:
        ChromeWindow.find_element(By.CLASS_NAME, 'form-errors__error')
        print('CAPTCHA detection! Retry!')
        sleep(3)
        # Move to the bottom of the page
        ChromeWindow.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        ChromeWindow.find_element(By.CLASS_NAME, 'form__button--submit').click()
    except NoSuchElementException:
        print(ascii_art.success)
        success = True

# Close browser  window - Quit
sleep(5)
ChromeWindow.quit()
