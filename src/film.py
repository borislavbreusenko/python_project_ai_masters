class Film():
    def __init__(self, **kwargs: str) -> None:
        self.__nameRu = kwargs["nameRu"]
        self.__type = kwargs["type"]
        self.__year = kwargs["year"]
        self.__description = kwargs["description"]
        self.__filmLength = kwargs["filmLength"]
        self.__countries = kwargs["countries"]
        self.__genres = kwargs["genres"]
        self.__rating = kwargs["rating"]
        self.__ratingVoteCount = kwargs["ratingVoteCount"]
        self.__posterUrl = kwargs["posterUrl"]
        self.__posterUrlPreview = kwargs["posterUrlPreview"]

    def get_name(self) -> str:
        return self.__nameRu

    def get_year(self) -> str:
        return self.__year

    def get_genres(self) -> str:
        return ', '.join(self.__genres)

    def get_rating(self) -> str:
        return self.__rating

    def get_discribtion(self) -> str:
        return self.__description

    def get_poster(self) -> str:
        return self.__posterUrl

    def __str__(self) -> str:
        title = f'<b> {self.get_name()} {self.get_year()}</b> \n'
        rating = f'Рейтинг по Кинопоиску: <i> {self.get_rating()} </i> \n'
        desc = f'{self.get_discribtion()} \n'

        msg = f'{title}\n{rating}\n{desc}'
        return msg
