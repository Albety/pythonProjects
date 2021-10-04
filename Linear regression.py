# euclidean_distance

def euclidean_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    distance += (pt1[i] - pt2[i]) ** 2
  return distance ** 0.5

# manhattan distance

def manhattan_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    distance += abs(pt1[i] - pt2[i])
  return distance

# hamming distance

def hamming_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    if pt1[i] != pt2[i]:
      distance += 1
  return distance

print(euclidean_distance([1, 2], [4, 0]))
print(manhattan_distance([1, 2], [4, 0]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))

print('\nscipy.stats\n')

# Distances using Scipy
from scipy.spatial import distance

print(distance.euclidean([1,2], [4, 0]))
print(distance.cityblock([1,2], [4, 0]))
print(distance.hamming([5, 7, 9,4], [1, 7, 9,4]))

# Regression

# gradient b and m
def get_gradient_at_b(x, y, m, b):
  diff = 0
  N = len(x)
  for i in range(N):
    y_val = y[i]
    x_val = x[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -2 / N * diff
  return b_gradient


def get_gradient_at_m(x, y, m, b):
  diff = 0
  N = len(x)
  for i in range(N):
    y_val = y[i]
    x_val = x[i]
    diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -2 / N * diff
  return m_gradient

# step gradient
def step_gradient(b_current, m_current, x, y, learnign_rate):
  b_gradient = get_gradient_at_b(x, y, b_current, m_current)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  b = b_current - (learnign_rate * b_gradient)
  m = m_current - (learnign_rate * m_gradient)
  return [b, m]


# gradient descent
def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0
  m = 0
  for i in range(num_iterations):
    b, m = step_gradient(b, m, x, y, learning_rate)
  return b, m

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

b, m = gradient_descent(months, revenue, 0.01, 1000)
print(b, m)

# using Sklearn library

from sklearn.linear_model import LinearRegression
line_fitter = LinearRegression()
line_fitter.fit(X, y)
y_predicted = line_fitter.predict(X)