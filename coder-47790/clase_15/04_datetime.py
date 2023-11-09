from datetime import datetime


ahora_mismo = datetime.now()

print(ahora_mismo)
print("_" * 90)
print(ahora_mismo.year)
print(ahora_mismo.month)
print(ahora_mismo.day)
print(ahora_mismo.hour)
print(ahora_mismo.minute)
print(ahora_mismo.microsecond)
print("_" * 90)

print(ahora_mismo.strftime("%b b"))
print(ahora_mismo.strftime("%b/%d: %a"))
print("_" * 90)

argentina_campeon = datetime(year=2022, month=12, day=18)
print(argentina_campeon.strftime("%b/%d: %A"))
