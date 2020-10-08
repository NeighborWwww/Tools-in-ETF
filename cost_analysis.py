# This program compare 4 techs with different market time delay, NRE cost, and unit cost
# The program will plot a per-product cost figure, it can visualize the result

import matplotlib.pyplot as plt

# W is the half of the product lifetime. In this case, the product lifetime is 150 months
W = 75

# D is the time delay to the market
D = [3, 6, 12, 25]

# Label list for a better print message
label = ["A", "B", "C", "D"]

# Unit cost of the products
uc = [55, 11, 2, 0.5]

# The product order quantity
productnum = 175000

# Calculate the time-to-market loss using W and D
n = 0
loss = []
for d in D:
    prl = 1 - ((2 * W - d) * (W - d))/(2 * W ** 2)
    rev = 700000 * prl
    print("{}: loss rate: {}, loss: {}".format(label[n], prl, rev))
    loss.append(rev)
    n = n + 1

# The total fix cost is NRE + time-to-market loss
NRE = [1000+loss[0], 5000+loss[1], 25000+loss[2], 100000+loss[3]]

y = [[], [], [], []]
x = []
intersection = [[], []]
for n in range(productnum):
    # print(n)
    if n != 0:
        for i in range(len(NRE)):
            y[i].append(NRE[i] / n + uc[i])
        x.append(n)
        # print(y)
        ycomp = [l[n-1] for l in y]
        if n == 1:
            ylcmax = ycomp.index(min(ycomp))
            print("at the beginning, {} is the most cost efficient".format(label[ylcmax]))
        else:
            if ycomp.index(min(ycomp)) != ylcmax:
                intersection[0].append(n)
                intersection[1].append(min(ycomp))
                print("{} becomes more efficient than {} at {} products".format(label[ycomp.index(min(ycomp))], label[ylcmax], n))
                ylcmax = ycomp.index(min(ycomp))
# print(intersection)

# Plot the result figure
plt.plot(x, y[0], x, y[1], x, y[2], x, y[3])
plt.scatter(intersection[0], intersection[1], color='black')
plt.ylim(0, 100)
plt.legend(label, loc="best")
plt.xlabel("Product number")
plt.ylabel("Per-product cost")
plt.show()