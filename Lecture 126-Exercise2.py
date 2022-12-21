# Program to store data in a dictionary input by user

info = {}

name = input('What is your name : ')
age = input('what is your age : ')
fav_movies = input('your favpurite movies separated by comma : ').split(',')
fav_songs = input('your favpurite songs separated by comma : ').split(',')

info['name'] = name
info['age'] = age
info['fav_movies'] = fav_movies
info['fav_songs'] = fav_songs

for key,value in info.items():
    print(key,":",value)