from rest_framework.exceptions import APIException
from rest_framework import status
from abc import ABC

class CustomAPIException(APIException, ABC):
    status_code = NotImplemented
    default_code = NotImplemented
    default_detail = NotImplemented
    log_exception = True


class NonePhoneNumber(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "NonePhoneNumber"
    default_detail = {
        "NonePhoneNumber": "Somthing Went Wrong While Recieving Your PhoneNumber.",
        "message": "مشکلی در دریافت شماره تلفن از سمت شما به وجود آمده است."
    }



class PhoneNumberShort(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "PhoneNumberShort"
    default_detail = {
        "Short": "Phone number is shorter than 13 character",
        "message": "شماره تلفن باید 11 رقم باشد"
    }



class PhoneNumberLong(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "PhoneNumberLong"
    default_detail = {
        "Long": "Phone number is longer than 13 character",
        "message": "تعداد ارقام شماره تلفن بیش از حد مجاز است."
    }




class PhoneNumberBadFormat(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "PhoneNumberBadFormat"
    default_detail = {
        "BadFormat": "Phone number should start with '+98'",
        "message": "فرمت شماره تلفن صحیح نمی باشد."
    }