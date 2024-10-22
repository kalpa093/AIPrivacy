import random
import string
import json

class KoreanPassportNumberGenerator:
    def __init__(self):
        self.prefix_types = ['M', 'R']
        self.second_char = string.digits + string.ascii_uppercase

    def generate_passport_number(self, invalid_ratio=0.3):
        if random.random() < invalid_ratio:
            return self._generate_invalid_passport_number(), 'SIMILAR'
        else:
            return self._generate_valid_passport_number(), 'PASSPORT'

    def _generate_valid_passport_number(self):
        prefix = random.choice(self.prefix_types)
        second_char = random.choice(self.second_char)
        base_number = ''.join(random.choices(string.digits, k=6))
        full_number = prefix + second_char + base_number
        checksum = self._calculate_checksum(full_number)
        return full_number + str(checksum)

    def _generate_invalid_passport_number(self):
        valid_number = self._generate_valid_passport_number()
        modification_type = random.choice(['prefix', 'second_char', 'length', 'checksum', 'chars'])
        
        if modification_type == 'prefix':
            return random.choice(string.ascii_uppercase.replace('M', '').replace('R', '')) + valid_number[1:]
        elif modification_type == 'second_char':
            return valid_number[0] + random.choice(string.ascii_lowercase) + valid_number[2:]
        elif modification_type == 'length':
            return valid_number[:-1] if random.choice([True, False]) else valid_number + random.choice(string.digits)
        elif modification_type == 'checksum':
            return valid_number[:-1] + str((int(valid_number[-1]) + 1) % 10)
        else:  # chars
            position = random.randint(2, len(valid_number) - 1)
            return valid_number[:position] + random.choice(string.ascii_lowercase) + valid_number[position+1:]

    def _calculate_checksum(self, number):
        weights = [7, 3, 1, 7, 3, 1, 7, 3, 1]
        total = sum((ord(char) - 55 if i == 0 else int(char) if char.isdigit() else ord(char) - 55) * weights[i] for i, char in enumerate(number))
        return (10 - (total % 10)) % 10

