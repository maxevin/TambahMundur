def reverse(string):
    # the string are listed
    string = list(string)
    reversed_string = ''

    # loop the list using 'reversed'
    for i in reversed(string):
        reversed_string += i

    # return the function with string that already reversed (e.g : from 1245 into 5421)
    return reversed_string

def tambahMundur(x,y):
    # convert variable x & y from integer into string
    string_x = str(x)
    string_y = str(y)

    # call reverse function, convert into integer, and sum it into 'jumlah' variable
    jumlah = int(reverse(string_x)) + int(reverse(string_y))

    # return the function by convert 'jumlah' into string, call reverse function and convert it into integer
    return int(reverse(str(jumlah)))

while True:
    x = input('Masukkan Angka 1 : ')
    if x.isnumeric() and int(x) < 359999:
        y = input('Masukkan Angka 2 : ')

        if y.isnumeric() and int(x) < 359999:
            # when x and y already set, call tambahMundur function by convert x and y into integer
            print('Hasil tambah mundurnya :',tambahMundur(int(x),int(y)))

        else:
            print('Invalid Input!')
            break
        
    else:
        print('Invalid Input!')
        break