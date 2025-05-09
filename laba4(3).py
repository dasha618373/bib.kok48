#Задание 3
from Bio import SeqIO

def translate_cds(record):
    
    for feature in record.features:
        if feature.type == "CDS":
            start, end = feature.location.start, feature.location.end
            protein_seq = feature.qualifiers.get("translation", [""])[0]
            print(f"{record.id}: {record.description}")
            print(f"Coding sequence location = [{start}:{end}]")
            print(f"Translation =\n{protein_seq}\n")

def parse_genbank(file_path):
    """Чтение файла GenBank и трансляция CDS"""
    for record in SeqIO.parse(file_path, "genbank"):
        translate_cds(record)


file_path = "E:\example cds.gb" #путь к файлу 
parse_genbank(file_path)