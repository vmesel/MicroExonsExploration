import pandas as pd
import matplotlib.pyplot as plt

# Load dos dados dos genes
file_location = "/home/vmesel/Dropbox/Vinicius/Iniciação Científica/2018 - MicroExons/Dados/microexon_transcripts.csv"
df = pd.read_csv(file_location, low_memory=False)

mes_count = []

for arch in df["architecture"]:
    arch = arch.strip()
    arch = arch.split("-")

    count = 0

    for exon in arch:
        if exon == "ME":
            count += 1

    mes_count.append(count)

from collections import Counter

agg_count = dict(Counter(mes_count))

total_mes = sum(agg_count.values())

qt_mes, percent = [], []

for k, v in agg_count.items():
    qt_mes.append(k)
    percentage = agg_count[k] / total_mes
    percent.append(percentage)

# print(list(zip(qt_mes, percent)))
qt_mes_n, percent_n = [], []

for n, item in enumerate(sorted(list(zip(qt_mes, percent)), key=lambda x: x[1])[::-1][:4]):
    qt_mes_n.append(str(item[0]))
    percent_n.append(item[1])

qt_mes_n.append("Outros")
percent_n.append(1 - sum(percent_n))

explode = tuple([0.2, 0.2, 0.2, 0.2, 0.5])

plt.pie(percent_n, explode=explode, labels=qt_mes_n, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
