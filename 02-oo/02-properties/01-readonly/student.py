class MusicalNote:
    def __init__(self, name, pitch):
        self._name = name
        self._pitch = pitch

    @property
    def name(self):
        return self._name

    @property
    def pitch(self):
        return self._pitch
