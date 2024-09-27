
from . import exceptions


def phone_number_validator(phone_number: str):
    if not phone_number:
        raise exceptions.NonePhoneNumber()

    if len(phone_number) != 13:
        if len(phone_number) < 13:
            raise exceptions.PhoneNumberShort()
        raise exceptions.PhoneNumberLong()

    if phone_number[:3] != "+98" or not phone_number[3:].isnumeric():
        raise exceptions.PhoneNumberBadFormat()
    return phone_number