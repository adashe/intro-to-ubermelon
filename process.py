log_file = open("um-server-01.txt")


def sales_reports(log_file):
    """
    Opens a file and prints the orders from Monday
    """
    for line in log_file:           # reviews each line in the log
        line = line.rstrip()        # strips whitespace to the right of the word
        day = line[0:3]             # slices the first three letters of the day of the week
        if day == "Mon":            # finds Tuesday lines     # changed to Monday
            print(line)             # prints Tuesday lines    # changed to Monday


sales_reports(log_file)             # calls the function on the file
