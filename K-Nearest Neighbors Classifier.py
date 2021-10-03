# K-Nearest Neighbors Classifier

# Distance
star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]

def distance(movie1, movie2):
    distance = 0
    for i in range(len(movie1)):
        distance += (movie1[i] - movie2[i])**2
    return distance**0.5


print(distance(star_wars, raiders))
print(distance(star_wars, mean_girls))

# Normalization min-max: (value - min) / (max - min)
release_dates = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011, 1965, 1891, 1978]

def min_max_normalize(lst):
    minimum = min(lst)
    maximum = max(lst)
    normalized = []
    for value in lst:
        norm_value = (value-minimum) / (maximum-minimum)
        normalized.append(norm_value)
    return normalized


print(min_max_normalize(release_dates))

# Classifier

#print(movie_dataset['Bruce Almighty']) -> [0.006630902005283176, 0.21843003412969283, 0.8539325842696629]
#print(movie_labels['Bruce Almighty'])  -> 0 (0-bad, 1- good)

def classify(unknown, dataset, labels, k):
  distances = []
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    distances.append([distance_to_point, title])
  distances.sort()
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0


# print('Call Me By Your Name' in movie_dataset)
my_movie = [350000, 132, 2017]
normalized_my_movie = min_max_normalize(my_movie)

print(classify(normalized_my_movie, movie_dataset, movie_labels, 5))


# Choosing K and validation accuracy
def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
  num_correct = 0.0
  for title in validation_set:
    guess = classify(validation_set[title], training_set, training_labels, k)
    if guess == validation_labels[title]:
      num_correct += 1

  return num_correct / len(validation_set)

print(find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, 5))

# Using sklearn

from sklearn.neighbors import KNeighborsClassifier


classifier = KNeighborsClassifier(5)
classifier.fit(movie_dataset, labels)
print(classifier.predict([[0.45, 0.2, 0.5], [0.25, 0.8, 0.9], [0.1, 0.1, 0.9]]))



