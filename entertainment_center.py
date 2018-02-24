import fresh_tomatoes
import media

'''
Create instances of each movie to be displayed

Attribution:
All storylines are taken from the films description on IMDB(www.imdb.com)
'''
princess_bride = media.Movie(
    'The Princess Bride',
    'While home sick in bed, a young boy\'s grandfather reads him a story called The Princess Bride.',
    'https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg',
    'https://www.youtube.com/watch?v=VYgcrny2hRs',
    'Rob Reiner',
    'September 25, 1987'
)

fifth_element = media.Movie(
    'The Fifth Element',
    'In the colorful future, a cab driver unwittingly becomes the central figure in the search for a legendary cosmic weapon to keep Evil and Mr. Zorg at bay.',
    'https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg',
    'https://www.youtube.com/watch?v=199EvXTKucc',
    'Luc Besson',
    '7 May 1997'
)

ferris_bueller = media.Movie(
    'Ferris Bueller\'s Day Off',
    'A high school wise guy is determined to have a day off from school, despite what the Principal thinks of that.',
    'https://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg',
    'https://www.youtube.com/watch?v=R-P6p86px6U',
    'John Hughes',
    'June 11, 1986'
)

legend = media.Movie(
    'Legend',
    'A young man must stop the Lord of Darkness from both destroying daylight and marrying the woman he loves.',
    'https://upload.wikimedia.org/wikipedia/en/9/98/Legendposter.jpg',
    'https://www.youtube.com/watch?v=als5pGB3Tfg',
    'Ridley Scott',
    'April 18, 1986'
)

willow = media.Movie(
    'Willow',
    'A reluctant dwarf must play a critical role in protecting a special baby from an evil queen.',
    'https://upload.wikimedia.org/wikipedia/en/7/7b/Willow_movie.jpg',
    'https://www.youtube.com/watch?v=JkSkdMw9qis',
    'Ron Howard',
    'May 20, 1988'
)

neverending_story = media.Movie(
    'The Neverending Story',
    'A troubled boy dives into a wondrous fantasy world through the pages of a mysterious book.',
    'https://upload.wikimedia.org/wikipedia/en/9/9b/Neverendingstoryposter.jpg',
    'https://www.youtube.com/watch?v=jRM0yLxMis4',
    'Wolfgang Petersen',
    '20 July 1984'
)


'''
Add each movie instance to list
'''
movies = [
    princess_bride,
    fifth_element,
    ferris_bueller,
    legend,
    willow,
    neverending_story
]

'''
Invoke program to launch trailer website
'''
fresh_tomatoes.open_movies_page(movies)
