import numpy as np

timbreVector = {
    'loudness': 1,
    'brightness': 2,
    'flatness': 3,
    'attack': 4,
    'b1': 5,
    'b2': 6,
    'b3': 7,
    'b4': 8,
    'b5': 9,
    'b6': 10,
    'b7': 11,
    'b8': 12
}


'''
 Saves the cluster centroids of the given 3 features sets to `clusterCentroid.bin`
 File Format: [Year, cent_x, cent_y, cent_z]
 Limit: Limits the data for each year
'''
def clusterCentroid(train, features, limit):
    centroids = []

    years = np.unique(train[:,0])

    for year in years:
        rowRng = (train[:,0] == year).nonzero()[0]

        x, y, z = [], [], []
        limitC = 0
        for row in rowRng:
            x.append(train[row][timbreVector[features[0]]])
            y.append(train[row][timbreVector[features[1]]])
            z.append(train[row][timbreVector[features[2]]])

            if limitC == limit:
                break

        x, y, z = np.array(x), np.array(y), np.array(z)

        cent_x = np.sum(x)/x.shape[0]
        cent_y = np.sum(y)/y.shape[0]
        cent_z = np.sum(z)/z.shape[0]

        print "[SUCCESS] Year: ", year, " Centroids", cent_x, cent_y, cent_z

        centroids.append(np.array([year, cent_x, cent_y, cent_z]))

    with open('bin/clusterCentroid.bin', 'wb') as f:
        np.save(f, np.array(centroids))
        print "[SUCCESS] Saved as `clusterCentroid.bin`"

'''
'''
def predict(features):
    with open('bin/clusterCentroid.bin', 'r') as f:
        centroids = np.load(f)
        c1 = centroids[:,1]
        c2 = centroids[:,2]
        c3 = centroids[:,3]

        c1 = np.square(c1-features[0])
        c2 = np.square(c2-features[1])
        c3 = np.square(c2-features[2])

        ind = np.argmin(c1 + c2 + c3)

        predicted = centroids[ind]
        centDist = np.sqrt(
            np.square(features[0]-predicted[1])+
            np.square(features[1]-predicted[2])+
            np.square(features[2]-predicted[3]))

        return np.append(predicted, [centDist])

if __name__ == '__main__':
    with open('bin/train.bin', 'r') as f:
        train = np.load(f)
        features = ['loudness', 'flatness', 'b3']

        # clusterCentroid(train, features, -1)
        print predict([43.3, 5.2, -2.7])
