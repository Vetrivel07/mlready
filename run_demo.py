import pandas as pd
import mlready as mr

df = pd.DataFrame({
    "Price": ["$1,200", "1.2M"],
    "Membership": ["Yes", "no"],
})

clean, recipe, rep = mr.apply(df)

print(clean)
print(rep)
