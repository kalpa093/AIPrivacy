from .. import Provider as PhoneNumberProvider
from numpy.random import choice
import random

class Provider(PhoneNumberProvider):
    mobile_prefixes = ['010', '011', '016', '017', '018', '019']
    landline_prefixes = {
        '02': '서울',
        '031': '경기',
        '032': '인천',
        '033': '강원',
        '041': '충남',
        '042': '대전',
        '043': '충북',
        '044': '세종',
        '051': '부산',
        '052': '울산',
        '053': '대구',
        '054': '경북',
        '055': '경남',
        '061': '전남',
        '062': '광주',
        '063': '전북',
        '064': '제주'
    }

    def phone_number(self, invalid_ratio=0.5, invalid_types=None):
        if invalid_types is None:
            invalid_types = {
                'valid': 0.5,
                'invalid_prefix': 0.1,
                'invalid_length': 0.1,
                'invalid_format': 0.1,
                'invalid_chars': 0.1,
                'landline_as_mobile': 0.05,
                'mobile_as_landline': 0.05
            }
        
        total = sum(invalid_types.values())
        normalized_types = {k: v / total for k, v in invalid_types.items()}
        
        rand = random.random()
        cumulative = 0
        for type_, prob in normalized_types.items():
            cumulative += prob
            if rand <= cumulative:
                if type_ == 'valid':
                    return self._generate_valid_number()
                elif type_ == 'invalid_prefix':
                    return self._generate_invalid_prefix_number()
                elif type_ == 'invalid_length':
                    return self._generate_invalid_length_number()
                elif type_ == 'invalid_format':
                    return self._generate_invalid_format_number()
                elif type_ == 'invalid_chars':
                    return self._generate_invalid_chars_number()
                elif type_ == 'landline_as_mobile':
                    return self._generate_landline_as_mobile()
                elif type_ == 'mobile_as_landline':
                    return self._generate_mobile_as_landline()

    def _generate_valid_number(self):
        if random.choice([True, False]):  # 50% 확률로 휴대폰 또는 유선전화 번호 생성
            prefix = random.choice(self.mobile_prefixes)
            middle = f"{random.randint(0, 9999):04d}"
            last = f"{random.randint(0, 9999):04d}"
            return f"{prefix}-{middle}-{last}"
        else:
            prefix = random.choice(list(self.landline_prefixes.keys()))
            if prefix == '02':
                middle = f"{random.randint(0, 9999):04d}"
            else:
                middle = f"{random.randint(0, 999):03d}"
            last = f"{random.randint(0, 9999):04d}"
            return f"{prefix}-{middle}-{last}"

    def _generate_invalid_prefix_number(self):
        invalid_prefix = f"0{random.randint(20, 99)}"
        middle = f"{random.randint(0, 9999):04d}"
        last = f"{random.randint(0, 9999):04d}"
        return f"{invalid_prefix}-{middle}-{last}"

    def _generate_invalid_length_number(self):
        prefix = random.choice(self.mobile_prefixes + list(self.landline_prefixes.keys()))
        middle = f"{random.randint(0, 99999):05d}"  # 5자리
        last = f"{random.randint(0, 999):03d}"  # 3자리
        return f"{prefix}-{middle}-{last}"

    def _generate_invalid_format_number(self):
        number = self._generate_valid_number()
        return number.replace('-', '')  # 하이픈 제거

    def _generate_invalid_chars_number(self):
        number = self._generate_valid_number()
        invalid_chars = ['A', 'B', 'C', 'X', 'Y', 'Z']
        position = random.randint(0, len(number) - 1)
        return number[:position] + random.choice(invalid_chars) + number[position+1:]

    def _generate_landline_as_mobile(self):
        prefix = random.choice(list(self.landline_prefixes.keys()))
        middle = f"{random.randint(0, 9999):04d}"
        last = f"{random.randint(0, 9999):04d}"
        return f"010-{middle}-{last}"  # 유선전화 번호를 010으로 시작하게 함

    def _generate_mobile_as_landline(self):
        prefix = random.choice(self.mobile_prefixes)
        middle = f"{random.randint(0, 999):03d}"
        last = f"{random.randint(0, 9999):04d}"
        return f"02-{middle}-{last}"  # 휴대폰 번호를 02로 시작하게 함