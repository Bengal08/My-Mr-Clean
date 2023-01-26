import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import random

def get_content(article_name):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "extracts",
        "titles": article_name,
        "format": "json"
  
    }
  
    data = requests.get(url, params=params)
    return data.json()

CLEANING
data = get_content("Ozone_layer")
#print(data)

def merge_contents(data):
      required_data = list(data["query"]["pages"].values())[0]["extract"]
      soup = BeautifulSoup(required_data, "html.parser").text
      return soup


merged_content = merge_contents(data)
#print(merged_content)

TOKENIZATION
def tokenize(content):
    splitter = re.split("\. |, |\.|\n| |-|\'", content)
    words = []
    for i in splitter:
        if i.isalpha():
            words.append(i)
    return words

stop_words = ["the", "of", "and", "in", "to", "is", "a", "by"]
collection = tokenize(merged_content)
#print(collection)

def lower_collection(collection):
    lower_words = [word.lower() for word in collection]
    return lower_words

collection = lower_collection(collection)
#print(collection)

Term Frequency
count Frequency
def count_frequency(collection):
    frequency = {}
    for word in collection:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
def print_most_frequent(frequencies, n):
    for i in range(n):
        word, freq = max(frequencies.items(), key=lambda x: x[1])
        print(f"{word}: {freq}")
        del frequencies[word]

frequencies = count_frequency(collection)
print_most_frequent(frequencies, 10)


Filtering
def remove_stop_words(words, stop_words):
    stop_words = set(stop_words)
    return (word for word in words if word not in stop_words)


collection = tokenize(merged_content)
collection = lower_collection(collection)

filtered_collection = remove_stop_words(collection, stop_words)
print(list(filtered_collection))

Visualizing
def visualizing(frequencies, n):
    words = []
    counts = []
    colors = []
    for i in range(n):
        word, freq= max(frequencies.items(), key=lambda x: x[1])
        words.append(word)
        counts.append(freq)
        colors.append('#%06X' % random.randint(0, 0xFFFFFF))
        del frequencies[word]
    
    plt.figure(figsize=(20, 10))
    plt.xlabel("Most Common Tokens in the Ozone layer article")
    plt.barh(words[::-1], counts[::-1], color=colors[::-1])
    plt.show()

filtered_collection = list(remove_stop_words(collection, stop_words))
if len(filtered_collection) == 0:
    print("filtered_collection is empty")
else:
    frequencies_filtered = count_frequency(filtered_collection)
    visualizing(frequencies_filtered,  20)    
#frequencies = count_frequency(collection)
#visualizing(frequencies, 20)
