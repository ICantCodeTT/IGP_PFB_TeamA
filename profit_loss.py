from pathlib import Path
import csv
def profitloss_function():
    '''
    This functions runs everything related to "profitloss"
    which includes the return value.
    '''
# create a file to csv file
    fp = Path(r"C:\IGP_PFB_TeamA\csv_reports\profit-and-loss-usd (Day 48 to 52).csv")

# read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header


        profitloss = 0 # Creation of needed variables 
        row_counter = 0
        check = 0
        data_to_return = []
        
        for row in reader:
            row_counter += 1 
            if int(row[4]) > profitloss: # If int in row[4] is greater than profitloss, it equals to profitloss
                profitloss = int(row[4])
                check += 1 # check by counting if all the rows is greater than profitloss
            else:
                # Append all the days that are lower than the previous days
                data_to_return.append(f"[PROFIT DEFECIT] DAY: {row[0]}, AMOUNT: USD{profitloss - int(row[4])}")
                profitloss = int(row[4])
        # Only if check and row_counter have the exact final value, it will append "NET PROFIT SURPLUS" statement
        if check == row_counter: 
            data_to_return.append("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    return data_to_return


