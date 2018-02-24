#!/usr/bin/env python
# coding: utf-8
# author: Kevin Wing <kevinrwing@gmail.com>
# created: 9/29/17
# modified 9/29/17


class Movie():
    '''This class provides a way to store movie related information'''

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube,
        movie_director,
        release_date
    ):
        '''
        Initializes instance of Movie and provides access to instance related
        properties.
        Takes in 6 inputs as strings and stores them:
            Title
            Storyline
            Thumbnail image link
            Movie trailer link
            Director
            Release date
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_director = movie_director
        self.release_date = release_date
