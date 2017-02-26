import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



class NBATest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def test_fblogin(self):
        driver = self.driver
        driver.get("http://www.nba.com")
        self.assertIn('NBA.com', driver.title)
        
        #while True:
        self.pullscore()
        
        #while True:
        #    self.cmpmsg()

        def tearDown(self):
            self.driver.close()
            
    def pullscore(self):
        driver = self.driver
        score_elem = driver.find_elements_by_class_name('current_score')
        for scores in score_elem:
            print (scores.text)


if __name__ == "__main__":
    unittest.main()

