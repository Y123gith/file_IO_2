# question 1
def print_file(file):
    with open(file,"r") as f:
        print(f.read())
    return

# question 2
def add_to_file(file,string):
    file1 = open(file, "w")
    file1.write(string)
    file1.close()
    return

# question 3
def switch_file(file_source,file_destination):
    file1 = open(file_source, "r")
    file1.read(file_source)
    file1.close()
    file2 = open(file_source, "w")
    file2.write(file_destination)
    file2.close()
    return

# question 4
def count_lines(file):
    counter = 0
    with open(file,"r") as f:
        lines = f.readlines()
        for line in lines:
            counter += 1
    return counter

# question 5  
def occurance_in_file(file,string):
    with open(file, "r") as f:
        document = f.read()
        occurance = document.count(string)
    return occurance

print(occurance_in_file("hello.txt","yes"))
