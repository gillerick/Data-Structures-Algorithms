"""
Use the HTTP GET method to retrieve information from a database of countries. Query https://jsonmock.hackerrank.com/api/countries/search?name=s where s is the value of s1, to find all of the countries that have the substring in their names (not case sensitive). The query response is paginated and can be further accessed by appending to the query string &page=num where num is the page number. The query response from the website is a JSON response with the following fields
page: current page number
per_page: maximum number of records to display per page
total: total records matching the query
total_pages: the number of pages required to display the matching records
data: a json array containing details of the queried county(ies)
Given a substring s and the minimum population p, find the number of county names that contain s and that have population greater than p.


"""

import requests


def populations(country, p):
    URL = 'https://jsonmock.hackerrank.com/api/countries/search?'
    PARAMS = {'name': country}

    # Performing a GET request
    data = requests.get(url=URL, params=PARAMS)

    # Extracting the data in JSON format
    d_json = data.json()
    countries = d_json['data']
    count = 0
    for country in countries:
        if country['population'] > p:
            count += 1
    return count


print(populations('un', 100090))  # Returns 8
print(populations('un', 100))  # Prints 10
print(populations('kenya', 1000))  # Prints 1
