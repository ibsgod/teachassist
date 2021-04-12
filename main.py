import time
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ta.yrdsb.ca/yrdsb/")

def send(to):
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    username = 'sankeethdude@gmail.com'
    password = 'hteeknas1234'
    from_addr = username
    to_addrs = [to]
    message = MIMEText("Your marks changed")
    message['subject'] = 'Bruh'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()


username = driver.find_element_by_name("username")
username.send_keys("340803493")
password = driver.find_element_by_name("password")
password.send_keys("hotdogsr")
login = driver.find_element_by_name("submit")
time.sleep(5)
login.click()
marks = []
while True:
    for i in range(3):
        marklinks = driver.find_elements_by_partial_link_text("current mark")
        time.sleep(5)
        marklinks[i].click()
        mark = driver.find_element_by_xpath("/html/body/div/div[3]/div/table[1]/tbody/tr/td[1]/div")
        print(mark.text)
        if len(marks) <= i + 1:
            marks.append(mark.text)
        elif mark.text != marks[i]:
            send("340803493@gapps.yrdsb.ca")
        back = driver.find_element_by_partial_link_text("back to cours")
        time.sleep(5)
        back.click()

