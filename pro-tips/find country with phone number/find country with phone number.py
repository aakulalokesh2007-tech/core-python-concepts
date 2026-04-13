import phonenumbers
from phonenumbers import geocoder

mobile_number="+9173XXXXXX85"

ph=phonenumbers.parse(mobile_number)

print(geocoder.description_for_number(ph,"en"))
