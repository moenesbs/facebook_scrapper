from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
prefs = {
  "translate_whitelists": {"your native language":"en"},
  "translate":{"enabled":"True"},
  "profile.default_content_setting_values.notifications" : 2
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('app/chromedriver', chrome_options=options)  


driver.get('http://www.facebook.com/google/')

time.sleep(3)



def openreplies():
    replies = driver.find_elements(By.XPATH, "//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv']")
    if len(replies) > 0:
        count = 0
        for i in replies:
            action=ActionChains(driver)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    driver.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        time.sleep(1)
    else:
        pass    

def openComment():    
    moreComment = driver.find_elements(By.XPATH, "//span[contains(@class,'x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen x1s688f xi81zsa') and starts-with(text(), 'View') and contains(text(), 'more comment')]")
    if len(moreComment) > 0:
        count = 0
        for i in moreComment:
            action=ActionChains(driver)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    driver.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        time.sleep(1)
    else:
        pass

def openSeeMore():
    readMore = driver.find_elements(By.XPATH, "//div[contains(@class,'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f') and contains(text(), 'See more')]")
    if len(readMore) > 0:    
        count = 0
        for i in readMore:
            action=ActionChains(driver)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    driver.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        time.sleep(1)
    else:
        pass

def openSeeMoreComment():
    readMore = driver.find_elements(By.XPATH, "//div[contains(@class,'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f') and contains(text(), 'See more')]")
    if len(readMore) > 0:    
        count = 0
        for i in readMore:
            action=ActionChains(driver)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    driver.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        time.sleep(1)
    else:
        pass


def scroll():
    for _ in  range(15):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)