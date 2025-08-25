# Advanced Python Modules

import numpy as np
import pandas as pd


data = {
    "id": [101, 102, 103],
    "name": ["Sonu", "Monu", "Tonu"],
    "salary": [50000, 55000, 48000],
}

df = pd.DataFrame(data)
print(df)
print(df["salary"].mean())


# marks = np.array([98, 95, 99, 95, 97])

# print(marks)
# print(np.max(marks))
# print(np.sort(marks))


# # Generators in Python and Exception handling


# def gen(n):
#     i = 1
#     while i <= n:
#         yield i  # next
#         i += 1


# val = gen(5)

# while True:
#     try:
#         print(next(val))
#     except StopIteration:
#         print("done")
#         break
#     except Exception:
#         print("done")
#         break
#     finally:
#         print("closing...")


# # # Generators in Python


# # def gen(n):
# #     i = 1
# #     while i <= n:
# #         yield i  # next
# #         i += 1


# # val = gen(5)
# # print(next(val))
# # print(next(val))
# # print(next(val))
# # print(next(val))
# # print(next(val))
# # print(next(val))

# # # for num in gen(5):
# # #     print(num)
