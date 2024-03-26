# Initialize the WebDriver and login
from selenium import webdriver
import pickle

def driver_init(login_url):
    driver = webdriver.Safari()
    driver.set_window_size(1920, 1480)

    # Navigate to the URL
    URL = login_url
    driver.start_client()
    driver.get(URL)

    # Wait for JavaScript to load (you can customize the wait time)
    driver.implicitly_wait(1)
    
    driver.get(login_url) #Access website
    driver.implicitly_wait(2)

    try:
        # Find the login form elements and fill in your login credentials
        username_input = driver.find_element(by="id", value="username")
        password_input = driver.find_element(by="id", value="password")

        # Enter your login credentials (replace with your own)
        username_input.send_keys("trololo")
        password_input.send_keys("trololo123AZE")
        driver.implicitly_wait(2)

        # Submit the login form
        login_button = driver.find_element(by="id", value="loginButton")
        login_button.submit() #Click login button. ie submit login credentials

        # You may need to handle CAPTCHA here if it appears
        # You can use CAPTCHA solving services (e.g., 2Captcha) or manual intervention
    except Exception as e:
        print("An error occurred:", e)
        
    # Wait for some time (adjust as needed) to allow for successful login
    driver.implicitly_wait(2)
        
    return driver # After login, we can perform additional actions as needed



def pickle_data(file_path, operation, data=None):
    """
    Function to write or read data to/from a pickle file.

    Parameters:
    file_path (str): The path of the file.
    operation (str): The operation to perform - 'write' or 'read'.
    data (optional): The data to write. Required if operation is 'write'.

    Returns:
    The data read from the file if operation is 'read'.
    """
    if operation == 'write':
        if data is None:
            raise ValueError("Data must be provided for write operation")
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
    elif operation == 'read':
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    else:
        raise ValueError("Operation must be 'write' or 'read'")