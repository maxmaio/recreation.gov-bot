from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

profile = FirefoxProfile("/Users/maxmaio/Library/Application Support/Firefox/Profiles/48s8diof.default-release")
profile.update_preferences()
driver = webdriver.Firefox(profile)
driver.get("https://www.recreation.gov/camping/campgrounds/234513")
closeModal = driver.find_element(By.CLASS_NAME, "sarsa-modal-close-button")
driver.execute_script("arguments[0].click();", closeModal)

checkoutTime = time.time()
startDateInput = driver.find_element(By.ID, "campground-start-date-calendar")
startDateInput.send_keys("04/14/22" + Keys.ENTER)

endDateInput = driver.find_element(By.ID, "campground-end-date-calendar")
endDateInput.send_keys("04/22/22" + Keys.ENTER)

startButton = driver.find_element(By.ID,"60171")
childeren = startButton.find_elements(By.CLASS_NAME, "available")
firstClick = childeren[0].find_element(By.CLASS_NAME, "rec-availability-date")
driver.execute_script("arguments[0].click();", firstClick)
secondClick = childeren[5].find_element(By.CLASS_NAME, "rec-availability-date")
driver.execute_script("arguments[0].click();", secondClick)

addToCart = driver.find_element(By.CLASS_NAME, "availability-page-book-now-button-tracker")
driver.execute_script("arguments[0].click();", addToCart)

print(time.time()- checkoutTime)