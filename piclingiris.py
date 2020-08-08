import pickle
import requests

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
response = requests.get(url)
respon = response.text
data = respon.splitlines()
red = [[i] for i in data]

file = open("pic.pkl","wb")
pickle.dump(red,file)
file.close()

file = open("pic.pkl",'rb')
data = pickle.load(file)
print(data)