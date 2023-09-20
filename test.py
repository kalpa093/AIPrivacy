import pandas as pd
from faker import Faker

fake = Faker('ko_KR')

def generate_fake_addresses(num=10000):
    addresses = [fake.address() for _ in range(num)]
    return addresses

def save_to_csv(data, filename='202301_kor_adr/fake_addresses.csv'):
    df = pd.DataFrame(data, columns=['Address'])
    df.to_csv(filename, index=False, encoding='cp949')

def load_real_addresses(directory='202301_kor_adr/', filename='merged_result.csv'):
    df = pd.read_csv(directory + filename, encoding='cp949')
    cities = set(df['city'].unique())
    boroughs = {city: set(df[df['city'] == city]['borough'].unique()) for city in cities}
    return cities, boroughs

def validate_fake_address(fake_address, cities, boroughs):
    parts = fake_address.split(' ')
    city = parts[0]
    borough = parts[1]

    if city not in cities:
        return False
    elif borough not in boroughs.get(city, set()):
        return False
    else:
        return True

if __name__ == "__main__":
    fake_addresses = generate_fake_addresses(10000)
    save_to_csv(fake_addresses)

    cities, boroughs = load_real_addresses()
    fake_addresses_df = pd.read_csv('202301_kor_adr/fake_addresses.csv',encoding='cp949')
    
    mismatches = fake_addresses_df['Address'].apply(lambda x: not validate_fake_address(x, cities, boroughs))
    mismatch_count = mismatches.sum()

    print(f"Number of mismatched addresses: {mismatch_count} out of {len(fake_addresses_df)}")
