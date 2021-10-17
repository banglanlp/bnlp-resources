files = ['Tatoeba.bn-en.bn', 'Tatoeba.bn-en.en',]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read().strip().split("\n")
        print(f"{file}: {len(lines)}")