import requests
from bs4 import BeautifulSoup
from datetime import date
import datetime
import re


current_time = datetime.datetime.now() #gets the date
main = requests.get("https://www.teamunify.com/Calendar.jsp?team=ilreach&type=m&y=" + str(current_time.year) + "&m=" + str(current_time.month)) #fetches website
soup = BeautifulSoup(main.text, 'html.parser') #parses

def get_data():
    table = soup.find_all("table")
    rows = table[3].find_all("tr")
    for row in rows:
        columns = row.find_all("td", {"class": "calday"})
        #reg ex
        for column in columns:
            m = re.search(r'Lead A[\s,\w]+[@at][\s\w]([A-z]{3,4}) (\d+:\d\d [\s\w]+- \d+:\d+ [PA]M)', column.text)
            d = re.search(r'(\d+)\s+\W+', column.text)
            if m:
                print(" -----------------------------\n| " + d.group(0)+m.group(0) + "     |\n ")
        #»



def week_data():
    year, week_num, day_of_week = current_time.isocalendar()
    dates = []
    start = int(current_time.day - day_of_week)
    for x in range(1, 8):
        dates.append(start+x)
    current_time.day
    table = soup.find_all("table")
    rows = table[3].find_all("tr")
    for row in rows:
        columns = row.find_all("td", {"class": "calday"})
        for column in columns:
            m = re.search(r'Lead A[\s,\w]+[@at][\s\w]([A-z]{3,4}) (\d+:\d\d [\s\w]+- \d+:\d+ [PA]M)', column.text)
            d = re.search(r'(\d+)\s', column.text)
            days_of_week = dates
            if m:
                if int(d.group(1)) in days_of_week:
                    print(" -----------------------------\n| " + d.group(0)+m.group(0) + "     |\n ")

choice = input(" -----------------------------\n| \u00bb 1 for month schedule.     |\n| \u00bb Enter 2 for week schedule.|\n -----------------------------\n")
print(r"""
            ___
          /`  _\
          |  / 0|--.
     -   / \_|0`/ /.`'._/)
 - ~ -^_| /-_~ ^- ~_` - -~ _
 -  ~  -| |   - ~ -  ~  -
        \ \, ~   -   ~
         \_|
""")

choice = int(choice)

if choice == 1:
    get_data()
elif choice == 2:
    week_data()
else:
   print("Wrong Choice, terminating the program.")