from app.database.instaTwinDB import get_twin_by_personId


class Person:

    def __init__(self, name, doc, email, history, id=0,) -> None:
        self.id = id
        self.name = name
        self.doc = doc
        self.email = email
        self.history = history

    def get_person_data(self, socialmedia=None):
        if socialmedia is None:
            return self.id, self.name, self.doc, self.email, self.history
        else:
            if socialmedia=='Instagram':
                return get_twin_by_personId(self.id)
            else:
                return 'Twin não implementado'

    def get_person_and_twins_data(self):
        istatwin = get_twin_by_personId(self.id)
        person = self.get_person_data()
        return istatwin, person