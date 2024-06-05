from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


file_path = os.path.abspath('GAUDICOS1.html')
file_url = f'file:///{file_path.replace("\\", "/")}'


driver = webdriver.Chrome()

try:
    driver.get(file_url)

    about_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'ABOUT'))
    )
    about_link.click()
    time.sleep(2)  

    about_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'about'))
    )
    assert about_section.is_displayed(), "About section is not displayed"

    portfolio_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'PORTFOLIO'))
    )
    portfolio_link.click()
    time.sleep(2)  

    portfolio_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'portfolio'))
    )
    assert portfolio_section.is_displayed(), "Portfolio section is not displayed"

    
    facebook_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.facebook.com/ian1203']"))
    )
    facebook_link.click()
    time.sleep(2)
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        assert "Facebook" in driver.title, "Facebook page did not open"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    else:
        print("Facebook page did not open")


    instagram_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.instagram.com/iann.iannn/']"))
    )
    instagram_link.click()
    time.sleep(2) 
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        assert "Instagram" in driver.title, "Instagram page did not open"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    else:
        print("Instagram page did not open")


    portfolio_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#attendance']"))
    )
    portfolio_item.click()
    time.sleep(2)
    attendance_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'attendance'))
    )
    assert attendance_section.is_displayed(), "Attendance section is not displayed"
    back_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#portfolio']"))
    )
    back_button.click()
    time.sleep(2)
    assert portfolio_section.is_displayed(), "Back to portfolio section failed"

    print("All tests passed successfully!")

except AssertionError as e:
    print(f"Test failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
