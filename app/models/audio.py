class Audio:

    def __init__(self, name, extension, type, text, path, hashMD5, hashSHA256, duration, creationDate, modificationDate, size) -> None:
        self.id = 0
        self.name = name
        self.text = text
        self.extension = extension
        self.type = type
        self.path = path
        self.hashMD5 = hashMD5
        self.hashSHA256 = hashSHA256
        self.duration = duration
        self.creationDate = creationDate
        self.modificationDate = modificationDate
        self.size = size
