
from fastapi import FastAPI
from joblib import load

app = FastAPI()

SVM = load('svm.ml')
print(SVM.predict([[2, 0, 0, 1]]))

@app.get("/iris")
async def predictClass(
    sepal_length: float, 
    sepal_width:float, 
    petal_length:float, 
    petal_width:float):
    prediction = int(SVM.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0])
    response = {"class": prediction}
    return response