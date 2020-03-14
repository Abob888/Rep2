import csv

with open('st.csv', 'r') as f:
    q = csv.reader(f, delimiter=',')
    for row in q:
        print(','.join(row))
