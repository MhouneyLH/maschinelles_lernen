zahlen: list = range(1, 101)
gerade: list = filter(lambda x: x % 2 == 0, zahlen)
print(f"Gerade Zahlen: {list(gerade)}")

zahlen = [1, 2, 3]
buchstaben = ["a", "b", "c"]
ergebnis = zip(zahlen, buchstaben)
print(f"Mit Zip: {list(ergebnis)}")

quadrate = map(lambda x: x * x, zahlen)
print(f"Mit Map: {list(quadrate)}")

# __str__ für toString-Methode
# Überschreiben == mit __eq__, etc.

# immutable
tupel = (1, 2, 3)
# mutable
liste = [1, 2, 3]
