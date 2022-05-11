import csv
with open("airports.csv","r",encoding="utf-8") as file:
    line=file.readline()
    number_of_records=1
    count_small_airports=0
    while line:
        if 'small_airport' in line:
            print(f"small_airport at {count_small_airports} ")
            count_small_airports+=1
        line=file.readline()
        number_of_records+=1
    print("Total number of records",number_of_records)
    print("Total number of small_airports",count_small_airports)

