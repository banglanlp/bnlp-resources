import csv

with open('bn_all_train.n.tsv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['id', 'text', 'class_label'])
    with open('bn_all_train.tsv', 'r', encoding='utf-8') as fp:
        reader = csv.reader(fp, delimiter='\t')
        next(reader)
        for row in reader:
            if row[2] == 'positive':
                row[2] = 'Positive'
            elif row[2] == 'neutral':
                row[2] = 'Neutral'
            elif row[2] == 'negative':
                row[2] = 'Negative'
            elif row[2] == 'BN_POS':
                row[2] = 'Positive'
            elif row[2] == 'BN_NEU':
                row[2] = 'Neutral'
            elif row[2] == 'BN_NEG':
                row[2] = 'Negative'

            writer.writerow(row)

with open('bn_all_dev.n.tsv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['id', 'text', 'class_label'])
    with open('bn_all_dev.tsv', 'r', encoding='utf-8') as fp:
        reader = csv.reader(fp, delimiter='\t')
        next(reader)
        for row in reader:
            if row[2] == 'positive':
                row[2] = 'Positive'
            elif row[2] == 'neutral':
                row[2] = 'Neutral'
            elif row[2] == 'negative':
                row[2] = 'Negative'
            elif row[2] == 'BN_POS':
                row[2] = 'Positive'
            elif row[2] == 'BN_NEU':
                row[2] = 'Neutral'
            elif row[2] == 'BN_NEG':
                row[2] = 'Negative'
            writer.writerow(row)

with open('bn_all_test.n.tsv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['id', 'text', 'class_label'])
    with open('bn_all_test.tsv', 'r', encoding='utf-8') as fp:
        reader = csv.reader(fp, delimiter='\t')
        next(reader)
        for row in reader:
            if row[2] == 'positive':
                row[2] = 'Positive'
            elif row[2] == 'neutral':
                row[2] = 'Neutral'
            elif row[2] == 'negative':
                row[2] = 'Negative'
            elif row[2] == 'BN_POS':
                row[2] = 'Positive'
            elif row[2] == 'BN_NEU':
                row[2] = 'Neutral'
            elif row[2] == 'BN_NEG':
                row[2] = 'Negative'

            writer.writerow(row)

