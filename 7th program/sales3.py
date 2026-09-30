import numpy as np
import pandas as pd

data = {
    "Name": ["sangavi", "Kaviya", "Abi"],
    "Salary": [25000, 30000, 28000]
}
df = pd.DataFrame(data)
print("EMPLOYEE DATA")
print(df)
salary = np.array(df["Salary"])
print("Total Salary:", np.sum(salary))
print("Average Salary:", np.mean(salary))
print("Highest Salary:", np.max(salary))
print("Lowest Salary:", np.min(salary))