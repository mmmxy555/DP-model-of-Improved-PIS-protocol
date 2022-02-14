import random

import matplotlib.pyplot as plt
import numpy as np


def noisyCount(sensitivety, epsilon):
    beta = sensitivety / epsilon
    u1 = np.random.random()
    u2 = np.random.random()
    if u1 <= 0.5:
        n_value = -beta * np.log(1. - u2)
    else:
        n_value = beta * np.log(u2)
    # print(n_value)
    return n_value


def laplace_mech(data, sensitivety, epsilon):
    DPdata = data[:]
    for i in range(len(data)):
        DPdata[i] = data[i] + noisyCount(sensitivety, epsilon)
    return DPdata


def figure():
    raw_data = []
    for i in range(100):
        raw_data.append(random.randint(1, 100))
    print("raw_data", raw_data)

    circulate_time = 20
    sensitivety_time = 100

    epsilon = 1
    x = range(sensitivety_time)
    raw_data_sum = sum(raw_data)

    diff = [0] * sensitivety_time

    for j in range(circulate_time):
        DP_sum = []
        for sensitivety in range(100):
            DP_sum.append(sum(laplace_mech(raw_data, sensitivety, epsilon)))
            diff[sensitivety] += abs(sum(laplace_mech(raw_data, sensitivety, epsilon)) - raw_data_sum)
        colorbar = plt.scatter(x, DP_sum, c=DP_sum, s=5, cmap=plt.cm.viridis)

    plt.plot(x, [x / circulate_time for x in diff], label='average diff data sum')
    plt.plot(x, [raw_data_sum] * sensitivety_time, label='raw data sum')

    plt.xlabel('sensitivety')
    plt.legend()
    plt.colorbar(colorbar)
    plt.show()

def ratetest(sensitivety):
    timelist=[0]
    for j in range(10000,1000000,10000):
        # print(j)
        raw_data = []
        for i in range(j):
            raw_data.append(random.randint(1, 100))
        epsilon=1
        import time
        T1 = time.time()
        laplace_mech(raw_data, sensitivety, epsilon)

        T2 = time.time()

        timelist.append(T2-T1)

    return timelist