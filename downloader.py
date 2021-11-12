from archive import get_years

def download():
    years = input("Which years do you want? Enter a Comma Separated List.\n")
    yr_list = years.split(",")
    print(yr_list)
    get_years(yr_list)

download()