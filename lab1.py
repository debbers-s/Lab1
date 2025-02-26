import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

## 1 Modules and Data Science Packages
rand_num = np.random.rand(10)
print(rand_num)
print(f"""Mean: {rand_num.mean()}
Sum: {rand_num.sum()}
""")
plt.plot(rand_num)
plt.show()

## 2 Strings and Regular Expressions
def extract_email(txt):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, txt)
    return emails

pythonCopyEdittext = "Contact us at support@example.com or sales@example.org for assistance."
print(extract_email(pythonCopyEdittext))

## 3 Preview of Data Science Tools
rand_num2 = np.random.rand(5)
print(rand_num2)
tabledata = {
    'Name': ['-', '-', '-'],
    'Age': ['-', '-', '-'],
    'City': ['-', '-', '-'],
}
table = pd.DataFrame(tabledata)
print(table)

## 4 Exploring Further Resources

items = ['broken eggs', 'spilled milk', 'expired yogurt']
count = [400, 100, 50]
plt.bar(items, count, color="pink")
plt.title('Expensive Mistakes')
plt.xlabel('Items')
plt.ylabel('Count')
plt.show()





