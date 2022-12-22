def Magik_data():
    date = input().split('.')
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        return True
    else:
        return False

print(Magik_data())