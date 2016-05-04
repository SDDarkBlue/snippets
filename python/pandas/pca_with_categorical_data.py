import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn.feature_extraction import DictVectorizer

d = [['yes', 'no', 'yes'], ['yes', 'yes', 'no'], ['yes', 'no', 'no'], ['no', 'yes', 'yes'], ['no', 'no', 'yes'], ['no', 'no', 'no']]
target = [0, 1, 0, 1, 0, 1]
dc = []
for datap in d:
    dc.append({'one': datap[0], 'two': datap[1], 'three': datap[2]})
# This vectorize will help us transform categorical data to a sparse matrix
dv = DictVectorizer()
X = dv.fit_transform(dc)
# X is now a sparse matrix, however, pca needs a dense matrix. Therefore, use X.toarray()

pca = decomposition.PCA(n_components=2)
pca.fit(X.toarray())
X2 = pca.transform(X.toarray())
plt.scatter([d[0] for d in X2], [d[1] for d in X2], c=target)
plt.show()
