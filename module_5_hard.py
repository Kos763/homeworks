class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

    def __str__(self):
        return f'{self.nickname}'


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return True
            return False

    def register(self, nickname, password, age):
        if self.log_in(nickname, password):
            print('Такой пользователь существует!')
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[-1]
            print(f'Пользователь {self.users[-1]} успешно зарегестрирован')

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if str(video) not in self.videos:
                self.videos.append(video)

    def get_videos(self, text: str):
        result = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                result.append(video.title)
        return result

    def watch_video(self, video_title):
        if self.current_user is None:
            print('Войдите в аккаунт')
            return
        for video in self.videos:
            if video.title == video_title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам  нет 18 пожалуйста покиньте страницу!')
                    return
                for i in range(video.duration):
                    print(i, end=' ')
                    video.time_now += 1
                video.time_now = 0
                print('Конец видео')


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
