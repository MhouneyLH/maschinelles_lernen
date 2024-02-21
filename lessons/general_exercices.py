num: int = 1
word: str = "Hallo"
correct: bool = True
tupel: tuple = (1, 2, 3)
liste: list = [1, 2, 3]

zahlen: list = range(1, 42)
ungerade = filter(lambda x: x % 2 != 0, zahlen)
print(f"Ungerade Zahlen: {list(ungerade)}")

zweier_potenzen = map(lambda x: 2**x, range(1, 101))
print(f"zweier_potenzen: {list(zweier_potenzen)}")

a = ["Ich", "mag", "Kuchen"]
# das hier ist eine Referenz
# b = a
# das hier ist eine Kopie
b = a.copy()
b[b.index("Kuchen")] = "Pizza"

print(f"a: {list(a)}")
print(f"b: {list(b)}")
