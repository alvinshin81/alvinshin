from selenium import webdriver


driver = webdriver.Chrome('../model/drivers/chromedriver_98')



driver.get('chrome://downloads')

driver.switch_to.frame('body')
downloadfile = driver.find_element_by_xpath('//*[@id="file-link"]').text

print(downloadfile)

