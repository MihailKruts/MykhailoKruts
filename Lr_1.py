import math

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

def write_frequency(movies, lst):
    result = open('result.txt', 'w')
    result.writelines("—" * 45 + '\n')
    result.writelines('|Movie number|Frequency|Cumulative frequency|\n')
    result.writelines('—' * 45 + '\n')
    cumulative_frequency = 0
    for movie in movies:
        number = str(movie).center(12)
        frequency = str(lst.count(movie)).center(9)
        cumulative_frequency += int(frequency)
        result.writelines(f'|{number}|{frequency}|{str(cumulative_frequency).center(20)}|\n')
        result.writelines('—' * 45 + '\n')
    result.writelines(f"|{'Total'.center(12)}|{str(cumulative_frequency).center(30)}|\n")
    result.writelines('—' * 45 + '\n')
    result.close()

def find_the_median(movies):
    if len(movies) % 2 == 0:
        return (movies[len(movies)//2] + movies[len(movies)//2 - 1]) / 2
    else:
        return movies[(len(movies) - 1)//2]

def find_the_mode(movies, frequencies):
    mode = []
    for index, frequency in enumerate(frequencies):
        if frequency == max(frequencies):
            mode.append(movies[index])
    return mode

def find_the_variance(movies, lst, frequencies):
    return sum([(movies[x]**2)*frequencies[x] for x in range(len(movies))])/sum(frequencies) - (sum(lst)/len(lst))**2    

if __name__ == "__main__":
    #Part_1
    file = input("File name: ")
    list_of_movies = read_file(file)
    set_of_movies = sorted(list(set(list_of_movies)))
    write_frequency(set_of_movies, list_of_movies)
    frequencies = []
    for movie in set_of_movies:
        frequencies.append(list_of_movies.count(movie))
    mode = find_the_mode(set_of_movies, frequencies)
    result = open('result.txt', 'a')
    if len(mode) == 1:
        result.writelines(f"The most watched movie: {mode[0]}\n")
    else:
        result.writelines(f"The most watched movies: {', '.join(list(map(str, mode)))}\n")
    #Part_2
    result.writelines(f"Median: {find_the_median(set_of_movies)}\n")
    if len(mode) == 1:
        result.writelines(f"Mode: {mode[0]}\n")
    else:
        result.writelines(f"Mode: {', '.join(list(map(str, mode)))}\n")
    #Part_3
    variance = find_the_variance(set_of_movies, list_of_movies, frequencies)
    standard_deviation = math.sqrt(variance)
    result.writelines(f"Variance: {format(variance, '.2f')}\n")
    result.writelines(f"Standard deviation: {format(standard_deviation, '.2f')}\n")
    result.close()
    print("Дані збережено у файлі result.txt")

