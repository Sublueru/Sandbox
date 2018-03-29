from sys import argv
import csv
import requests
from bs4 import BeautifulSoup
import re

# initiate argv to accept the csv file from the user that contains a list of non-canonical URLs

try:
    _, provided_csv = argv
except ValueError:
    print """
        Please include the CSV file when submitting!
        Example Format:
        python Canonicalator.py test.csv
        """
    exit()

# take csv file of the non-canonical links provided my user

f = open(provided_csv)
csv_f = csv.reader(f)

# iterates over the csv data provided by the user, using requests module to pull the HTML page data
for row in csv_f:
    response = requests.get(row[0])
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
# using BeautifulSoup module to pick out the important pieces of the returned HTML from the header (pick out the canonical link)
    raw_canonical = str(soup.find(href=re.compile("help.republicwireless.com")))

# using strip methods to remove the html junk from the canonical web address
    left_strip = raw_canonical[12:]

    final_strip = left_strip[:-19]

    print final_strip






    # print response.content
    # print "success!!" # temp loop validator