# SVM Iris dataset predictor API
- Requires python 3.9 or higher

## Creating docker image
- run `pip install pipenv`
- run `pipenv sync`
- run `python model.py` or `python model.py` depending on your setup
    - This should generate a svm.ml file used by the main app once deployed
- run `docker build -t docker-ml-model -f dockerfile .`
- start the container by `docker run docker-ml-model` or `docker run -p 8001:8000 docker-ml-model` if you want to expose the docker port locally
- The requiest has the form `http://localhost:8001/iris?sepal_length=1&sepal_width=0&petal_length=0&petal_width=1`