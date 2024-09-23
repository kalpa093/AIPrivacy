from .. import Provider as SsnProvider
import random
from datetime import datetime, timedelta

class Provider(SsnProvider):
    def ssn(self, invalid_ratio=0.5, invalid_types=None):
        if invalid_types is None:
            invalid_types = {
                'valid': 0.5,
                'invalid_date': 0.1,
                'invalid_checksum': 0.1,
                'invalid_region_code': 0.1,
                'invalid_gender_year': 0.1,
                'future_date': 0.1
            }
        
        total = sum(invalid_types.values())
        normalized_types = {k: v / total for k, v in invalid_types.items()}
        
        rand = random.random()
        cumulative = 0
        for type_, prob in normalized_types.items():
            cumulative += prob
            if rand <= cumulative:
                if type_ == 'valid':
                    return self._generate_valid_rrn()
                elif type_ == 'invalid_date':
                    return self._generate_invalid_date_rrn()
                elif type_ == 'invalid_checksum':
                    return self._generate_invalid_checksum_rrn()
                elif type_ == 'invalid_region_code':
                    return self._generate_invalid_region_code_rrn()
                elif type_ == 'invalid_gender_year':
                    return self._generate_invalid_gender_year_rrn()
                elif type_ == 'future_date':
                    return self._generate_future_date_rrn()

    def _generate_valid_rrn(self):
        birth_date = self._generate_random_date()
        gender_digit = self._get_gender_digit(birth_date.year)
        region_code = random.randint(0, 95)
        serial = random.randint(0, 999)
        
        rrn = f"{birth_date.strftime('%y%m%d')}{gender_digit}{region_code:02d}{serial:03d}"
        checksum = self._calculate_checksum(rrn)
        
        return f"{rrn[:6]}-{rrn[6:]}{checksum}"

    def _generate_invalid_date_rrn(self):
        year = random.randint(0, 99)
        month = random.randint(1, 12)
        day = 31 if month in [4, 6, 9, 11] else (29 if month == 2 and year % 4 != 0 else random.randint(29, 31))
        
        gender_digit = self._get_gender_digit(2000 + year if year < 22 else 1900 + year)
        region_code = random.randint(0, 95)
        serial = random.randint(0, 999)
        
        rrn = f"{year:02d}{month:02d}{day:02d}{gender_digit}{region_code:02d}{serial:03d}"
        checksum = self._calculate_checksum(rrn)
        
        return f"{rrn[:6]}-{rrn[6:]}{checksum}"

    def _generate_invalid_checksum_rrn(self):
        valid_rrn = self._generate_valid_rrn().replace("-", "")
        invalid_checksum = (int(valid_rrn[-1]) + 1) % 10
        return f"{valid_rrn[:6]}-{valid_rrn[6:13]}{invalid_checksum}"

    def _generate_invalid_region_code_rrn(self):
        birth_date = self._generate_random_date()
        gender_digit = self._get_gender_digit(birth_date.year)
        region_code = random.randint(96, 99)  # Invalid region code
        serial = random.randint(0, 999)
        
        rrn = f"{birth_date.strftime('%y%m%d')}{gender_digit}{region_code:02d}{serial:03d}"
        checksum = self._calculate_checksum(rrn)
        
        return f"{rrn[:6]}-{rrn[6:]}{checksum}"

    def _generate_invalid_gender_year_rrn(self):
        birth_date = self._generate_random_date()
        year = birth_date.year
        if year < 2000:
            gender_digit = random.choice([3, 4, 7, 8])  # Invalid for pre-2000
        else:
            gender_digit = random.choice([1, 2, 5, 6])  # Invalid for post-2000
        
        region_code = random.randint(0, 95)
        serial = random.randint(0, 999)
        
        rrn = f"{birth_date.strftime('%y%m%d')}{gender_digit}{region_code:02d}{serial:03d}"
        checksum = self._calculate_checksum(rrn)
        
        return f"{rrn[:6]}-{rrn[6:]}{checksum}"

    def _generate_future_date_rrn(self):
        future_date = datetime.now() + timedelta(days=random.randint(1, 3650))  # Up to 10 years in the future
        gender_digit = self._get_gender_digit(future_date.year)
        region_code = random.randint(0, 95)
        serial = random.randint(0, 999)
        
        rrn = f"{future_date.strftime('%y%m%d')}{gender_digit}{region_code:02d}{serial:03d}"
        checksum = self._calculate_checksum(rrn)
        
        return f"{rrn[:6]}-{rrn[6:]}{checksum}"

    def _generate_random_date(self):
        start_date = datetime(1900, 1, 1)
        end_date = datetime.now()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        return start_date + timedelta(days=random_number_of_days)

    def _get_gender_digit(self, year):
        if 1800 <= year <= 1899:
            return random.choice([9, 0])
        elif 1900 <= year <= 1999:
            return random.choice([1, 2, 5, 6])
        else:  # 2000년대
            return random.choice([3, 4, 7, 8])

    def _calculate_checksum(self, rrn):
        multipliers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
        checksum = sum(int(rrn[i]) * multipliers[i] for i in range(12))
        return (11 - (checksum % 11)) % 10