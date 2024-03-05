from db.database import *


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
                return True
            else:
                print("enter correct password or id")
        except Exception as err:
            print(err)

    except Exception as err:
        print(err)
    return False


def CHECK_PHONE_NOT_EXIST(phone_number):
    print('phone number enter: ', )
    phone_number = phone_number.strip('0')
    print('phone number send to db:', phone_number)
    try:
        if not phone_number_exists(phone_number):

            return True
        else:
            print("this phone number already exist")
    except Exception as err:
        print(err)
    return False


def CHECK_IN_PASS_EQ_GEN_PASS(input_pass, genrate_pass):
    try:
        if input_pass == genrate_pass:
            return True
        else:
            print("incorrect code")
    except:
        print("CHECK_IN_PASS_EQ_GEN_PASS err")

    return False
