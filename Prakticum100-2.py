import csv

a = [['123',
      '456',
      '789'],
     ['11',
      '12',
      '13'],
     ['100',
      '200',
      '300']]

with open('exer10.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    for m_l in a:
        w.writerow(m_l)
