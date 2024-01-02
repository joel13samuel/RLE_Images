from console_gfx import ConsoleGfx


def to_hex_string(data):
    # string is for each values index to be checked
    string = "0123456789abcdef"
    # empty string for everything to be added to
    hex_string = ""
    # for loop to add everything to the empty string
    for i in data:
        hex_string = hex_string + string[i]
    return hex_string


def count_runs(flat_data):
    # current to hold place marker
    current = flat_data[0]
    # value to return
    count = 1
    # current count for the exception to a number being repeated more than 15 times
    current_count = 1

    # for loop that gets the value for count
    for i in flat_data[1:]:
        # checks these two conditions first
        if current == i and current_count < 15:
            current_count += 1
        else:
            count += 1
            current = i
            current_count = 1
    return count


def encode_rle(flat_data):
    # very similar to count_runs but uses a list to hold values
    lst = []
    current = flat_data[0]
    current_count = 1

    # for loop to append the count of the value then the value itself
    for i in flat_data[1:]:
        if current == i and current_count < 15:
            current_count += 1
        else:
            lst.append(current_count)
            lst.append(current)
            current = i
            current_count = 1
    # accounts for the last item
    lst.append(current_count)
    lst.append(current)

    return lst


def get_decoded_length(rle_data):
    # uses enumerate to get the length of the decoded rle data
    sum_even = 0
    for index, item in enumerate(rle_data):
        if index % 2 == 0:
            sum_even += item
    return sum_even


def decode_rle(rle_data):
    # has a lst to store the values in
    lst = []
    # gets the count and then uses a for loop to print it that many times
    for index, item in enumerate(rle_data):
        if index % 2 == 0:
            for i in range(rle_data[index]):
                lst.append(rle_data[index + 1])
    return lst


def string_to_data(data_string):
    # similar to encode rle but instead reverses it by using the index
    string = "0123456789abcdef"
    lst = []
    for i in range(len(data_string)):
        lst.append(string.index(data_string[i]))
    return lst

def to_rle_string(rle_data):
    strs = ""
    count = 0
    string = "0123456789abcdef"
    for index,item in enumerate(rle_data):
        count += 1
        if index % 2 == 1:
            strs += string[item]
        else:
            strs += str(item)
        if count % 2 == 0:
            strs += ":"
    return strs[0:-1]

def string_to_rle(rle_string):
    lst = rle_string.split(":")
    lst2 = []
    string = "0123456789abcdef"
    str = ""
    for i in lst:
        if len(i) == 3:
            lst2.append(int(i[0:2]))
            lst2.append(int(string.index(i[2])))
        else:
            lst2.append(int(i[0]))
            lst2.append(int(string.index(i[1])))
    return lst2

if __name__ == '__main__':

    # TODO: print out the welcome message
    # TODO: print out Displaying spectrum image message
    image_data = None
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print()
    print()

    run = True
    while run:
        # TODO: print out the RLE menu with all the menu options
        print("RLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data\n")

        # TODO: prompt the user for a menu selection - menu_option

        menu_option = input("Select a Menu Option: ")

        # TODO: when menu option is equal to 1
        #   TODO: prompt the user user for file name
        # image_data = ConsoleGfx.load_file(filename)

        if menu_option == "0":
            run = False

        elif menu_option == "1":
            file_name = input("Enter name of file to load: \n")
            image_data = ConsoleGfx.load_file(file_name)

        # TODO: when menu option is equal to 2
        # TODO: update image_data to be ConsoleGfx.test_image
        elif menu_option == "2":
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.\n")

        # takes in the data and decodes the rle
        elif menu_option == "3":
            rle_data = input("Enter an RLE string to be decoded: ")
            print()
            a = string_to_rle(rle_data)
            image_data = decode_rle(a)

        # takes in the data containing the hex string holding rle data and then decodes it
        elif menu_option == "4":
            rle_data = input("Enter the hex string holding RLE data: ")
            rle_data = rle_data.lower()
            print()
            a = string_to_data(rle_data)
            image_data = decode_rle(a)

        #takes in the data as a hex string holding flat data and converts it
        elif menu_option == "5":
            rle_data = input("Enter the hex string holding flat data: ")
            print()
            image_data = string_to_data(rle_data)

        # TODO: when menu option is equal to 6
        # TODO: display the image using image_data
        elif menu_option == "6":
            print("Displaying image...")
            ConsoleGfx.display_image(image_data)
            print()

        # prints out the rle rep.
        elif menu_option == "7":
            b = encode_rle(image_data)
            print("RLE Representation: ", end="")
            print(to_rle_string(b))
            print()

        # prints out the rle hex values
        elif menu_option == "8":
            b = encode_rle(image_data)
            print("RLE hex values: ", end="")
            print(to_hex_string(b))
            print()

        # prints out the flat hex values
        elif menu_option == "9":
            print("Flat hex values: ", end="")
            print(to_hex_string(image_data))
            print()

