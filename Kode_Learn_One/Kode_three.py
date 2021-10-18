

def exceptionhandling():
    car={'make': 'BMW', 'model': '10h', 'year': 2021 }

    try:
        print(car['year'])

    except:
        print("haha")

    else:
        print("no exception so in else")

    finally:
        print("end")

exceptionhandling()