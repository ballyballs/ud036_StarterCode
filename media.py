class Video():
    def __init__(self, title, video_url, video_duration, video_coverart, video_release_date):
        self.title = title
        self.video_url = video_url
        self.video_duration = video_duration
        self.video_coverart = video_coverart
        self.video_release_date = video_release_date

class Movie(Video):
    def __init__(self, title, video_url, video_duration, video_coverart, video_release_date, movie_actor, movie_actress):
        Video.__init__(self, title, video_url, video_duration, video_coverart, video_release_date)
        self.movie_actor = movie_actor
        self.movie_actress = movie_actress

class Music(Video):
    def __init__(self, title, video_url, video_duration, video_coverart, video_release_date, music_artist):
        Video.__init__(self, title, video_url, video_duration, video_coverart, video_release_date)
        self.music_artist = music_artist

class TV_Show(Video):
    def __init__(self, title, video_url, video_duration, video_coverart, video_release_date, season):
        Video.__init__(self, title, video_url, video_duration, video_coverart, video_release_date)
        self.season = season
        
    
        
