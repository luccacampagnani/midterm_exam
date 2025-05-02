#Q1
import requests
import pandas as pd
import matplotlib.pyplot as plt
ticker = "META"
url = f"https://raw.githubusercontent.com/itb-ie/midterm_data/refs/heads/main/{ticker}.csv"
with open("company.csv", "w") as f:
    f.write(requests.get(url).text)
df = pd.read_csv("company.csv", index_col="Date", parse_dates=["Date"])

# Number of rows
print("Number of rows:", len(df))
# Column names
print("Column names:", list(df.columns))
# April 10th highest stock value
april_10_data = df.loc[df.index == pd.Timestamp("2025-04-10")]
if not april_10_data.empty:
    highest_value = april_10_data["High"].max()
    print("Highest stock value on April 10th:", highest_value)
else:
    print("No data available for April 10th.")
# Plot a chosen column
df["Close"].plot(title="META Stock Close Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

#Q3
import numpy as np
a = np.arange(0, 12)
a = a ** 2 + 1
result = []
for i in range(0, 12, 4):
    result.append(list(a[i:i+4]))
print(np.array(result))

#Q4
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(4, 4), index=[1, 2, 3, 4], columns=['a', 'b', 'c', 'd'])
print(df)

print("Using index:", df['b'][2])          # Regular indexing
print("Using loc:", df.loc[2, 'b'])        # Label-based access
print("Using iloc:", df.iloc[1, 1])        # Integer position-based access

#Q6
class NumberUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0
# Example usage
print(NumberUtils.is_even(4))  # True
print(NumberUtils.is_even(7))  # False

#Q7
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.1)
y = x**2 + 4*x + 10
# Find and display minimum value of y
min_y = np.min(y)
print("Minimum value of y:", min_y)

#Q8
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_full_name(self):
        return f"{self.first} {self.last}"

    def __str__(self):
        return f"Person({self.first} {self.last})"

# Example usage
p = Person("Alice", "Johnson")
print(p.get_full_name())  # Regular method
print(p)                  # Magic method __str__ used here
