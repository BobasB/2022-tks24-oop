import math
import datetime
import pandas as pd

for x in range(0, int(2 * math.pi)):
    print(f"Sin {x} = {math.sin(x)}")

print(datetime.datetime.now())

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)