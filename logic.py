from random import randint
import requests


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)

    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer

        self.pokemon_number = randint(1, 1000)
        self.img = self.get_full_image()
        self.name = self.get_name()
        self.hp = randint(1, 100)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        pass

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['name'])
        else:
            return 'Pikachu'

    def get_front_image(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fanime-characters-fight.fandom.com%2Fru%2Fwiki%2F%25D0%259F%25D0%25B8%25D0%25BA%25D0%25B0%25D1%2587%25D1%2583_%25D0%25AD%25D1%2588%25D0%25B0&psig=AOvVaw1x8ss28AIPpm2Huin42RCo&ust=1701087406215000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLCZwMjS4YIDFQAAAAAdAAAAABAE'

    def get_back_image(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['back_default'])
        else:
            return 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fanime-characters-fight.fandom.com%2Fru%2Fwiki%2F%25D0%259F%25D0%25B8%25D0%25BA%25D0%25B0%25D1%2587%25D1%2583_%25D0%25AD%25D1%2588%25D0%25B0&psig=AOvVaw1x8ss28AIPpm2Huin42RCo&ust=1701087406215000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLCZwMjS4YIDFQAAAAAdAAAAABAE'

    def get_full_image(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fanime-characters-fight.fandom.com%2Fru%2Fwiki%2F%25D0%259F%25D0%25B8%25D0%25BA%25D0%25B0%25D1%2587%25D1%2583_%25D0%25AD%25D1%2588%25D0%25B0&psig=AOvVaw1x8ss28AIPpm2Huin42RCo&ust=1701087406215000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLCZwMjS4YIDFQAAAAAdAAAAABAE'

    # Метод класса для получения информации

    def info(self):
        return f'Тренер покемона: @{self.pokemon_trainer}\nИмя твоего покеомона: {self.name}\nЗдоровье покемона: {self.hp}%'

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
