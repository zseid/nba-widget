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
        self.pulldata()
        
        #while True:
        #    self.cmpmsg()

        def tearDown(self):
            self.driver.close()
            
    def pulldata(self):
        teamlist = []
        scorelist = []
        driver = self.driver
        #
        #pull scores
        #
        score_elem = driver.find_elements_by_class_name('current_score')
        for scores in score_elem:
            scorelist.append(scores.text)
        #
        #pull team
        #
        team_elem = driver.find_elements_by_class_name('team-points')
        for teams in team_elem:
            teamlist.append(teams.text[:3])
        self.prntstats(scorelist,teamlist)

    def printstats(self, score_list, team_list):
        teamlist = team_list
        scorelist = score_list
        for i in range(0, (len(scorelist) -1)):
            print("\n")
            print(teamlist[i],"Vs.",teamlist[i+1])
            print(scorelist[i],"    ",scorelist[i+1])
        #
        #nugget text
        #
        #nugget_elem = driver.find_element_by_class_name('score__tile--nugget-text')
        #print (nugget_elem.text)
if __name__ == "__main__":
    unittest.main()
