package_info = "Asynchronous file operations"
version_info = (0, 1, 0)


author_info = (
    ('Dmitry Orlov', 'me@mosquito.su'),
)

author_email = ", ".join("{}".format(info[1]) for info in author_info)

license = "Apache 2"

__version__ = ".".join(str(x) for x in version_info)
__author__ = ", ".join("{} <{}>".format(*info) for info in author_info)


__all__ = (
    '__author__',
    '__version__',
    'author_info',
    'license',
    'package_info',
    'version_info',
    'AIOFile',
    'Reader',
    'Writer',
)


try:
    from ._aio import AIOFile as _AIOFile
except ImportError:
    from ._thread import AIOFile as _AIOFile

from .utils import Reader, Writer
