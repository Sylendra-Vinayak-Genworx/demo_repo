class ApplicationError(Exception):
    """Base application exception."""


class NotFoundError(ApplicationError):
    pass
