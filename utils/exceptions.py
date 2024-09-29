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
        "message": "تعداد ارقام کمتر از 13 است"
    }



class PhoneNumberLong(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "PhoneNumberLong"
    default_detail = {
        "Long": "Phone number is longer than 13 character",
        "message": "تعداد ارقام شماره تلفن بیش 13 است."
    }




class PhoneNumberBadFormat(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "PhoneNumberBadFormat"
    default_detail = {
        "BadFormat": "Phone number should start with '+98'",
        "message": "فرمت شماره تلفن صحیح نمی باشد."
    }



class AmountValue(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "AmountValue"
    default_detail = {
        "BadFormat": "Amount must be a positive integer.",
        "message": "مبلغ باید عدد صحیح مثبت باشد."
    }



class InventoryNotEnough(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "InventoryNotEnough"
    default_detail = {
        "InventoryNotEnough": "Inventory is Not Enough.",
        "message": "موجودی حساب شما برای انجام این عملیات کافی نیست"
    } 



class NotAdmin(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "NotAdmin"
    default_detail = {
        "NotAdmin": "You Are Not Admin.",
        "message": "دسترسی به این سرویس تنها برای ادمین مجاز است."
    } 



class NotSeller(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "NotSeller"
    default_detail = {
        "NotSeller": "You Are Not Seller.",
        "message": "دسترسی به این سرویس تنها برای فروشنده مجاز است."
    }




class UserNotActive(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "UserNotActive"
    default_detail = {
        "UserNotActive": "Your Account Has Been Deactivated.",
        "message": "حساب شما غیر فعال شده است."
    }



class HasOpenChargeRequest(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "HasOpenChargeRequest"
    default_detail = {
        "HasOpenChargeRequest": "You Have an Open Charge Request.",
        "message": "شما در خواست شارژ تایید نشده دارید."
    } 



class ClientNotFound(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "ClientNotFound"
    default_detail = {
        "ClientNotFound": "Phone Number Does Not Exist.",
        "message": "کاربری باشماره تلفن وارد شده یافت نشد."
    } 



class ChargeClientFailed(CustomAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "ChargeClientFailed"
    default_detail = {
        "ChargeClientFailed": "Charge Client Failed.",
        "message": "شارژ شماره مورد نظر نا موفق بود."
    } 

    