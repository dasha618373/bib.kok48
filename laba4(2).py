#Вариант 1
#Задание 2
from Bio import SeqIO

file_path = "E:\example cds.gb" #путь к файлу 
records = []


for record in SeqIO.parse(file_path, "genbank"):
    gc_content = (record.seq.count("G") + record.seq.count("C")) / len(record.seq)
    records.append((record.id, record.description, gc_content))

# Сортируем записи по GC-составу
records.sort(key=lambda x: x[2])

# Выводим результат
for record_id, description, gc_content in records:
    print(f"{record_id}: {description}, GC = {gc_content:.5f}")
