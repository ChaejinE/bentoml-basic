import bentoml

from sklearn import svm
from sklearn import datasets

iris = datasets.load_iris()
X, y = iris.data, iris.target

clf = svm.SVC(gamma="scale")
clf.fit(X, y)

saved_model = bentoml.sklearn.save_model("iris_clf", clf)
print(f"Model saved : {saved_model}")

loaded_model = bentoml.sklearn.load_model("iris_clf:latest")
print(f"loaded Model : {loaded_model}")
