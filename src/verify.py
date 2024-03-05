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
