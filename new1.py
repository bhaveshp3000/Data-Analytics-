import quandl

dataset1 = quandl.get("NSE/IBULISL")

for i in range(0,4):
    print(dataset1['Open'][i])


