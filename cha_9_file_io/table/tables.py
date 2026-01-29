def genTable(n):
    table = ""
    for i in range(1, 11):
        table = table + f"{n}x{i}={n*i}\n"
    with open(f"cha_9_file_io/table/tables{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 31):
    genTable(i)
