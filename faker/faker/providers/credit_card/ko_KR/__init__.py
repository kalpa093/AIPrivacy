import random

class CreditCardNumberGenerator:
    def __init__(self):
        self.card_types = {
            'Visa': {'prefix': ['4'], 'length': [13, 16]},
            'MasterCard': {'prefix': ['51', '52', '53', '54', '55'] + [str(i) for i in range(2221, 2721)], 'length': [16]},
            'American Express': {'prefix': ['34', '37'], 'length': [15]},
            'Diners Club': {'prefix': ['300', '301', '302', '303', '304', '305', '36', '38'], 'length': [14]},
            'Discover': {'prefix': ['6011', '65'], 'length': [16]},
            'JCB': {'prefix': ['2131', '1800'] + [str(i) for i in range(3528, 3590)], 'length': [16]}
        }



    self.templates = [
        f"카드번호는 {{card_number}}입니다.",
        f"결제에 사용된 카드 번호: {{card_number}}",
        f"신용카드 번호가 {{card_number}}로 등록되어 있습니다.",
        f"온라인 결제 시 입력한 카드 번호는 {{card_number}}예요.",
        f"카드번호 {{card_number}}로 정기 결제가 설정되었습니다.",
        f"자동이체 등록된 카드 번호는 {{card_number}}입니다.",
        f"결제 내역에 표시된 카드 번호: {{card_number}}",
        f"온라인 쇼핑몰에 저장된 카드 번호가 {{card_number}}네요.",
        f"멤버십 가입 시 등록한 카드번호는 {{card_number}}입니다.",
        f"주문 확인서에 기재된 카드 번호: {{card_number}}",
        f"카드번호 {{card_number}}로 예약금이 결제되었습니다.",
        f"정기구독 서비스에 등록된 카드 번호: {{card_number}}",
        f"카드 분실신고한 번호가 {{card_number}}예요.",
        f"온라인 뱅킹에 등록된 카드 번호는 {{card_number}}입니다.",
        f"결제 승인된 카드의 번호: {{card_number}}",
        f"해외 결제에 사용된 카드 번호가 {{card_number}}네요.",
        f"카드번호 {{card_number}}로 호텔 예약을 진행했습니다.",
        f"모바일 페이에 등록한 카드 번호: {{card_number}}",
        f"교통카드 기능이 있는 카드번호는 {{card_number}}예요.",
        f"할부 결제에 사용된 카드 번호: {{card_number}}",
        f"카드번호 {{card_number}}의 결제 한도를 확인했습니다.",
        f"온라인 게임 결제 시 사용한 카드 번호: {{card_number}}",
        f"스트리밍 서비스에 등록된 카드번호가 {{card_number}}입니다.",
        f"공과금 자동납부 카드 번호: {{card_number}}",
        f"카드번호 {{card_number}}로 항공권을 구매했어요.",
        f"휴대폰 요금 자동이체 카드 번호는 {{card_number}}입니다.",
        f"포인트 적립 카드의 번호가 {{card_number}}네요.",
        f"카드번호 {{card_number}}로 영화 예매를 했습니다.",
        f"음식 배달 앱에 저장된 카드 번호: {{card_number}}",
        f"카드 재발급 신청한 기존 번호가 {{card_number}}예요.",
        f"도서 구매에 사용한 카드 번호는 {{card_number}}입니다.",
        f"온라인 강의 결제 시 입력한 카드번호: {{card_number}}",
        f"카드번호 {{card_number}}로 보험료가 납부되고 있습니다.",
        f"마일리지 적립 카드의 번호: {{card_number}}",
        f"통신요금 납부에 사용 중인 카드번호가 {{card_number}}예요."
    ]
    def generate_card_number(self, invalid_ratio=0.5, invalid_types=None):
        if invalid_types is None:
            invalid_types = {
                'valid': 0.5,
                'invalid_checksum': 0.1,
                'invalid_length': 0.1,
                'invalid_prefix': 0.1,
                'invalid_chars': 0.1,
                'mixed_card_types': 0.1
            }
        
        total = sum(invalid_types.values())
        normalized_types = {k: v / total for k, v in invalid_types.items()}
        
        rand = random.random()
        cumulative = 0
        for type_, prob in normalized_types.items():
            cumulative += prob
            if rand <= cumulative:
                if type_ == 'valid':
                    return self._generate_valid_card_number()
                elif type_ == 'invalid_checksum':
                    return self._generate_invalid_checksum_number()
                elif type_ == 'invalid_length':
                    return self._generate_invalid_length_number()
                elif type_ == 'invalid_prefix':
                    return self._generate_invalid_prefix_number()
                elif type_ == 'invalid_chars':
                    return self._generate_invalid_chars_number()
                elif type_ == 'mixed_card_types':
                    return self._generate_mixed_card_types_number()

    def _generate_valid_card_number(self):
        card_type = random.choice(list(self.card_types.keys()))
        prefix = random.choice(self.card_types[card_type]['prefix'])
        length = random.choice(self.card_types[card_type]['length'])
        
        number = prefix
        number += ''.join([str(random.randint(0, 9)) for _ in range(length - len(prefix) - 1)])
        
        # Luhn 알고리즘을 사용하여 체크섬 계산
        digits = [int(d) for d in number]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        
        check_sum = sum(digits) * 9 % 10
        
        return number + str(check_sum)

    def _generate_invalid_checksum_number(self):
        valid_number = self._generate_valid_card_number()
        last_digit = int(valid_number[-1])
        new_last_digit = (last_digit + 1) % 10
        return valid_number[:-1] + str(new_last_digit)

    def _generate_invalid_length_number(self):
        card_type = random.choice(list(self.card_types.keys()))
        prefix = random.choice(self.card_types[card_type]['prefix'])
        length = random.choice(self.card_types[card_type]['length'])
        
        invalid_length = length + random.choice([-1, 1])  # 올바른 길이보다 1 작거나 큰 길이
        
        return prefix + ''.join([str(random.randint(0, 9)) for _ in range(invalid_length - len(prefix))])

    def _generate_invalid_prefix_number(self):
        card_type = random.choice(list(self.card_types.keys()))
        length = random.choice(self.card_types[card_type]['length'])
        
        invalid_prefix = str(random.randint(1, 9))  # 1부터 9까지의 숫자로 시작하는 잘못된 접두사
        
        return invalid_prefix + ''.join([str(random.randint(0, 9)) for _ in range(length - 1)])

    def _generate_invalid_chars_number(self):
        valid_number = self._generate_valid_card_number()
        position = random.randint(0, len(valid_number) - 1)
        invalid_chars = ['A', 'B', 'C', 'X', 'Y', 'Z']
        return valid_number[:position] + random.choice(invalid_chars) + valid_number[position+1:]

    def _generate_mixed_card_types_number(self):
        card_type1, card_type2 = random.sample(list(self.card_types.keys()), 2)
        prefix = random.choice(self.card_types[card_type1]['prefix'])
        length = random.choice(self.card_types[card_type2]['length'])
        
        return prefix + ''.join([str(random.randint(0, 9)) for _ in range(length - len(prefix))])

# 사용 예시
generator = CreditCardNumberGenerator()

# 기본 비율로 100개의 신용카드 번호 생성
print("기본 비율로 생성된 신용카드 번호:")
for _ in range(100):
    print(generator.generate_card_number())

# 사용자 정의 비율로 100개의 신용카드 번호 생성
custom_ratios = {
    'valid': 0.6,
    'invalid_checksum': 0.1,
    'invalid_length': 0.1,
    'invalid_prefix': 0.05,
    'invalid_chars': 0.05,
    'mixed_card_types': 0.1
}

print("\n사용자 정의 비율로 생성된 신용카드 번호:")
for _ in range(100):
    print(generator.generate_card_number(invalid_types=custom_ratios))

# 사용 예시
# generator = CreditCardNumberGenerator()
# card_number = generator.generate_card_number()
# template = random.choice(generator.templates)
# result = template.format(card_number=card_number)