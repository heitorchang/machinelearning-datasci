RAW = "c:/Users/neo/Desktop/code/machinelearning-datasci/titanic/deeplearning/ans.csv"
FMT = "c:/Users/neo/Desktop/code/machinelearning-datasci/titanic/deeplearning/submissiondeep.csv"

init = 892
with open(RAW) as r, open(FMT, 'w') as f:
    for line in r:
        print(str(init) + "," + line, end='', file=f)
        init += 1
        
