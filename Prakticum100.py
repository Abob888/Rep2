import os

p = os.path.join('C:\'
                 ,
                 'Users\'
                 ,
                 'Аня\'
                 ,
                 'Videos\'
                 ,
                 'Примеры программ\'
                 ,
                 'Self_Taught_Programmer_Althoff\'
                 ,
                 'Глава 20\'
                 ,
                 'output.txt')

with open(p, 'r') as f:
    print(f.read())
