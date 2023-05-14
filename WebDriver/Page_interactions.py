from selenium.webdriver.common.by import By
#################################################################
# Page handling functions
#################################################################

# Login Constants
UsernameTag = "ctl00$Main$txtUserName"
PasswordTag = "ctl00$Main$txtPassword"
LoginSubmitTag = "ctl00$Main$btnLogin"

def Login(browser, username, password): #Pass user's username and password and enter it into the MOFTB login page
    browser.find_element(By.NAME, UsernameTag).send_keys(username)
    browser.find_element(By.NAME, PasswordTag).send_keys(password)
    browser.find_element(By.NAME, LoginSubmitTag).click()


# Choose_Project Func Constants
ProjectListTag = "ctl00_Main_gvProjectsList"
