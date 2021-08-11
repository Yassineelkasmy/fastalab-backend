from datetime import datetime, timedelta
import dateutil.parser
from jose import jwt
import string
import random


from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):

    return pwd_context.verify(plain_password, hashed_password)




def get_password_hash(password):

    return pwd_context.hash(password)

def pin_code_genrator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def verify_expire_date(strDate:str) -> bool:
    date = dateutil.parser.parse(strDate)
    diff = datetime.utcnow() - date
    if diff.days < 0:
        return True
    else:
        return False