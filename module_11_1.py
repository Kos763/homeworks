import requests
import numpy as np
import matplotlib.pyplot as plt

def get_data(url):
    response = requests.get(url)
    data = response.text
    return data

def create_array(data):
    array = np.array(data.splitlines())
    return array

def plot_data(array):
    plt.plot(array)
    plt.title('Пример графика')
    plt.xlabel('Время')
    plt.ylabel('Значение')
    plt.grid(True)
    plt.show()

url = 'https://www.example.com/data.csv'
data = get_data(url)
array = create_array(data)
plot_data(array)
