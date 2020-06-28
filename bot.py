from selenium import webdriver
from time import sleep


class IgBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def start(self, igUsername, igPassword, friendIg, message, quantity):
        self.igUsername = igUsername
        self.igPassword = igPassword
        self.friendIg = friendIg
        self.message = message
        self.quantity = quantity

        self.login(igUsername, igPassword)

        self.closeNotification()

        self.findFriend(friendIg)

        self.sendMessage(message, quantity)

    def login(self, igUsername, igPassword):
        self.driver.get('https://instagram.com')
        self.igUsername = igUsername
        self.igPassword = igPassword

        sleep(2)

        user = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        user.send_keys(igUsername)

        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        password.send_keys(igPassword)

        loginBtn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
        loginBtn.click()
        sleep(3)

        saveInfo = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        saveInfo.click()

        sleep(3)

    def closeNotification(self):
        notification = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[1]')
        notification.click()

    def findFriend(self, friendAccount):
        self.friendAccount = friendAccount

        searchBar = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
        searchBar.click()

        sleep(2)

        barInput = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        barInput.send_keys(friendAccount)
        sleep(6)

        profile = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a/div')
        profile.click()

        sleep(2)

    def sendMessage(self, text, quantity):
        sendMsg = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button')
        sendMsg.click()

        sleep(2)

        self.closeNotification()

        for i in range(quantity):
            msgBox = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

            msgBox.click()

            sleep(1)

            msgBoxInput = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            msgBoxInput.send_keys(text)
            sendBtn = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
            sendBtn.click()


user = input("Username: ")
password = input("Password: ")
friend = input("FriendAccount: ")
message = input("Write the message: ")
quantity = input("Quantity of repetitions: ")

bot = IgBot()
bot.start(user, password, friend, message, quantity)
