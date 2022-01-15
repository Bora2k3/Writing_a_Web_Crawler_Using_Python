import csv

csv_file = "result.csv"
txt_file = "result.txt"
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
with open("result.txt", 'r') as f:
    myNames = [line.strip() for line in f]
    myNames.sort()
    myNames.remove('url')
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(myNames))
        f.close()
