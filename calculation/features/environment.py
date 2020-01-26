from pyvirtualdisplay import Display
from selenium import webdriver

def before_tag(context, tag):
    if 'web' in context.tags:
        context.display = Display(visible=0, size=(800, 600))
        context.display.start()
        context.browser = webdriver.Firefox()
        context.browser.implicitly_wait(10)


def after_tag(context, tag):
    if 'web' in context.tags:
        context.browser.quit()
        context.display.stop()
