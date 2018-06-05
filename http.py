import requests
import json 

def getCountries(string, p):
    # inital get request to get page data
    r = requests.get('https://jsonmock.hackerrank.com/api/countries/search?name=' + string)
    getPageData = json.loads(r.content)
 
    # get and concantenate all pages for request
    totalPages = getPageData['total_pages']
    countries = []
    for page in range(1, totalPages + 1):
        r2 = requests.get('https://jsonmock.hackerrank.com/api/countries/search?name=' + string + '&page=' + str(page))
        getData = json.loads(r2.content)
        countries += getData['data']

    # filter data by population parameter p
    filteredData = [country for country in countries if country['population'] > p]

    return len(filteredData)
