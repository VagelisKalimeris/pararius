# Objective

Repeatedly applying to Pararius listings can be tedious and tiresome, 
especially typing or pasting your personal details. To tackle this productivity 
issue, I implemented this quick & dirty Selenium script, automating the 
repetitive task.


# Requirements
### Python
Developed and tested under Python 3.11
### Selenium
If you haven't already, setup Selenium by following instructions 
[here](docs/selenium_setup.md).


# Instructions

### Credentials
Go to [creds.json](data/creds.json) file and enter your credentials. For example:

    {
      "message": "Hi, I am awesome!",
      "first_name": "John",
      "last_name": "Doe",
      "email": "johndoe@mail.com",
      "phone": "+99 99999999"
    }

### Execution
Run **apply.py** and enter your preferred listing's link on prompt.
