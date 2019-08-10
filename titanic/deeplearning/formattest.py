import re

# data columns
info = """ Save? Y/N
N PassengerId,
Y Pclass, Ticket class 1 = 1st class, 2 = 2nd, 3 = 3rd
N Name, 
Y Sex, male (set to 1), female (set to 0)
Y Age, 
Y SibSp, number of siblings or spouses
Y Parch, number of parents or children
N Ticket, ticket number
Y Fare, 
N Cabin, cabin number
N Embarked C = Cherbourg, Q = Queenstown, S = Southampton

Y Survived, 0 = No, 1 = Yes (the variable we wish to predict)
"""

TEST_CSV = "c:/Users/neo/Desktop/code/machinelearning-datasci/titanic/data/test.csv"
MASSAGED = "c:/Users/neo/Desktop/code/machinelearning-datasci/titanic/deeplearning/testm.msv"

# use average age for those without age

avg_age = 23

namepat = re.compile(r'".*?"')

with open(TEST_CSV) as t, open(MASSAGED, 'w') as m:
    for line in t:
        line = namepat.sub("NAME", line)
        print(line)
        passid, pclass, name, sex, age, sib, par, ticket, fare, cab, embark = line.strip().split(",")

        try:
            agem = int(age)
        except ValueError:
            agem = avg_age

        try:
            ff = float(fare) / 512
        except ValueError:
            ff = 0
            
        # pclass, sex, age, sibsp, par, fare
        print("{},{},{},{},{},{}".format(round(int(pclass) / 3, 6),
                                         1 if sex == 'male' else 0,
                                         round(int(agem) / 80, 6),
                                         round(int(sib) / 8, 6),
                                         round(int(par) / 6, 6),
                                         ff),
              file=m)

        
              
        
