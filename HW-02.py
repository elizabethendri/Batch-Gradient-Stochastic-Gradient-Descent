# Elizabeth Endri
# CSC 481 - Artificial Intelligence
# HW 02
# This program implements batch gradient descent and stochastic descent algorithms
# to find the linear regression equation


# Initial Weights       w0=.25        w1= .25     α = 0.0001 or 1/t
# Repeat until convergence


# how fast our model learns (learning rate)
alpha = 0.0001


initial_b = 0
initial_m = 0
iterations = 1000000

# weights
w0 = 0.25
w1 = 0.25


x_points = [2, 4, 6, 7, 8, 10]
y_points = [5, 7, 14, 14, 17, 19]

for i in range(iterations):
    summation = 0
    summation2 = 0
    for j in range(6):
        summation += y_points[j] - (w0 + w1 * x_points[j])
        summation2 += (y_points[j] - (w0 + w1 * x_points[j])) * x_points[j]

    w0 = w0 + alpha * summation
    w1 = w1 + alpha * summation2

print(w0)
print(w1)


# STOCHASTIC
for i in range(iterations):
    for i in range(6):
       w0 = w0 + alpha * (y_points[i] - (w0 +w1 * x_points[i]))
       w1 = w1 + alpha * (y_points[i] - (w0 + w1 * x_points[i])) *x_points[i]


print(w0)
print(w1)
