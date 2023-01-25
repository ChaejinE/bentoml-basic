import bentoml

bento = bentoml.get("iris_classifier:latest")

print(bento.tag)
print(bento.path)
print(bento.info.to_dict())
