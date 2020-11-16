import support.session as session
import time

# steps

@given("I log in to the Amazon Shop app")
def step_impl(context):
    session.driver.startServer(session.capabilities)
    login()

@when("I make a search")
def step_impl(context):
    search()

@then("I am able to add it to the cart")
def step_impl(context):
    cart()

# functions

def login():
    session.driver.clickAnElement("SKIP SIGN IN")

def search():
    session.driver.clickAnElement("SEARCH BAR")
    session.driver.enterValue("SEARCH BAR",'Alexa')
    session.driver.clickAnElement("SELECT FILTER")
    time.sleep(15) #la app se reinicia automáticamente para ofrecer una búsqueda personalizada basada en la región del usuario
    session.driver.clickAnElement("SEARCH BAR")
    session.driver.clickAnElement("SELECT PREVIOUS FILTER")
    time.sleep(5)
    session.driver.swipe(540, 2000, 540, 170)
    session.driver.swipe(540, 2000, 540, 170)
    session.driver.swipe(540, 2000, 540, 170)
    session.driver.swipe(540, 2000, 540, 170)
    time.sleep(5)
    session.driver.clickAnElement("NEXT PAGE")

def cart():
    session.driver.clickAnElement("SELECT THIRD ITEM")
    time.sleep(5)
    session.driver.swipe(540, 2000, 540, 570)
    time.sleep(5)
    session.driver.clickAnElement("ADD TO CART")
    session.driver.clickAnElement("VIEW CURRENT CART")