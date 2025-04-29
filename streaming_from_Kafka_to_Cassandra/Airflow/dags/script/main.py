import json
from typing import Dict
import requests
from kafka import KafkaProducer
import time

def get_data() -> Dict:
    try:
        response = requests.get("https://fakerapi.it/api/v2/addresses?_quantity=1", timeout=5)
        response.raise_for_status()
        response = response.json()['data'][0]
        return response
    except requests.RequestException as e:
        raise Exception(f"Error fetching data: {e}") from e


# def format_data(raw_data: Dict) -> Dict:
#     formatted = {
#         street: raw_data['street'],
#         streetname: raw_data["streetname"],
#         building_number: raw_data["building_number"],
#         city: raw_data["city"],
#         country: raw_data["country"],
#         country_code: raw_data["country_code"],
#         latitude: raw_data["latitude"],
#         longitude: raw_data["longitude"],
#     }
#     return formatted


def stream_data():
    try:
        raw_data = get_data()
        # user_data = format_data(raw_data)

        producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                 max_block_ms=8000,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        
        producer.send('user_data', raw_data)
    except Exception as e:
        print(f"Streaming error: {e}")