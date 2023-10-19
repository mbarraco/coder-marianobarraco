import pandas as pd


file_name = "dataset.csv"
df = pd.read_csv(file_name)



# print(df)
# print(len(df))
# print(df.columns)
# print(df.head(15))
# print(df.tail(3))
# print(
#     df.altura_tot.value_counts()
# )

df = df.sort_values("altura_tot", ascending=False)
print(df.head(15))




def generar_link_a_google_maps(lat, long):
    base_url = "https://www.google.com/maps/search/?api=1&query="
    link = base_url + f"{lat},{long}"
    return link

lat = float(input("Enter the latitud: "))
long = float(input("Enter the longitud: "))

link = generar_link_a_google_maps(lat, long)
print("_" * 90)
print(f"\n Google Maps link: {link}")
print("_" * 90)


