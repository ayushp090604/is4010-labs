import json


class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename

        try:
            with open(filename, "r") as file:
                self.favorites = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.favorites = {}

    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.favorites, file)

    def add(self, name, location):
        key = name.lower()

        if key in self.favorites:
            return False

        self.favorites[key] = location
        self.save()
        return True

    def remove(self, name):
        key = name.lower()

        if key not in self.favorites:
            return False

        del self.favorites[key]
        self.save()
        return True

    def list_all(self):
        return self.favorites.copy()

    def get_location(self, name):
        return self.favorites.get(name.lower())