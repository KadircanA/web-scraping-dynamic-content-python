from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
currenttime =(time.strftime("%x %H:%M"))

#This path shows the current address of the chromedriver
driver_path = "C:\\Users\\chromedriver.exe"
browser = webdriver.Chrome(driver_path)

#This link goes to the Linkedin website and shows the last last 24 hours of the record of the jobs posting details page
browser.get("https://tr.linkedin.com/jobs/jobs-in-i%CC%87stanbul-t%C3%BCrkiye?location=%3Fstanbul%2C%20T%EF%BF%BDrkiye&f_PP=100170895&geoId=102424322&locationId=&keywords=&f_TPR=r86400&countryRedirected=1&position=1&pageNum=0")

browser.maximize_window()
for _ in range(10):
    browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(1)

PageSource=browser.page_source
soup = BeautifulSoup(PageSource, "lxml")
Jobs_Source = soup.find_all("div", attrs={"class":"base-card"})
browser.close()

Job_number =0
Eror_Job_Number =0
for job in Jobs_Source:
    try:
        Job_Title = job.find("h3", attrs={"base-search-card__title"}).text.strip()
        Job_number +=1
        Company_Link = job.find("h4", attrs={"base-search-card__subtitle"}).a.get("href")
        Company_Title = job.find("h4", attrs={"base-search-card__subtitle"}).a.text.strip()
        Job_Link = job.a.get("href")
        r=requests.get(Job_Link)
        Job_soup = BeautifulSoup(r.content, "lxml")
        Job_Page_Detail = Job_soup.find("div", attrs={"class":"decorated-job-posting__details"}).find("ul", attrs={"class":"description__job-criteria-list"}).find_all("li", attrs={"class":"description__job-criteria-item"})
        print(Job_Title)
        print(Company_Title)
        print("Company_Link:",Company_Link)
        print("---"*30)
        for Detail in Job_Page_Detail:
            Title = Detail.find("h3", attrs={"class":"description__job-criteria-subheader"}).text.strip()
            Explanation = Detail.find("span", attrs={"class":"description__job-criteria-text description__job-criteria-text--criteria"}).text.strip()
            print(f"{Title}: {Explanation}")

        print(f"For more details:{Job_Link}")
        print("###"*30)
    except AttributeError :
        Eror_Job_Number +=1
        pass
print("There are {} missing jobs in the database".format(Eror_Job_Number) if Eror_Job_Number > 0 else "")
print("*-*"*30)
print(f"{currenttime}==> {Job_number} new job postings ")
print("*-*"*30)