import random

class KoreanTrackingNumberGenerator:
    def __init__(self):
        self.carriers = {
            'CJ': {'length': 10, 'prefix': ['1', '2', '3']},
            'Lotte': {'length': 12, 'prefix': ['4', '5']},
            'Post Office': {'length': 13, 'prefix': ['6', '7']}
        }

    self.templates = [
    f"운송장번호는 {tracking_number}입니다.",
    f"배송 조회 번호: {tracking_number}",
    f"택배 송장 번호가 {tracking_number}로 발급되었습니다.",
    f"주문하신 상품의 운송장번호는 {tracking_number}예요.",
    f"배송 추적 번호 {tracking_number}가 등록되었습니다.",
    f"상품 발송 완료! 운송장번호: {tracking_number}",
    f"주문하신 물품의 송장번호는 {tracking_number}입니다.",
    f"배송조회는 {tracking_number}로 가능합니다.",
    f"택배사에 등록된 운송장번호: {tracking_number}",
    f"주문번호에 할당된 송장번호가 {tracking_number}예요.",
    f"물품 배송 시작! 운송장번호는 {tracking_number}입니다.",
    f"반품 접수된 운송장번호: {tracking_number}",
    f"교환 신청하신 상품의 송장번호는 {tracking_number}예요.",
    f"택배기사님께 전달된 운송장번호: {tracking_number}",
    f"발송 처리된 주문의 운송장번호가 {tracking_number}입니다.",
    f"배송 추적을 위한 송장번호: {tracking_number}",
    f"출고 완료! 운송장번호는 {tracking_number}예요.",
    f"주문하신 상품은 {tracking_number}로 배송됩니다.",
    f"회수 요청하신 상품의 운송장번호: {tracking_number}",
    f"택배 발송된 상품의 송장번호가 {tracking_number}입니다.",
    f"주문 완료! 운송장번호는 {tracking_number}예요.",
    f"배송 접수된 상품의 송장번호: {tracking_number}",
    f"택배사에 전달된 운송장번호가 {tracking_number}입니다.",
    f"상품 출고 시 사용된 송장번호: {tracking_number}",
    f"물품 발송 접수 번호는 {tracking_number}예요.",
    f"택배 기사님께 배정된 운송장번호: {tracking_number}",
    f"온라인 주문 배송 번호: {tracking_number}",
    f"물류센터에서 발급된 송장번호가 {tracking_number}입니다.",
    f"배송 시스템에 등록된 운송장번호: {tracking_number}",
    f"고객님의 주문 운송장번호는 {tracking_number}예요.",
    f"자동 발급된 택배 송장 번호: {tracking_number}",
    f"판매자가 등록한 운송장번호가 {tracking_number}입니다.",
    f"묶음배송 주문의 운송장번호: {tracking_number}",
    f"합배송 처리된 송장번호는 {tracking_number}예요.",
    f"픽업 예정인 상품의 운송장번호: {tracking_number}",
    f"새벽배송 운송장번호가 {tracking_number}입니다.",
    f"당일배송 주문의 송장번호: {tracking_number}",
    f"신선식품 배송 운송장번호는 {tracking_number}예요.",
    f"택배 집하 완료! 운송장번호: {tracking_number}",
    f"배송 예약된 상품의 송장번호가 {tracking_number}입니다.",
    f"해외배송 운송장번호: {tracking_number}",
    f"국제택배 송장번호는 {tracking_number}예요.",
    f"특송 서비스 운송장번호가 {tracking_number}입니다.",
    f"퀵서비스 배송 번호: {tracking_number}",
    f"등기우편 운송장번호는 {tracking_number}예요.",
    f"안전배송 운송장번호: {tracking_number}",
    f"맞춤배송 주문의 송장번호가 {tracking_number}입니다.",
    f"배송 대행 서비스 운송장번호: {tracking_number}",
    f"택배 대리점 발급 송장번호는 {tracking_number}예요.",
    f"물류창고 출고 운송장번호: {tracking_number}",
    f"직배송 주문의 송장번호가 {tracking_number}입니다.",
    f"새벽배송 접수 운송장번호: {tracking_number}",
    f"프레시 배송 송장번호는 {tracking_number}예요.",
    f"설치배송 운송장번호가 {tracking_number}입니다.",
    f"대형가전 배송 송장번호: {tracking_number}",
    f"가구 배송 운송장번호는 {tracking_number}예요.",
    f"이사화물 운송장번호: {tracking_number}",
    f"귀중품 배송 송장번호가 {tracking_number}입니다.",
    f"보냉배송 운송장번호: {tracking_number}",
    f"냉동식품 배송 송장번호는 {tracking_number}예요.",
    f"냉장배송 운송장번호가 {tracking_number}입니다.",
    f"익일배송 송장번호: {tracking_number}",
    f"주말배송 운송장번호는 {tracking_number}예요.",
    f"심야배송 접수 번호: {tracking_number}",
    f"예약배송 운송장번호가 {tracking_number}입니다.",
    f"정기배송 송장번호: {tracking_number}",
    f"구독배송 운송장번호는 {tracking_number}예요.",
    f"프리미엄 배송 운송장번호: {tracking_number}",
    f"특급배송 송장번호가 {tracking_number}입니다.",
    f"우선배송 운송장번호: {tracking_number}",
    f"급송 서비스 송장번호는 {tracking_number}예요.",
    f"긴급배송 운송장번호가 {tracking_number}입니다.",
    f"안심배송 송장번호: {tracking_number}",
    f"안전포장 배송 운송장번호는 {tracking_number}예요.",
    f"친환경 포장 배송 번호: {tracking_number}",
    f"재포장 배송 운송장번호가 {tracking_number}입니다.",
    f"선물포장 배송 송장번호: {tracking_number}",
    f"신규 주문 운송장번호는 {tracking_number}예요.",
    f"추가 주문 배송 번호: {tracking_number}",
    f"변경 배송 운송장번호가 {tracking_number}입니다.",
    f"수정 배송 송장번호: {tracking_number}",
    f"일반 택배 운송장번호는 {tracking_number}예요.",
    f"대량 주문 배송 번호: {tracking_number}",
    f"B2B 배송 운송장번호가 {tracking_number}입니다.",
    f"기업 배송 송장번호: {tracking_number}",
    f"개인 배송 운송장번호는 {tracking_number}예요.",
    f"단체 주문 배송 번호: {tracking_number}",
    f"공동구매 운송장번호가 {tracking_number}입니다.",
    f"벌크 주문 송장번호: {tracking_number}",
    f"소량 주문 운송장번호는 {tracking_number}예요.",
    f"개별 포장 배송 번호: {tracking_number}",
    f"분할 배송 운송장번호가 {tracking_number}입니다.",
    f"부분 배송 송장번호: {tracking_number}",
    f"선입고 배송 운송장번호는 {tracking_number}예요.",
    f"후입고 배송 번호: {tracking_number}",
    f"사전 발송 운송장번호가 {tracking_number}입니다.",
    f"지연 배송 송장번호: {tracking_number}",
    f"예약 발송 운송장번호는 {tracking_number}예요.",
    f"정시 배송 번호: {tracking_number}",
    f"특별 배송 운송장번호가 {tracking_number}입니다.",
    f"임시 배송 송장번호: {tracking_number}",
    f"테스트 배송 운송장번호는 {tracking_number}예요.",
    f"샘플 배송 번호: {tracking_number}",
    f"체험판 배송 운송장번호가 {tracking_number}입니다.",
    f"무료 배송 송장번호: {tracking_number}",
    f"유료 배송 운송장번호는 {tracking_number}예요."
    ]
    def generate_tracking_number(self, invalid_ratio=0.5, invalid_types=None):
        if invalid_types is None:
            invalid_types = {
                'valid': 0.5,
                'invalid_length': 0.1,
                'invalid_prefix': 0.1,
                'invalid_format': 0.1,
                'invalid_chars': 0.1,
                'mixed_carrier': 0.1
            }
        
        total = sum(invalid_types.values())
        normalized_types = {k: v / total for k, v in invalid_types.items()}
        
        rand = random.random()
        cumulative = 0
        for type_, prob in normalized_types.items():
            cumulative += prob
            if rand <= cumulative:
                if type_ == 'valid':
                    return self._generate_valid_tracking_number()
                elif type_ == 'invalid_length':
                    return self._generate_invalid_length_number()
                elif type_ == 'invalid_prefix':
                    return self._generate_invalid_prefix_number()
                elif type_ == 'invalid_format':
                    return self._generate_invalid_format_number()
                elif type_ == 'invalid_chars':
                    return self._generate_invalid_chars_number()
                elif type_ == 'mixed_carrier':
                    return self._generate_mixed_carrier_number()

    def _generate_valid_tracking_number(self):
        carrier = random.choice(list(self.carriers.keys()))
        prefix = random.choice(self.carriers[carrier]['prefix'])
        length = self.carriers[carrier]['length']
        
        number = prefix + ''.join([str(random.randint(0, 9)) for _ in range(length - 1)])
        
        return number

    def _generate_invalid_length_number(self):
        carrier = random.choice(list(self.carriers.keys()))
        prefix = random.choice(self.carriers[carrier]['prefix'])
        length = self.carriers[carrier]['length'] + random.choice([-1, 1])  # 올바른 길이보다 1 작거나 큰 길이
        
        return prefix + ''.join([str(random.randint(0, 9)) for _ in range(length - 1)])

    def _generate_invalid_prefix_number(self):
        carrier = random.choice(list(self.carriers.keys()))
        length = self.carriers[carrier]['length']
        invalid_prefix = str(random.randint(8, 9))  # 존재하지 않는 접두사
        
        return invalid_prefix + ''.join([str(random.randint(0, 9)) for _ in range(length - 1)])

    def _generate_invalid_format_number(self):
        valid_number = self._generate_valid_tracking_number()
        return '-'.join([valid_number[i:i+4] for i in range(0, len(valid_number), 4)])  # 하이픈 추가

    def _generate_invalid_chars_number(self):
        valid_number = self._generate_valid_tracking_number()
        position = random.randint(0, len(valid_number) - 1)
        invalid_chars = ['A', 'B', 'C', 'X', 'Y', 'Z']
        return valid_number[:position] + random.choice(invalid_chars) + valid_number[position+1:]

    def _generate_mixed_carrier_number(self):
        carrier1, carrier2 = random.sample(list(self.carriers.keys()), 2)
        prefix = random.choice(self.carriers[carrier1]['prefix'])
        length = self.carriers[carrier2]['length']
        
        return prefix + ''.join([str(random.randint(0, 9)) for _ in range(length - 1)])

# 사용 예시
generator = KoreanTrackingNumberGenerator()

# 기본 비율로 100개의 운송장번호 생성
print("기본 비율로 생성된 운송장번호:")
for _ in range(100):
    print(generator.generate_tracking_number())

# 사용자 정의 비율로 100개의 운송장번호 생성
custom_ratios = {
    'valid': 0.6,
    'invalid_length': 0.1,
    'invalid_prefix': 0.1,
    'invalid_format': 0.05,
    'invalid_chars': 0.05,
    'mixed_carrier': 0.1
}

print("\n사용자 정의 비율로 생성된 운송장번호:")
for _ in range(100):
    print(generator.generate_tracking_number(invalid_types=custom_ratios))