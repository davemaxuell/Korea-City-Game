import pandas
import csv

data_dict = {
    # "region": ["서울특별시", "부산광역시", "대구광역시", "인천광역시", "대전광역시", "울산광역시", "세종특별자치시", "광주광역시", "경기도", "강원도", "충청북도", "충청남도", "전라북도","전라남도", "경상남도", "경상북도", "제주특별자치도"],
    "region": ["seoul", "busan", "north chungcheong", "incheon", "gangwon", "north gyeongsang", "daegu", "south chungcheong", "sejong", "north jeolla", "gwangju", "south jeolla", "south gyeongsang", "ulsan", "jeju"],
    "coorx": [-222, 270, -7, -259, 18, 61, 235, -95, -208, -67, -269, -95, 21, 248, -119],
    "coory": [231 ,-100 ,112, 125, 213, 69, 52, 71, -7, -27, -134, -122, -61, -34, -288]
}

# Create DataFrame
korea = pandas.DataFrame(data_dict)

# Save as CSV file
korea.to_csv("대한민국_행정구역.csv", index=False)
print("CSV file created successfully.")