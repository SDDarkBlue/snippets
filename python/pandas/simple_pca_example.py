import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import decomposition

iris = datasets.load_iris()

pca = decomposition.PCA(n_components=2)
pca.fit(iris.data)
X = pca.transform(iris.data)
plt.scatter([d[0] for d in X], [d[1] for d in X], c=iris.target)
plt.show()
