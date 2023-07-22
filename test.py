from matplotlib import pyplot as plt
# style = plt.style.available
# print(style)

# time = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# x= [2, 2, 1, 2, 2, 4, 3]
# y = [2, 3, 4, 5, 6, 5, 1]
# z = [6, 5, 5, 3, 2, 1, 6]
# labels = ["Ibnu", "John", "Jane"]
# plt.stackplot(time, x, y, z, labels = labels) 

# plt.legend(loc = "upper left")
# plt.show()

# data = [45, 56, 78, 67, 99]
# labels = ["Chelsea", "Man City", "Man United", "Barcelona", "Madrid"]
# colors_hex_codes = [
#     "#0000FF",  # Blue
#     "#40E0D0",  # Turquoise (Tosca)
#     "#FF0000",  # Red
#     "#EE82EE",  # Violet
#     "#FFFDD0",  # Cream
# ]

# plt.pie(data, labels = labels, 
#         colors = colors_hex_codes, wedgeprops=({'edgecolor': 'black'}), autopct= '%0.f%%')
# plt.show()

# data = [200, 10 , 90, 40, 60, 20]
# x = ["Jan", "Feb", "Mar","Apr", "May","Jun"]
# plt.plot(x, data, label = "trend", linewidth = 2, color = "red")
# plt.bar(x, data)
# plt.legend()
# plt.show()

# freya = [2, 4, 8, 6, 8, 9, 9, 7, 8, 10]
# ibnu = [2, 1, 5, 6, 7, 9, 9, 9, 9, 10]
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(freya))
# print(len(ibnu))
# print(len(x))
# plt.style.use('fivethirtyeight')
# plt.plot(x, freya, linewidth =2, color = "blue", label = "freya")
# plt.plot(x, ibnu, linewidth =2, color = "yellow", label = "Ibnu")
# above_freya = [i > j for i, j in zip(ibnu, freya)]
# below_freya = [i <= j for i, j in zip(ibnu, freya)]
# plt.fill_between(x, ibnu, freya, where = (above_freya), interpolate= True, color= "yellow", alpha = 0.25, label ="above freya")
# plt.fill_between(x, ibnu, freya, where = (below_freya), interpolate= True, color= "blue", alpha = 0.25, label ="below freya")
# plt.legend()
# plt.tight_layout()
# plt.show()
# import random
# weights = []
# for _ in range(1000):
#     weight = random.uniform(55, 100)
#     weights.append(weight)
# print(weights)
# bins = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
#
# plt.hist(weights, bins = bins, edgecolor = "black")
# plt.show()