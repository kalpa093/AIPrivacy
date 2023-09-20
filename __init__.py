import string

from .. import Provider as AddressProvider

ALPHABET = string.ascii_uppercase


class Provider(AddressProvider):
    """
    Korean Address Provider
    =======================

    Korea has two address and postal code system.

    Address:
        - Address based on land parcel numbers
          (지번 주소, OLD, but someone use consistently)
        - Address based on road names and building numbers (도로명 주소, NEW)

    :meth:`land_address` generate Address based on land parcel numbers and
    :meth:`road_address` generate Address based on road names and building
    numbers.

    Postal code:
        - Old postal code (6-digit, OLD and dead)
        - New postal code (5-digit, New)

    :meth:`old_postal_code` and :meth:`postcode` generate old 6-digit code
    and :meth:`postal_code` generate newer 5-digit code.

    Reference:
        - `Official Confirmation Prividing that Old and New Addresses are Identical`__
          (warn: cert error)

    __ https://www.juso.go.kr/addridentity/AddrIdentityHelp.htm

    """

    building_suffixes = (
        "빌라",
        "아파트",
        "연립",
        "마을",
        "타운",
        "타워",
    )
    road_suffixes = ("로", "길", "거리", "가")
    town_suffixes = ("동", "읍", "면", "리", "마을")
    postcode_formats = ("###-###",)
    new_postal_code_formats = ("#####",)
    metropolitan_cities = (
        "서울특별시",
        "부산광역시",
        "대구광역시",
        "인천광역시",
        "광주광역시",
        "대전광역시",
        "울산광역시",
        "세종특별자치시",
    )
    provinces = (
        "경기도",
        "강원도",
        "충청북도",
        "충청남도",
        "전라북도",
        "전라남도",
        "경상북도",
        "경상남도",
        "제주특별자치도",
    )
    metropolitan_cities_boroughs = {
        '서울특별시': ['중랑구', '구로구', '동작구', '관악구', '중구', '송파구', '종로구', '성북구', '강서구', '양천구', '마포구', '광진구', '강동구', '강남구', '동대문구', '강북구', '서대문구', '노원구', '서초구', '성동구', '용산구', '금천구', '은평구', '영등포구', '도봉구'],
        '부산광역시': ['영도구', '강서구', '연제구', '금정구', '부산진구', '사하구', '수영구', '사상구', '기장군', '동구', '남구', '중구', '해운대구', '서구', '동래구', '북구'],
        '대구광역시': ['달서구', '남구', '달성군', '동구', '수성구', '북구', '중구', '서구'],
        '인천광역시': ['옹진군', '강화군', '계양구', '미추홀구', '동구', '부평구', '중구', '서구', '남동구', '연수구'],
        '광주광역시': ['남구', '동구', '북구', '서구', '광산구'],
        '대전광역시': ['유성구', '대덕구', '동구', '중구', '서구'],
        '울산광역시': ['남구', '동구', '울주군', '중구', '북구'],
        '세종특별자치시': ['아름동', '전동면', '어진동', '합강동', '장군면', '전의면', '보람동', '종촌동', '연기면', '금남면', '연서면', '소정면', '고운동', '누리동', '연동면', '조치원읍', '세종동', '용호동', '다솜동', '집현동', '새롬동', '부강면', '반곡동', '해밀동', '소담동', '가람동', '도담동', '한별동', '나성동', '다정동', '대평동', '한솔동', '산울동'],

    }

    province_to_cities = {
        '경기도': ['연천군', '안양시 만안구', '수원시 권선구', '수원시 장안구', '시흥시', '의왕시', '양주시', '성남시 수정구', '안성시', '이천시', '용인시 기흥구', '안산시 상록구', '광주시', '가평군', '군포시', '용인시 처인구', '수원시 팔달구', '성남시 중원구', '고양시 덕양구', '고양시 일산서구', '화성시', '수원시 영통구', '파주시', '안양시 동안구', '여주시', '의정부시', '용인시 수지구', '포천시', '부천시', '광명시', '구리시', '하남시', '과천시', '양평군', '성남시 분당구', '안산시 단원구', '오산시', '고양시 일산동구', '남양주시', '평택시', '김포시', '동두천시'],
        '강원도': ['동해시', '정선군', '양양군', '속초시', '홍천군', '횡성군', '영월군', '인제군', '고성군', '화천군', '춘천시', '삼척시', '원주시', '철원군', '태백시', '양구군', '강릉시', '평창군'],
        '충청북도': ['청주시 흥덕구', '단양군', '진천군', '음성군', '청주시 서원구', '청주시 청원구', '옥천군', '영동군', '충주시', '제천시', '보은군', '증평군', '청주시 상당구', '괴산군'],
        '충청남도': ['예산군', '천안시 서북구', '서천군', '홍성군', '공주시', '계룡시', '논산시', '금산군', '부여군', '태안군', '서산시', '천안시 동남구', '보령시', '당진시', '아산시', '청양군'],
        '전라북도': ['전주시 덕진구', '익산시', '순창군', '고창군', '전주시 완산구', '완주군', '군산시', '무주군', '남원시', '부안군', '임실군', '장수군', '정읍시', '진안군', '김제시'],
        '전라남도': ['목포시', '여수시', '순천시', '함평군', '장성군', '무안군', '진도군', '강진군', '보성군', '완도군', '나주시', '고흥군', '곡성군', '구례군', '해남군', '신안군', '영암군', '광양시', '담양군', '화순군', '영광군', '장흥군'],
        '경상북도': ['청송군', '경주시', '고령군', '칠곡군', '예천군', '영천시', '상주시', '봉화군', '구미시', '영양군', '경산시', '울릉군', '울진군', '안동시', '청도군', '군위군', '영주시', '문경시', '김천시', '의성군', '영덕군', '포항시 남구', '포항시 북구', '성주군'],
        '경상남도': ['의령군', '남해군', '창원시 진해구', '창원시 의창구', '창원시 마산합포구', '김해시', '진주시', '밀양시', '산청군', '창원시 성산구', '창녕군', '함양군', '하동군', '양산시', '거창군', '고성군', '창원시 마산회원구', '합천군', '함안군', '통영시', '거제시', '사천시'],
        '제주특별자치도': ['제주시', '서귀포시'],
    }

    cities = (
        "파주시",
        "수원시",
        "수원시 권선구",
        "수원시 팔달구",
        "수원시 영통구",
        "성남시",
        "성남시 수정구",
        "성남시 중원구",
        "화성시",
        "성남시 분당구",
        "안양시",
        "안양시 만안구",
        "안양시 동안구",
        "부천시",
        "부천시 원미구",
        "부천시 소사구",
        "부천시 오정구",
        "광명시",
        "평택시",
        "이천시",
        "동두천시",
        "안산시",
        "안산시 상록구",
        "안산시 단원구",
        "안성시",
        "고양시",
        "고양시 덕양구",
        "고양시 일산동구",
        "고양시 일산서구",
        "과천시",
        "구리시",
        "남양주시",
        "오산시",
        "시흥시",
        "군포시",
        "의왕시",
        "하남시",
        "김포시",
        "용인시",
        "용인시 처인구",
        "용인시 기흥구",
        "용인시 수지구",
        "연천군",
        "가평군",
        "양평군",
        "광주시",
        "포천시",
        "양주시",
        "수원시 장안구",
        "의정부시",
        "여주시",
        "춘천시",
        "원주시",
        "강릉시",
        "동해시",
        "태백시",
        "속초시",
        "삼척시",
        "홍천군",
        "횡성군",
        "영월군",
        "평창군",
        "정선군",
        "철원군",
        "화천군",
        "양구군",
        "인제군",
        "고성군",
        "양양군",
        "천안시 동남구",
        "천안시 서북구",
        "공주시",
        "보령시",
        "아산시",
        "서산시",
        "논산시",
        "계룡시",
        "당진시",
        "금산군",
        "부여군",
        "서천군",
        "청양군",
        "홍성군",
        "예산군",
        "태안군",
        "청주시 상당구",
        "청주시 서원구",
        "청주시 흥덕구",
        "청주시 청원구",
        "충주시",
        "제천시",
        "보은군",
        "옥천군",
        "영동군",
        "증평군",
        "진천군",
        "괴산군",
        "음성군",
        "단양군",
    )
    road_names = (
        "압구정",
        "도산대",
        "학동",
        "봉은사",
        "테헤란",
        "역삼",
        "논현",
        "언주",
        "강남대",
        "양재천",
        "삼성",
        "영동대",
        "개포",
        "선릉",
        "반포대",
        "서초중앙",
        "서초대",
        "잠실",
        "석촌호수",
        "백제고분",
        "가락",
        "오금",
    )
    boroughs = (
        "종로구",
        "중구",
        "용산구",
        "성동구",
        "광진구",
        "동대문구",
        "중랑구",
        "성북구",
        "강북구",
        "도봉구",
        "노원구",
        "은평구",
        "서대문구",
        "마포구",
        "양천구",
        "강서구",
        "구로구",
        "금천구",
        "영등포구",
        "동작구",
        "관악구",
        "서초구",
        "강남구",
        "송파구",
        "강동구",
        "동구",
        "서구",
        "남구",
        "북구",
    )
    countries = (
        "대한민국"
    )
    building_dongs = (
        "가",
        "나",
        "다",
        "라",
        "마",
        "바",
        "##",
        "###",
    ) + tuple(ALPHABET)
    land_numbers = (
        "###",
        "###-#",
        "###-##",
    )
    road_numbers = (
        "#",
        "##",
        "###",
    )

    town_formats = (
        "{{first_name}}{{last_name}}{{town_suffix}}",
        "{{first_name}}{{last_name}}{{last_name}}{{town_suffix}}",
    )
    building_name_formats = (
        "{{first_name}}{{last_name}}{{building_suffix}}",
        "{{first_name}}{{last_name}}{{last_name}}{{building_suffix}}",
    )
    address_detail_formats = (
        "{{building_name}}",
        "{{building_name}} ###호",
        "{{building_name}} {{building_dong}}동 ###호",
    )
    road_formats = (
        "{{road_name}}{{road_suffix}}",
        "{{road_name}}{{road_number}}{{road_suffix}}",
    )
    road_address_formats = (
        "{{metropolitan_city}} {{borough}} {{road}}",
        "{{province}} {{city}} {{road}}",
        "{{metropolitan_city}} {{borough}} {{road}} ({{town}})",
        "{{province}} {{city}} {{road}} ({{town}})",
    )
    land_address_formats = (
        "{{metropolitan_city}} {{borough}} {{town}} {{land_number}}",
        "{{province}} {{city}} {{town}} {{land_number}}",
    )

    # Keep backward compatibility
    city_suffixes = ("시",)
    street_suffixes = road_suffixes
    street_name_formats = ("{{road_name}}",)
    street_address_formats = road_address_formats
    address_formats = road_address_formats

    def land_number(self) -> str:
        """
        :example: 507
        """
        return self.bothify(self.random_element(self.land_numbers))

    def land_address(self) -> str:
        """
        :example: 세종특별자치시 어진동 507
        """
        pattern: str = self.random_element(self.land_address_formats)
        # 수정된 부분: metropolitan_city, borough, province 선택
        metropolitan_city = self.random_element(self.metropolitan_cities)
        borough = self.random_element(self.metropolitan_cities_boroughs[metropolitan_city])
        province = self.random_element(list(self.province_to_cities.keys()))

        # 선택된 province에 해당하는 city 선택
        city = self.random_element(self.province_to_cities[province])

        return self.generator.parse(pattern).format(
            metropolitan_city=metropolitan_city,
            borough=borough,
            town=self.town(),
            land_number=self.land_number(),
            province=province,
            city=city,
        )

    def road_number(self) -> str:
        """
        :example: 24
        """
        return self.bothify(self.random_element(self.road_numbers))

    def road_address(self) -> str:
        """
        :example: 세종특별자치시 도움5로 19 (어진동)
        """
        pattern: str = self.random_element(self.road_address_formats)
        return self.generator.parse(pattern)

    def address_detail(self) -> str:
        """
        :example: 가나아파트 가동 102호
        """
        pattern: str = self.bothify(self.random_element(self.address_detail_formats))
        return self.generator.parse(pattern)

    def road(self) -> str:
        """
        :example: 도움5로
        """
        pattern: str = self.random_element(self.road_formats)
        return self.generator.parse(pattern)

    def road_name(self) -> str:
        """
        :example: 압구정
        """
        return self.random_element(self.road_names)

    def road_suffix(self) -> str:
        """
        :example: 길
        """
        return self.random_element(self.road_suffixes)

    def metropolitan_city(self) -> str:
        """
        :example: 서울특별시
        """
        return self.random_element(self.metropolitan_cities)

    def administrative_unit(self) -> str:
        """
        :example: 경기도
        """
        return self.random_element(self.provinces)

    province = administrative_unit

    def city(self) -> str:
        """
        :example: 고양시
        """
        pattern: str = self.random_element(self.cities)
        return self.generator.parse(pattern)

    def borough(self) -> str:
        """
        :example: 중구
        """
        return self.random_element(self.boroughs)

    def town(self) -> str:
        """
        :example: 가나동
        """
        pattern: str = self.random_element(self.town_formats)
        return self.generator.parse(pattern)

    def town_suffix(self) -> str:
        """
        :example: 동
        """
        return self.random_element(self.town_suffixes)

    def building_name(self) -> str:
        """
        :example: 김구아파트
        """
        pattern: str = self.random_element(self.building_name_formats)
        return self.generator.parse(pattern)

    def building_suffix(self) -> str:
        """
        :example: 아파트
        """
        return self.random_element(self.building_suffixes)

    def building_dong(self) -> str:
        """
        :example: 가
        """
        return self.bothify(self.random_element(self.building_dongs))

    def old_postal_code(self) -> str:
        """
        :example: 123-456
        """
        return self.bothify(self.random_element(self.postcode_formats))

    def postcode(self) -> str:
        """
        :example: 12345
        """
        return self.bothify(self.random_element(self.new_postal_code_formats))

    def postal_code(self) -> str:
        """
        :example: 12345
        """
        return self.postcode()
