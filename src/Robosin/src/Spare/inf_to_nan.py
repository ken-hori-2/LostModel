
import numpy as np

df = [12., 4., 6., np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0.]

df = np.array(df)

print(df)

# df = ",".join(df)

# print(df)

# df = df.replace([np.inf, -np.inf], np.nan)
df = df.replace([np.inf], np.nan)

print(df)

# s = 'one two one two one'

# print(s.replace(' ', '-'))