import pandas as pd


file_name = "dataset.csv"
df = pd.read_csv(file_name)



# print(df)
# print(len(df))
# print(df.columns)
# print(df.head(3))
# print(df.tail(3))
print(
    df.altura_tot.value_counts()
)












# def generate_gmaps_link(latitude, longitude):
#     base_url = "https://www.google.com/maps/search/?api=1&query="
#     link = base_url + f"{latitude},{longitude}"
#     return link

# latitude = float(input("Enter the latitude: "))
# longitude = float(input("Enter the longitude: "))

# link = generate_gmaps_link(latitude, longitude)
# print(f"\nGenerated Google Maps link: {link}")



# breakpoint()