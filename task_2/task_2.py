import re
import requests
from urllib.parse import urlsplit
import pandas as pd


def getResponse(url, url_query):
    if url_query != '':
        query_array = url_query.split(sep="&")
        query_dict = {}

        for part in query_array:
            part = part.split('=')
            query_dict[part[0]] = part[1]
        try:
            return requests.get(url=url, params=query_dict)
        except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema) as error:
            print("Error: " + error)
    else:
        try:
            return requests.get(url=url)
        except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema) as error:
            print("Error: " + error)


parts = urlsplit(input("Enter the url: "))
url = f"{parts.scheme}://{parts.netloc}{parts.path}"

response = getResponse(url, parts.query)

emails = set(re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,}", response.text, re.I))

df = pd.DataFrame(emails, columns=["Emails"])

excel_name = input("Type the final file name: ")
df.to_excel(f'{excel_name}.xlsx')

print("Completed.")