def generate_sentence_with_passport(generator):
    number, category = generator.generate_passport_number()
    
    templates = [
f"여권번호는 {number}입니다.",
        f"제 여권번호는 {number}예요.",
        f"여권에 적힌 번호는 {number}이에요.",
        f"내 여권 번호: {number}",
        f"여권 정보: 번호 {number}",
        f"제 새 여권 번호는 {number}로 발급되었습니다.",
        f"해외여행 준비 중인데, 여권번호가 {number}네요.",
        f"이번에 갱신한 여권의 번호는 {number}입니다.",
        f"비자 신청할 때 필요한 여권번호는 {number}에요.",
        f"공항에서 확인한 제 여권번호는 {number}였어요.",
        f"여행사에 제출한 여권 정보에는 {number}라고 적혀있어요.",
        f"호텔 예약할 때 사용한 여권번호: {number}",
        f"출입국 신고서에 {number}라고 여권번호를 기입했습니다.",
        f"온라인 체크인 시 입력한 여권번호는 {number}예요.",
        f"긴급 연락처에 기재할 여권번호로 {number}를 썼어요.",
        f"여권 분실신고를 위해 기억해둔 번호: {number}",
        f"보험 가입 시 필요한 여권번호가 {number}네요.",
        f"국제운전면허증 신청할 때 쓴 여권번호는 {number}였어요.",
        f"해외 계좌 개설 시 제출한 여권번호: {number}",
        f"워킹홀리데이 비자 신청서에 {number}로 여권정보를 기재했습니다.",
        f"여권 복사본을 보니 번호가 {number}로 되어 있네요.",
        f"친구에게 여권번호 {number}를 알려줬어요.",
        f"영사관에 제출한 서류에 여권번호 {number}를 기입했습니다.",
        f"해외 배송을 위해 입력한 여권번호는 {number}입니다.",
        f"여행 예약 확인 이메일에 {number}라고 여권번호가 표시되어 있어요.",
        f"대사관에서 비자 발급받을 때 확인한 여권번호: {number}",
        f"항공권 구매 시 입력한 여권정보 중 번호는 {number}였습니다.",
        f"여행 동행인에게 여권번호 {number}를 공유했어요.",
        f"여권 갱신 신청서에 이전 여권번호로 {number}를 적었습니다.",
        f"해외 체류 신고 시 필요한 여권번호가 {number}네요.",
        f"유학 서류에 기재한 여권번호는 {number}입니다.",
        f"여권 번호 {number}로 온라인 비자 신청을 완료했어요.",
        f"출국 심사대에서 확인한 제 여권번호는 {number}였습니다.",
        f"여행자보험 가입 시 입력한 여권번호: {number}",
        f"비즈니스 미팅 참석을 위해 제출한 여권번호는 {number}에요.",
        f"국제 컨퍼런스 등록 시 사용한 여권번호가 {number}네요.",
        f"해외 부동산 구매 계약서에 기재된 여권번호: {number}",
        f"국제 결혼 신고 시 제출한 여권번호는 {number}입니다.",
        f"외국인 등록증 발급을 위해 제시한 여권번호: {number}",
        f"국제 운송 서비스 이용 시 기입한 여권번호는 {number}예요.",
        f"해외 은행 송금을 위해 확인한 여권번호가 {number}였어요.",
        f"국제 면허증 발급 신청서에 {number}로 여권번호를 적었습니다.",
        f"여권번호 {number}로 글로벌 인증 시험에 등록했어요.",
        f"해외 의료 서비스 이용 시 제시한 여권번호: {number}",
        f"국제 공모전 참가 신청서에 기재한 여권번호는 {number}입니다.",
        f"외국 기업 인턴십 지원 시 입력한 여권번호가 {number}네요.",
        f"국제 학회 참가를 위해 제출한 여권 정보 중 번호는 {number}예요.",
        f"해외 박람회 입장권 예매 시 사용한 여권번호: {number}",
        f"국제 자원봉사 프로그램 지원서에 기재한 여권번호는 {number}입니다.",
        f"외국어 능력 시험 응시 시 입력한 여권번호가 {number}였어요.",
        f"국제 특허 출원 서류에 기재된 여권번호: {number}",
        f"해외 공연 티켓 예매를 위해 입력한 여권번호는 {number}네요.",
        f"국제 학술지 논문 투고 시 기재한 여권번호: {number}",
        f"외국계 회사 입사 지원서에 적은 여권번호가 {number}입니다.",
        f"국제 영화제 참가 등록 시 사용한 여권번호: {number}",
        f"해외 온라인 쇼핑몰 가입 시 인증에 사용한 여권번호가 {number}예요.",
        f"국제 스포츠 대회 참가 신청서에 기재한 여권번호: {number}",
        f"외국 대학 교환학생 프로그램 지원 시 입력한 여권번호가 {number}네요.",
        f"국제 전시회 참가자 등록 시 제출한 여권번호는 {number}입니다.",
        f"해외 부동산 임대 계약서에 기재된 여권번호: {number}",
        f"국제 기구 인턴십 지원 시 기입한 여권번호가 {number}였어요.",
        f"외국어 학원 해외 연수 프로그램 신청서에 적은 여권번호: {number}",
        f"국제 공항 라운지 이용을 위해 제시한 여권번호가 {number}네요.",
        f"해외 통신사 심카드 구매 시 등록한 여권번호: {number}",
        f"국제 면접을 위해 화상 회의 시스템에 입력한 여권번호가 {number}입니다.",
        f"외국 정부 장학금 신청서에 기재한 여권번호: {number}",
        f"국제 봉사 단체 가입 시 제출한 여권 정보 중 번호는 {number}예요.",
        f"해외 법인 설립 서류에 기재된 대표자의 여권번호: {number}",
        f"국제 미술 전시회 작품 출품 시 기재한 여권번호가 {number}네요.",
        f"외국어 능력 인증서 발급을 위해 입력한 여권번호: {number}",
        f"국제 요리 대회 참가 신청서에 기재한 여권번호는 {number}입니다.",
        f"해외 호텔 멤버십 가입 시 등록한 여권번호가 {number}였어요.",
        f"국제 패션쇼 모델 지원서에 기재한 여권번호: {number}",
        f"외국 병원 진료 예약을 위해 제시한 여권번호가 {number}네요.",
        f"국제 음악 콩쿠르 참가 등록 시 입력한 여권번호: {number}",
        f"해외 출판사와의 계약서에 기재된 저자의 여권번호: {number}",
        f"국제 디자인 공모전 참가 신청서에 적은 여권번호가 {number}입니다.",
        f"외국 투자 상담을 위해 제출한 여권번호: {number}",
        f"국제 IT 컨퍼런스 참가자 등록 시 입력한 여권번호가 {number}예요.",
        f"해외 부동산 투자 세미나 참석을 위해 기재한 여권번호: {number}",
        f"국제 환경 포럼 패널 등록 시 제출한 여권번호는 {number}네요.",
        f"외국 보험사에 제출한 여행자 보험 서류의 여권번호: {number}",
        f"국제 마라톤 대회 참가 신청서에 기재한 여권번호가 {number}입니다.",
        f"해외 미디어 인터뷰를 위해 제공한 여권번호: {number}",
        f"국제 과학 심포지엄 발표자 등록 시 입력한 여권번호가 {number}였어요.",
        f"외국 대학원 입학 지원서에 기재한 여권번호: {number}",
        f"국제 요가 대회 참가 등록 시 제출한 여권번호가 {number}네요.",
        f"해외 임시 거주지 등록을 위해 제시한 여권번호: {number}",
        f"국제 와인 시음회 참석을 위해 예약 시 기재한 여권번호는 {number}입니다.",
        f"외국 기업과의 계약서에 명시된 대표자의 여권번호: {number}"
    ]
    
    sentence = random.choice(templates)
    
    words = sentence.split()
    labels = []
    for word in words:
        if number in word:
            labels.append({"word": word, "label": f"B-{category}"})
        else:
            labels.append({"word": word, "label": "O"})
    
    return {"sentence": sentence, "labels": labels}

# JSON 생성
generator = KoreanPassportNumberGenerator()
data = [[generate_sentence_with_passport(generator) for _ in range(5)] for _ in range(200)]  # 200 배치, 각 배치당 5개 문장

# JSON 파일로 저장
with open('passport_sentences.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("1000개의 여권번호를 포함한 문장이 생성되어 passport_sentences.json 파일에 저장되었습니다.")
    
