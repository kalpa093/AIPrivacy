import random
import string

from .. import Provider as AddressProvider

class Provider(AddressProvider):
    administrative_divisions = {
        "부산광역시": ["사하구", "동래구", "북구", "해운대구", "수영구", "남구", "연제구", "중구", "영도구", "사상구", "금정구", "기장군", "동구", "부산진구", "강서구", "서구"],
        "충청북도": ["괴산군", "영동군", "청주시 청원구", "단양군", "청주시 상당구", "충주시", "음성군", "청주시 흥덕구", "제천시", "보은군", "옥천군", "청주시 서원구", "증평군", "진천군"],
    }
    
    road_names = {
        "부산광역시": ["해운대로", "중앙대로", "동래로", "구서로", "황령대로"],
        "충청북도": ["중앙로", "상당로", "대성로", "충렬로", "사직대로"],
    }
    
    building_suffixes = ("펠리스", "타워", "빌딩", "센터", "플라자")
    
    def __init__(self, generator):
        super().__init__(generator)
        self.all_districts = [district for districts in self.administrative_divisions.values() for district in districts]

    def address(self, invalid_ratios=None):
        if invalid_ratios is None:
            invalid_ratios = {"valid": 0.7, "invalid_district": 0.1, "invalid_road": 0.1, "invalid_building": 0.1}
        
        total = sum(invalid_ratios.values())
        normalized_ratios = {k: v / total for k, v in invalid_ratios.items()}
        
        rand = random.random()
        cumulative = 0
        for type_, prob in normalized_ratios.items():
            cumulative += prob
            if rand <= cumulative:
                if type_ == "valid":
                    return self._generate_valid_address()
                elif type_ == "invalid_district":
                    return self._generate_invalid_district_address()
                elif type_ == "invalid_road":
                    return self._generate_invalid_road_address()
                elif type_ == "invalid_building":
                    return self._generate_invalid_building_address()

    def _generate_valid_address(self):
        city = self.random_element(list(self.administrative_divisions.keys()))
        district = self.random_element(self.administrative_divisions[city])
        road = self.random_element(self.road_names.get(city, ["기본로"]))
        building_number = self.random_int(1, 100)
        detail = f"{self.random_element(self.building_suffixes)} {self.random_int(100, 9999)}호"
        return f"{city} {district} {road} {building_number}번길 {detail}"

    def _generate_invalid_district_address(self):
        city = self.random_element(list(self.administrative_divisions.keys()))
        district = self.random_element(self.all_districts)
        while district in self.administrative_divisions[city]:
            district = self.random_element(self.all_districts)
        road = self.random_element(self.road_names.get(city, ["기본로"]))
        building_number = self.random_int(1, 100)
        detail = f"{self.random_element(self.building_suffixes)} {self.random_int(100, 9999)}호"
        return f"{city} {district} {road} {building_number}번길 {detail}"

    def _generate_invalid_road_address(self):
        city = self.random_element(list(self.administrative_divisions.keys()))
        district = self.random_element(self.administrative_divisions[city])
        road = self.random_element(["가짜로", "존재하지않는길", "테스트로"])
        building_number = self.random_int(1, 100)
        detail = f"{self.random_element(self.building_suffixes)} {self.random_int(100, 9999)}호"
        return f"{city} {district} {road} {building_number}번길 {detail}"

    def _generate_invalid_building_address(self):
        city = self.random_element(list(self.administrative_divisions.keys()))
        district = self.random_element(self.administrative_divisions[city])
        road = self.random_element(self.road_names.get(city, ["기본로"]))
        building_number = self.random_int(1000, 9999)  # 비현실적으로 큰 번지수
        detail = f"{self.random_element(self.building_suffixes)} {self.random_int(10000, 99999)}호"  # 비현실적으로 큰 호수
        return f"{city} {district} {road} {building_number}번길 {detail}"