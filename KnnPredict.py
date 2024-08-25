#This is a basic implementation of the prediction method that works in a KNN algorithm, we are given data, labels, distance k and object distances.
#We calculate the Euclidean distance for all the elements in the training data set and obtain the distance for the new data (in this case, we're using the index 87 just to simplify the example).
#So, if the length of the data set is 80, the algorithm will calculate the distance for all 80 instances and then classify them and, based on our k, we can classify which category the new data belongs to.

distances = {}
def predict(data, labels, k, distances):   
    for i in range(data.shape[0]):
        euclidean_distance = 0
        for j in range(data.shape[1]):
            #The index 87 is simulating a new data
            euclidean_distance += (data[i][j] - data[87][j]) ** 2
        distances[i] = np.sqrt(euclidean_distance)
        print('belongs to class:', labels[i])
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    for i in range(k):
        print(labels[sorted_distances[i][0]], 'ss')
    print(labels[87], 'a')
    print(sorted_distances)
predict(wine_data, wine_labels, 5, distances)
