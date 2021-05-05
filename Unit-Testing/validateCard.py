import datetime
from datetime import *


def validateCard(exp):
    if exp >= datetime.now().date():
        print("Card is valid")
        return 'Valid'
    else:
        print("Card has expired")
        return 'Expired'


def validateCardException(exp):
    if exp >= datetime.now().date():
        print("Card is valid")
        return 'Valid'
    else:
        print("Card has expired")
        raise RuntimeError('Card has Expired')