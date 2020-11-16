from appium import webdriver
import support.webElements as we
from appium.webdriver.common.touch_action import TouchAction


class appiumHandler():

    def startServer(self,caps):
        caps = {}
        caps["deviceName"] = "Pixel_3a_11"
        caps["platformVersion"] = "11"
        caps["platformName"] = "Android"
        caps["app"] = "/Users/kinandcarta-appiumtest/support/apps/amazon_shopping.apk"
        caps["appPackage"] = "com.amazon.mShop.android.shopping"
        caps["appActivity"] = "com.amazon.mShop.home.HomeActivity"
        caps["automationName"] = "UiAutomator2"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(60) # segundos de espera máximos hasta que aparezce el elemento en pantalla
        self.driver = driver
    
    def getAnElement(self,elementName):
        actualDictionary = self.getDictionary(elementName)
        reference = actualDictionary[elementName]["reference"]
        typeRef = actualDictionary[elementName]["typeRef"]

        try:
            if typeRef=="xpath":
                element=self.driver.find_element_by_xpath(reference)
            if typeRef=="accessId":
                element=self.driver.find_element_by_accessibility_id(reference)
            if typeRef=="id":
                element=self.driver.find_element_by_id(reference)
            return element
        except:
            assert False, "The element: " + elementName + " can not be found"

    def enterValue(self,elementName,valueKey):
        element = self.getAnElement(elementName)
        element.send_keys(valueKey)
    
    def clickAnElement(self,elementName):
        element = self.getAnElement(elementName)
        element.click()

    def getDictionary(self,elementName):
        dictionaries = [we.LogIn, we.Dashboard, we.Buy]
        cont = 0
        actualDict = ''
        isInDictionary = False

        while isInDictionary==False and cont<len(dictionaries):
            if elementName in dictionaries[cont]:
                actualDict = dictionaries[cont]
                isInDictionary = True
            cont+=1
        if isInDictionary:
            return actualDict
        else:
            assert actualDict=='', "Can't find " + elementName + " element."

    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        action = TouchAction(self.driver)
        action \
            .press(x=start_x, y=start_y) \
            .wait(ms=duration) \
            .move_to(x=end_x, y=end_y) \
            .release()
        action.perform()
        return self