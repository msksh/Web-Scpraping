
import time
from selenium import webdriver

browser = webdriver.Chrome() #"./chromedriver.exe"


#1. 네이버 이동
browser.get("http://naver.com")

#2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. id, pw 입력
browser.find_element_by_id("id").send_keys("never_id")
browser.find_element_by_id("pw").send_keys("password")


#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

#5. id를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

#6. html 정보 출력
print(browser.page_source)

# 7.브라우저 종료
# browser.close() #현재 탭만 종료
browser.quit() # 전체 브라우저 종료



























#터미널을 이용해서 실행
# >>> browser.get("http://daum.net")
# >>> elem = browser.find_element_by_name("q")
# >>> elem
# <selenium.webdriver.remote.webelement.WebElement (session="b28b00b0a511ff04dab58b5e4be93135", element="ae05dacd-0b60-461a-b6fb-418c6db7a52c")>
# >>> elem.send_keys("성훈")
# >>> elem.send_keys(Keys.ENTER)
# >>> browser.back()
# >>> elem = browser.find_element_by_name("q")
# >>> elem.send_keys("성훈")
# >>> elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
# >>> elem
# <selenium.webdriver.remote.webelement.WebElement (session="b28b00b0a511ff04dab58b5e4be93135", element="9cedc8f6-c682-4220-8e70-aec65109564c")>
# >>> elem.clik()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'WebElement' object has no attribute 'clik'>>> elem.click()
# >>> browser.quit()
