# Helper utilities

def get_attribute_by_id(driver, id, attribute_name):
	element = driver.find_element_by_id(id)
	return element.get_attribute(attribute_name)


class element_has_css_style(object):

	def __init__(self, locator, css_style):
		self.locator = locator
		self.css_style = css_style

	def __call__(self, driver):
		element = driver.find_element(*self.locator)
		if self.css_style in element.get_attribute('style'):
			return True
		else:
			return False

