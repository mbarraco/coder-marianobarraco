informacion = [
    {
        "name": {
            "common": "Portugal",
            "official": "Portuguese Republic",
            "nativeName": {
                "por": {"official": "República português", "common": "Portugal"}
            },
        },
        "tld": [".pt"],
        "cca2": "PT",
        "ccn3": "620",
        "cca3": "PRT",
        "cioc": "POR",
        "independent": True,
        "status": "officially-assigned",
        "unMember": True,
        "currencies": {"EUR": {"name": "Euro", "symbol": "€"}},
        "idd": {"root": "+3", "suffixes": ["51"]},
        "capital": ["Lisbon"],
        "altSpellings": [
            "PT",
            "Portuguesa",
            "Portuguese Republic",
            "República Portuguesa",
        ],
        "region": "Europe",
        "subregion": "Southern Europe",
        "languages": {"por": "Portuguese"},
        "translations": {
            "ara": {"official": "الجمهورية البرتغالية", "common": "البرتغال"},
            "bre": {"official": "Republik Portugalat", "common": "Portugal"},
            "ces": {"official": "Portugalská republika", "common": "Portugalsko"},
            "cym": {"official": "Portuguese Republic", "common": "Portugal"},
            "deu": {"official": "Portugiesische Republik", "common": "Portugal"},
            "est": {"official": "Portugali Vabariik", "common": "Portugal"},
            "fin": {"official": "Portugalin tasavalta", "common": "Portugali"},
            "fra": {"official": "République portugaise", "common": "Portugal"},
            "hrv": {"official": "Portugalska Republika", "common": "Portugal"},
            "hun": {"official": "Portugál Köztársaság", "common": "Portugália"},
            "ita": {"official": "Repubblica portoghese", "common": "Portogallo"},
            "jpn": {"official": "ポルトガル共和国", "common": "ポルトガル"},
            "kor": {"official": "포르투갈 공화국", "common": "포르투갈"},
            "nld": {"official": "Portugese Republiek", "common": "Portugal"},
            "per": {"official": "جمهوری پرتغال", "common": "پرتغال"},
            "pol": {"official": "Republika Portugalska", "common": "Portugalia"},
            "por": {"official": "República português", "common": "Portugal"},
            "rus": {"official": "Португальская Республика", "common": "Португалия"},
            "slk": {"official": "Portugalská republika", "common": "Portugalsko"},
            "spa": {"official": "República Portuguesa", "common": "Portugal"},
            "srp": {"official": "Португалска Република", "common": "Португал"},
            "swe": {"official": "Republiken Portugal", "common": "Portugal"},
            "tur": {"official": "Portekiz Cumhuriyeti", "common": "Portekiz"},
            "urd": {"official": "جمہوریہ پرتگال", "common": "پرتگال"},
            "zho": {"official": "葡萄牙共和国", "common": "葡萄牙"},
        },
        "latlng": [39.5, -8.0],
        "landlocked": False,
        "borders": ["ESP"],
        "area": 92090.0,
        "demonyms": {
            "eng": {"f": "Portuguese", "m": "Portuguese"},
            "fra": {"f": "Portugaise", "m": "Portugais"},
        },
        "flag": "\uD83C\uDDF5\uD83C\uDDF9",
        "maps": {
            "googleMaps": "https://goo.gl/maps/BaTBSyc4GWMmbAKB8",
            "openStreetMaps": "https://www.openstreetmap.org/relation/295480",
        },
        "population": 10305564,
        "gini": {"2018": 33.5},
        "fifa": "POR",
        "car": {"signs": ["P"], "side": "right"},
        "timezones": ["UTC-01:00", "UTC"],
        "continents": ["Europe"],
        "flags": {
            "png": "https://flagcdn.com/w320/pt.png",
            "svg": "https://flagcdn.com/pt.svg",
            "alt": "The flag of Portugal is composed of two vertical bands of green and red in the ratio of 2:3, with the coat of arms of Portugal centered over the two-color boundary.",
        },
        "coatOfArms": {
            "png": "https://mainfacts.com/media/images/coats_of_arms/pt.png",
            "svg": "https://mainfacts.com/media/images/coats_of_arms/pt.svg",
        },
        "startOfWeek": "monday",
        "capitalInfo": {"latlng": [38.72, -9.13]},
        "postalCode": {"format": "####-###", "regex": "^(\\d{7})$"},
    }
]
informacion_en_diccionario = informacion[0]
latitud_longitud = informacion_en_diccionario["latlng"]
paises_fronterizos = informacion_en_diccionario["borders"]
nombre = informacion_en_diccionario["name"]["common"]
capital = informacion_en_diccionario["capital"]
print(nombre, latitud_longitud, paises_fronterizos, capital)
