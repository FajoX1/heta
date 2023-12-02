import builtins

from .search import search
from .heta_hash import decode_hash
from .module import module
from .repo import repo

builtins.search = search
builtins.heta_hash = heta_hash
builtins.module = module
builtins.repo = repo

heta = type('heta', (), {'__getattr__': lambda _, name: getattr(builtins, name)})

__main__ = heta()