lista_zakupów= {
    "warzywniak": ["marchew", "seler", "rukola"],
    "piekarnia": ["bułki", "chleb", "pączek"]
}
print(lista_zakupów)
for keys in lista_zakupów:
    print("Idę do %s i kupuję tam: %s" % (keys.capitalize(),  [x.capitalize() for x in lista_zakupów[keys]]))
