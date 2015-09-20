from hashids import Hashids

from .conf import settings


def int_to_hashid(i, min_length=11, salt=settings.RESPONSIVE_WRAPPER_HASHIDS_SALT):
    hashids = Hashids(salt, min_length=min_length)
    return hashids.encode(i)


def hashid_to_int(hashid, min_length=11, salt=settings.RESPONSIVE_WRAPPER_HASHIDS_SALT):
    hashids = Hashids(salt, min_length=min_length)

    try:
        return hashids.decode(hashid)[0]
    except IndexError:
        pass
