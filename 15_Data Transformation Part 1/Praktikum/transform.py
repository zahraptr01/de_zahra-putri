import pandas as pd

def extract_data():
    data = pd.read_csv('house_listings.csv')
    return data

if __name__ == '__main__':
    extract_data = extract_data()
    extract_data.to_excel('house_listings.xlsx')
    print(extract_data)