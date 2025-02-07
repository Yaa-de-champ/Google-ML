import random

# data = random.random()
# print(data)
#
# data = round(random.random(), 5)
# print(data)
#
# data = random.uniform(-20, 20)
# print(data)
#
# data = random.randint(10, 30)
# print(data)

# features = ['Age', 'Weight', 'Height', 'Complexion']
# # data = random.choice(features)
# data = random.choices(features, k=3)
# # data = random.sample(features, k=3) #no repitions
#  print(data)

# data = list(range(1, 14))
# print(data)

# features = ['Age', 'Weight', 'Height']
# data = random.choices(features, weights=[10, 10, 5], k=10)
# print(data)
# # 10/25 * 10


import random

def generate_data(size):
    fruits_list = ['mango', 'orange', 'pineapple', 'pear']
    colour_list = ['orange', 'yellow', 'green', 'brown']
    data = []

    for _ in range(size):
        weight = round(random.uniform(0.5, 5.1), 2)

        if weight <= 0.9:
            fruit = random.choice(['mango', 'orange'])
        else:
            fruit = random.choice(['pineapple', 'pear'])

        data.append([weight, fruit])
    return data

data = generate_data(20)
print(data)