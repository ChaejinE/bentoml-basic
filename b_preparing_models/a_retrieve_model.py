import bentoml

bentoml_model: bentoml.Model = bentoml.models.get("iris_clf:latest")

print(bentoml_model.tag)
print(bentoml_model.path)
print(bentoml_model.custom_objects)
print(bentoml_model.info.metadata)
print(bentoml_model.info.labels)

my_runner: bentoml.Runner = bentoml_model.to_runner()
print(f"Runner : {my_runner}")
