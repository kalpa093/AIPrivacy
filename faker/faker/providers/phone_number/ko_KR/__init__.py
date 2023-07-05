from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "02-####-####", # 서울
        "031-###-####", # 경기
        "032-###-####", # 인천
        "033-###-####", # 강원
        "041-###-####", # 충남
        "042-###-####", # 대전
        "043-###-####", # 충북
        "044-###-####", # 세종
        "051-###-####", # 부산
        "052-###-####", # 울산
        "053-###-####", # 대구
        "054-###-####", # 경북
        "055-###-####", # 경남
        "061-###-####", # 전남
        "062-###-####", # 광주
        "063-###-####", # 전북
        "064-7##-####", # 제주
        "010-####-####", # 휴대폰
        "011-###-####",  # 휴대폰
        "016-###-####", # 휴대폰
        "017-###-####", # 휴대폰
        "018-###-####", # 휴대폰
        "019-###-####", # 휴대폰
        "070-####-####", # 인터넷 전화
    )

