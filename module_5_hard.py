from time import sleep


class UrTube:
    def __init__(self, users = [], videos = [], current_user = ''):
        self.users = users
        self.videos = videos
        self.current_user = current_user
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        nicknames = []
        for user in self.users:
            nicknames.append(user.nickname)
        if nickname not in nicknames:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует ')

    def add(self, *args):
        videos = []

        for video in self.videos:
            videos.append(video.title)

        for arg in args:
            if arg.title not in videos:
                self.videos.append(arg)

    def get_videos(self, search_word):
        search_result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                search_result.append(video.title)
        return search_result


    def watch_video(self, title):
        if self.current_user == "":
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if title == video.title:
                    if video.adult_mode == True and self.current_user.age >= 18:
                        for i in range(1, video.duration+1):
                            sleep(1)
                            print(i, end=' ')
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста, покиньте страницу')





class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
class User:
    def __init__(self, nickname: str, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')