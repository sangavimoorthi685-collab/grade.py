import numpy as np
import pandas as pd
data = {
    "Name": ["Sangavi", "Ravi", "Kavi"],
    "Mark": [85, 75, 90]
}
df = pd.DataFrame(data)
print("STUDENT DATA")
print(df)
marks = np.array(df["Mark"])
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))