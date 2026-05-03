def read_a_number_from_file(path):
    try:
        f = open(path, "r")
        contents = f.read()
        number = int(contents)              # may raise a ValueError
    except FileNotFoundError:
        print("File not found")
        return None
    except ValueError:
        print("The value is not a whole number")
        return None
    except Exception as e:
        print("The following error has occurred:",e)
    else:
        print("Number read successfully:", number)
        return number
    finally:
        # Always executed – regardless of whether there is an error or not
        try:
            f.close()
            print("Close file")
        except UnboundLocalError:
            # f was never created (e.g. in the case of a FileNotFoundError before the open operation)
            pass

read_a_number_from_file("number.txt")
