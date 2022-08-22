# Movie_website_scraper

This is a porgram that uses pythons BeautifulSoup library for scraping data from a movie website. 
The data is scraped from - Empires 100 greates movies of all time. Relevant information is pulled out, like the title and the ranking of each movie. The next step is saving the data into a file 'movies.txt' as a list of movies that can be watched later.


The scraped data from the top 100 movies of all time from the website https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/ is stored in a file called `movies.txt`. This file lists the movies titles in ascending order (starting from 1). 


'movies.txt' file looks something like this:
```
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
5) Pulp Fiction
6) Goodfellas
7) Raiders Of The Lost Ark
8) Jaws
9) Star Wars
10) The Lord Of The Rings: The Fellowship Of The Ring
... and so on
```


The program was developed using python 3.10.6, BeautifulSoup, requests. 

In order to run the program, you have to execute the main.py.