import requests
import pandas as pd
from multiprocessing import Pool

def scrape_gene_save_result(gene):
    gene_url = "https://www.orthodb.org/tab?query={}&level=&species=&universal=&singlecopy=".format(gene)
    r = requests.get(gene_url)
    if "no clusters found" in r.text :
        return False
    else:
        f = open("data_downloaded/{}.tsv".format(gene), "w")
        f.write(r.text)
        f.close

def filter_gene_list(filename):
    df = pd.read_csv(filename, low_memory=False)
    df = df.query("gene_type == 'protein_coding'")[["gene_name"]]
    lista = list(set(list(df["gene_name"])))
    return lista


file_location = "/home/vmesel/Dropbox/Vinicius/Iniciação Científica/2018 - MicroExons/Dados/microexon_transcripts.csv"

gene_list = filter_gene_list(file_location)

with Pool(5) as p:
    print(p.map(scrape_gene_save_result, gene_list))
