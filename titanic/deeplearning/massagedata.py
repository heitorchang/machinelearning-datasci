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

TRAIN_CSV = "c:/Users/Heitor/Desktop/code/machinelearning-datasci/titanic/deeplearning/train.csv"
MASSAGED = "c:/Users/Heitor/Desktop/code/machinelearning-datasci/titanic/deeplearning/massaged.msv"
SURVIVED = "c:/Users/Heitor/Desktop/code/machinelearning-datasci/titanic/deeplearning/survived.msv"

# use average age for those without age

tot = 0
ct = 0
with open(TRAIN_CSV) as t:
    for line in t:
        vals = line.strip().split(",")
        try:
            tot += int(vals[6])
        except ValueError:
            pass
        ct += 1

avg_age = tot // ct
print(avg_age)

namepat = re.compile(r'".*?"')

with open(TRAIN_CSV) as t, open(MASSAGED, 'w') as m, open(SURVIVED, 'w') as s:
    for line in t:
        line = namepat.sub("NAME", line)

        passid, surv, pclass, name, sex, age, sib, par, ticket, fare, cab, embark = line.strip().split(",")
        print(surv, file=s)
        try:
            agem = int(age)
        except ValueError:
            agem = avg_age
        
        # pclass, sex, age, sibsp, par, fare
        print("{},{},{},{},{},{}".format(round(int(pclass) / 3, 6),
                                         1 if sex == 'male' else 0,
                                         round(int(agem) / 80, 6),
                                         round(int(sib) / 8, 6),
                                         round(int(par) / 6, 6),
                                         round(float(fare) / 512, 6)),
              file=m)

        
              
        
