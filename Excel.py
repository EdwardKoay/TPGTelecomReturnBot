import pandas as pd

def main():

    excel_file = 'C:/Users/T6433677/Desktop/2021 09 8 Returns.xlsm'
    movies = pd.read_excel(excel_file)
    movies.head()

if __name__ == '__main__':
    main()

