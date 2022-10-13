import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def read_file(name):
    movies_file = open(name, 'r')
    count_of_views = movies_file.readline()
    movie = movies_file.readline()
    movies = []
    while movie != '':
        movies.append(int(movie))
        movie = movies_file.readline()
    movies_file.close()
    return movies

file = input("File name: ")
list_of_movies = read_file(file)
set_of_movies = sorted(list(set(list_of_movies)))
(mu, sigma) = norm.fit(list_of_movies)
x = np.linspace(min(list_of_movies), max(list_of_movies), 100)
values, bins, _ = plt.hist(list_of_movies, bins=12)
area = sum(np.diff(bins) * values)
plt.plot(x, norm.pdf(x, mu, sigma) * area, 'r')
plt.savefig(file[:-3] + 'png')
plt.show()
