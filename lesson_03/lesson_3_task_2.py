from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy s26", "+79175647634"),
    Smartphone("Honor", "600 pro", "+798743212"),
    Smartphone("Nokia", "3310", "+79547898")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")