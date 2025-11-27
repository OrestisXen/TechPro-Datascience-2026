import numpy as np

dataset_arr = np.random.randint(0,10,(4*365, 5) )

# print(dataset_arr)

# question #1
# x = dataset_arr[:,0].sum(axis=0)
x = dataset_arr.sum(axis=0)
print(f"Total burger sales: {x[0]}")

# question #2
y = np.array([ 1.5, 1.2, 0.9, 0.75, 1.2 ])
x = dataset_arr[:,1].sum()
revenue = x*y[1]

print(f"Total Sandwich revenue {revenue}")


# Question #5

colaSales = dataset_arr[:,4] * 0.75
beerSales = dataset_arr[:,3] * 1.2

beerOutsold = beerSales > colaSales

print(beerOutsold.sum())

# Question #6

dailyRevenue = dataset_arr.dot(y)
print(dailyRevenue)



# Question #7
x = dailyRevenue.sum()
print(f"Total Revenue: {x}")









