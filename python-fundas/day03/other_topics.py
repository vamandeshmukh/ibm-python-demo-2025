import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/IBM"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

infobox = soup.find("table", {"class": "infobox"})


def get_infobox_value(infobox, label):
    row = infobox.find("th", string=label)
    if row:
        return row.find_next_sibling("td").get_text(strip=True)
    return None


founded = get_infobox_value(infobox, "Founded")
industry = get_infobox_value(infobox, "Industry")
products = get_infobox_value(infobox, "Products")

print("Founded:", founded)
print("Industry:", industry)
print("products:", products)


# # # Advanced Python Modules

# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")
# db = client["ems"]
# employees = db["employees"]

# emp = employees.find_one({"first_name": "Sonu"})
# print(emp)
# # employees.

# # import numpy as np
# # import pandas as pd


# # data = {
# #     "id": [101, 102, 103],
# #     "name": ["Sonu", "Monu", "Tonu"],
# #     "salary": [50000, 55000, 48000],
# # }

# # df = pd.DataFrame(data)
# # print(df)
# # print(df["salary"].mean())


# # # marks = np.array([98, 95, 99, 95, 97])

# # # print(marks)
# # # print(np.max(marks))
# # # print(np.sort(marks))


# # # # Generators in Python and Exception handling


# # # def gen(n):
# # #     i = 1
# # #     while i <= n:
# # #         yield i  # next
# # #         i += 1


# # # val = gen(5)

# # # while True:
# # #     try:
# # #         print(next(val))
# # #     except StopIteration:
# # #         print("done")
# # #         break
# # #     except Exception:
# # #         print("done")
# # #         break
# # #     finally:
# # #         print("closing...")


# # # # # Generators in Python


# # # # def gen(n):
# # # #     i = 1
# # # #     while i <= n:
# # # #         yield i  # next
# # # #         i += 1


# # # # val = gen(5)
# # # # print(next(val))
# # # # print(next(val))
# # # # print(next(val))
# # # # print(next(val))
# # # # print(next(val))
# # # # print(next(val))

# # # # # for num in gen(5):
# # # # #     print(num)
