import sys

import requests
from bs4 import BeautifulSoup

all_categories:list[str] = [
"Programming",
"Web-Development",
"Software-testing",
"Design",
"DevOps",
"Data Science",
"Database-Administrator",
"Cyber-Security",
"Gaming",
"Engineering",
"Networking",
"IT-Management",
"IT-Support",
"Consultant",
"hr",
"Online-Marketing",
"Content-creators",
"Others"
]

class JobInfo:
    def __init__(self,title:str, company_name:str, location:str, list_of_technologies:list[str], date:str) -> None:
        self.title = title
        self.company_name = company_name
        self.location = location
        self.list_of_technologies = list_of_technologies
        self.date = date

def url_create(categories:list[str], search:str):
    for category1 in categories:
        if category1 not in all_categories:
            return None
    url_:str = "https://www.juniors.ro/jobs"
    for category_ in categories:
        url_ = url_ + "/" + category_

    if search == "":
        return url_

    url_ = url_ + "?q=" + search

    return url_

def get_location_and_time(location_time:str):
    location:str = ""
    time:str = ""
    split = location_time.split(" ")
    #print(split)
    location = split[0]
    location =  location.split("\n")[0]
    i:int = 1
    while True:
        if split[i] == '':
            i += 1
        else:
            i += 1
            break

    time = split[i] + " " + split[i+1]

    return location, time



def get_info_from_url(url:str):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        return None
    soup = BeautifulSoup(response.text, 'html.parser')

    soup = soup.find("body", class_="").find("div", class_="page-structure").find("div").find("section").find("div").find("div", class_="grid").find("div", class_="col_content")

    #print (soup.prettify())

    soup_list = soup.find("ul", class_="job_list").find_all("li", class_="job")

    #print(len(soup_list))
    #for s in soup_list:
        #print(s.prettify())

    jobs:list[JobInfo] = []


    for soup_job in soup_list:
        title = soup_job.find("div", class_="job_header").find("div", class_="job_header_title").find("h3").get_text(strip=True)
        location_time = soup_job.find("div", class_="job_header").find("div", class_="job_header_title").find("strong").get_text(strip=True)

        location, time = get_location_and_time(location_time)

        tags: list[str] = []

        soup_tags =  soup_job.find("div", class_="job_header").find("div", class_="job_header_title").find("ul", class_="job_tags").find_all("li")

        for s in soup_tags:
            tags.append(s.find("a").get_text(strip=True))
            #print(s.prettify())

        company_name = soup_job.find("div", class_="job_content").find("div").find("ul").find("li").get_text(strip=True).split(":")[1]

        # print(tags)
        # print(title)
        # print(location)
        # print(time)
        # print(company_name)

        jobs.append(JobInfo(title, company_name, location, tags, time))

    return jobs


    return None

if __name__ == "__main__":
    categories:list[str] = []
    search:str = ""
    nr_categories = 0
    len_argv:int = len(sys.argv)
    if len_argv < 3:
        print("Usage: python job_search.py <number of categories> <list of categories> <search string>(optional)")
        sys.exit()
    try:
        nr_categories = int(sys.argv[1])
    except ValueError:
        print("number of categories<" + sys.argv[1] + "> must be an integer")
        sys.exit()

    if len_argv - 2 < nr_categories:
        print("to few categories")
        sys.exit()

    if len_argv - 3 > nr_categories:
        x = (len_argv - 3 - nr_categories)
        print("to many strings: " + str(x) + " to many")
        sys.exit()

    if nr_categories > 0:
        for category in sys.argv[2:(2+nr_categories):1]:
            categories.append(category)

    if len_argv - 3 == nr_categories:
        search = sys.argv[2+nr_categories]



    url:str = url_create(categories, search)
    if url is None:
        print("incorrect categories")
        sys.exit()

    #print(url)

    jobs = get_info_from_url(url)

    for job in jobs[:7]:
        print("Title: " + job.title)
        print("location: " + job.location)
        print("Post date: " + job.date)
        print("Company name: " + job.company_name)
        print("List of technologies: ",end='')
        for t in job.list_of_technologies:
            print(t + ", ",end='')
        print("\n")
