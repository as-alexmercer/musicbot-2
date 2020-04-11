class MusicbotError(Exception):
    pass


class MusicbotConfigError(MusicbotError):
    pass


class FailedAuthentication(MusicbotError):
    pass


class FailedRequest(MusicbotError):
    pass