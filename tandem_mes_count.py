import pandas as pd
import matplotlib.pyplot as plt

# Load dos dados dos genes
file_location = "/home/vmesel/Dropbox/Vinicius/Iniciação Científica/2018 - MicroExons/Dados/microexon_transcripts.csv"
df = pd.read_csv(file_location, low_memory=False)

tandem_mes_count = {
    "tandem":0,
    "not_tandem":0
}

for me in df["tandem"]:
    if me == "TANDEM":
        tandem_mes_count["tandem"] += 1
    else:
        tandem_mes_count["not_tandem"] += 1

total = len(df["tandem"])

keys = tandem_mes_count.keys()
values = [i/total for i in tandem_mes_count.values()]

explode = tuple([0.2, 0.2])

plt.pie(values, explode=explode, labels=keys, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
