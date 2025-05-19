import pandas as pd
import json

# 1. 加载数据
df = pd.read_csv('data/bottle data/bottle.csv')

# 2. 过滤掉氧气值 -999
df = df[df['micromoles_of_oxygen_per_unit_mass_in_sea_water'] != -999]

# 3. 为 JSON 准备只保留需要字段
columns_to_keep = [
    'time',
    'depth',
    'Latitude',
    'Longitude',
    'micromoles_of_oxygen_per_unit_mass_in_sea_water',
    'sea_water_density',
    'sea_water_practical_salinity',
    'sea_water_temperature'
]

df = df[columns_to_keep]

# 4. 转成 dict 列表，注意时间转 ISO 格式字符串
df['time'] = pd.to_datetime(df['time'])
df['time'] = df['time'].dt.strftime('%Y-%m-%dT%H:%M:%S')

data_list = df.to_dict(orient='records')

# 5. 导出为 JSON 文件（推荐放当前文件夹或 static 文件夹）
with open('static_data.json', 'w') as f:
    json.dump(data_list, f, indent=2)

print(f"Successfully exported {len(data_list)} records to static_data.json")
