import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("hdemo1.csv", index_col=0)

day_name = ["8~9", "9~10", "10~11", "11~12", "12~13", "13~14", "14~15", "15~16", "16~17"]
day_median = []

day_median.append(df.median()["8~9"])
day_median.append(df.median()["9~10"])
day_median.append(df.median()["10~11"])
day_median.append(df.median()["11~12"])
day_median.append(df.median()["12~13"])
day_median.append(df.median()["13~14"])
day_median.append(df.median()["14~15"])
day_median.append(df.median()["15~16"])
day_median.append(df.median()["16~17"])

fig = plt.figure()
plt.style.use('dark_background')
plt.bar(day_name, day_median, color = "#BAE8E8", edgecolor = "#FFD803", width=0.8)
plt.show()
fig.savefig("num/static/num/images/estimate.png" ,bbox_inches="tight")