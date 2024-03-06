from db.database import *
import string


def IS_MANAGER(id, password):
    try:
        if is_manager(int(id)):

            flname = employee_info(int(id), password)
            try:
                if flname:

                    print(flname)
                    return True
                else:
                    print("you are not manager ")
            except Exception as err:
                print(err)
        else:
            print("incorrect id or password")
    except Exception as err:
        print(err)
    return False


def IS_EMPLOYEE(id, password):
    try:

        flname = employee_info(int(id), password)
        try:
            if flname:

                print(flname)
                return flname
            else:
                print("enter correct password or id")
        except Exception as err:
            print(err)

    except Exception as err:
        print(err)
    return False


def CHECK_PHONE_EXIST(phone_number):
    phone_number = phone_number.strip('0')
    print('phone number:', phone_number)
    try:
        print("1")
        if res := phone_number_lookup(phone_number):
            print(res)
            print("this phone number exist")
            print('user id', res[0][0])

            return True
        else:
            print("this phone number not exist")
            return False
    except Exception as err:
        print(err)


def CHECK_IN_PASS_EQ_GEN_PASS(input_pass, genrate_pass):
    try:
        if input_pass == genrate_pass:
            return True
        else:
            print("incorrect code")
    except:
        print("CHECK_IN_PASS_EQ_GEN_PASS err")

    return False


def PHONE_NUMBER_EMPTY(phone_number):
    if bool(phone_number.strip()):
        print('pn', phone_number)
        return False
    else:
        return True


def IS_DRIVER(phone_number):
    phone_number = phone_number.strip('0')
    res = phone_number_lookup(phone_number)
    if is_driver_account_active(res[0][0]):
        return res
    else:
        return False


def IS_CLIENT(phone_number):
    phone_number = phone_number.strip('0')
    res = phone_number_lookup(phone_number)
    if is_client_account_active(res[0][0]):
        return res
    else:
        return False


def CHECK_ID_DRIVER(phone_number):
    phone_number = phone_number.strip('0')

    return phone_number_lookup(phone_number)
