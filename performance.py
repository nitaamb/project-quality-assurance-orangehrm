from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class AddKPI(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login
        time.sleep(2)
    
    def test_a_success_add_KPI(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu__Performance").click() # klik menu performance
        browser.find_element(By.ID,"menu_performance_Configure").click() # klik configure
        browser.find_element(By.ID,"menu_performance_searchKpi").click() # klik KPIs
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/select/option[8]").click() # select job title
        browser.find_element(By.ID,"defineKpi360_keyPerformanceIndicators").send_keys("problem solving") # isi KPI
        browser.find_element(By.ID,"saveBtn").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"//form[@id='frmList_ohrmListComponent']/div[2]").text
        self.assertEqual('Successfully Saved', response_data)
        
    def test_b_failed_add_KPI_with_all_empty_fields(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu__Performance").click() # klik menu performance
        browser.find_element(By.ID,"menu_performance_Configure").click() # klik configure
        browser.find_element(By.ID,"menu_performance_searchKpi").click() # klik KPIs
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.ID,"saveBtn").click() # klik tombol save

        # validasi
        response_job_title = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[2]/span").text
        response_key_performance_indicators = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[2]/span").text
            
        self.assertEqual('Required', response_job_title)
        self.assertEqual('Required', response_key_performance_indicators)

    def test_c_failed_add_KPI_with_minimum_rating_more_than_100(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu__Performance").click() # klik menu performance
        browser.find_element(By.ID,"menu_performance_Configure").click() # klik configure
        browser.find_element(By.ID,"menu_performance_searchKpi").click() # klik KPIs
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/select/option[8]").click() # select job title
        browser.find_element(By.ID,"defineKpi360_keyPerformanceIndicators").send_keys("problem solving") # isi KPI
        browser.find_element(By.NAME,"defineKpi360[minRating]").send_keys(Keys.CONTROL, "a") # ctrl+a
        browser.find_element(By.NAME,"defineKpi360[minRating]").send_keys(Keys.DELETE) # tekan deletee
        browser.find_element(By.NAME,"defineKpi360[minRating]").send_keys("101") # isi min rating
        browser.find_element(By.ID,"saveBtn").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[3]/span").text
        self.assertEqual('Should be less than 100', response_data)

    def test_d_failed_add_KPI_with_min_rating_greater_than_max_rating(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu__Performance").click() # klik menu performance
        browser.find_element(By.ID,"menu_performance_Configure").click() # klik configure
        browser.find_element(By.ID,"menu_performance_searchKpi").click() # klik KPIs
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/select/option[8]").click() # select job title
        browser.find_element(By.ID,"defineKpi360_keyPerformanceIndicators").send_keys("problem solving") # isi KPI
        browser.find_element(By.NAME,"defineKpi360[minRating]").send_keys(Keys.CONTROL, "a") # ctrl+a
        browser.find_element(By.NAME,"defineKpi360[minRating]").send_keys(Keys.DELETE) # tekan delete
        browser.find_element(By.NAME,"defineKpi360[minRating]").send_keys("100") # isi min rating
        browser.find_element(By.NAME,"defineKpi360[maxRating]").send_keys(Keys.CONTROL, "a") # ctrl+a
        browser.find_element(By.NAME,"defineKpi360[maxRating]").send_keys(Keys.DELETE) # tekan delete
        browser.find_element(By.NAME,"defineKpi360[maxRating]").send_keys("50") # isi max rating
        browser.find_element(By.ID,"saveBtn").click() # klik tombol save

        # validasi
        response_min_rating = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[3]/span").text
        response_max_rating = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[4]/span").text
            
        self.assertEqual('Max rating should be greater than Min rating', response_min_rating)
        self.assertEqual('Max rating should be greater than Min rating', response_max_rating)

    def test_e_failed_add_KPI_with_maximum_rating_more_than_100(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu__Performance").click() # klik menu performance
        browser.find_element(By.ID,"menu_performance_Configure").click() # klik configure
        browser.find_element(By.ID,"menu_performance_searchKpi").click() # klik KPIs
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/select/option[8]").click() # select job title
        browser.find_element(By.ID,"defineKpi360_keyPerformanceIndicators").send_keys("problem solving") # isi KPI
        browser.find_element(By.NAME,"defineKpi360[maxRating]").send_keys(Keys.CONTROL, "a") # ctrl+a
        browser.find_element(By.NAME,"defineKpi360[maxRating]").send_keys(Keys.DELETE) # tekan delete
        browser.find_element(By.NAME,"defineKpi360[maxRating]").send_keys("101") # isi max rating
        browser.find_element(By.ID,"saveBtn").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[4]/span").text
        self.assertEqual('Should be less than 100', response_data)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()