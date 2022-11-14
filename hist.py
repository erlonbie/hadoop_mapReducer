import numpy as np

# d = {}
# with open("out_sorted.txt") as f:
#     for line in f:
#        key, val = line.split("\t")
#        d[key] = int(val)

with open("./out_sorted.txt") as f:
    d = {k: int(v) for line in f for (k, v) in [line.strip().split('\t')]}

hist, bins = np.histogram(list(d.values()), range = (0.0, 520.0))

print(bins)
print(hist)
