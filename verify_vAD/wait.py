from selenium.common import exceptions


 def _is_element_visible(self, locator):
        retry_time = 3
        for i in range(retry_time):
            try:
                return self.driver.find_element_by_css_selector(locator).is_displayed()

            except (exceptions.NoSuchElementException,
                    exceptions.ElementNotVisibleException,
                    exceptions.StaleElementReferenceException) as e:

                # auto_updating of element may cause StaleElementReference-
                # Exception, which should be retry to confirm
                if not isinstance(e, exceptions.StaleElementReferenceException):
                    break

        return False

    def _wait_until(self, predicate, timeout=None, poll_frequency=0.5,
                    ignored_exceptions=None):
        """
        Wait until the value returned by predicate is not False or
        the timeout is elapsed.
        :param predicate: takes the driver as argument.
        :param timeout:
        :param poll_frequency:
        :param ignored_exceptions:
        :return:
        """
        if not timeout:
            timeout = self.explicit_wait
        wait.WebDriverWait(self.driver, timeout, poll_frequency,
                           ignored_exceptions).until(predicate)

    def _wait_till_element_visible(self, locator, timeout=None):
        self._wait_until(lambda x: self._is_element_visible(locator),
                         timeout)