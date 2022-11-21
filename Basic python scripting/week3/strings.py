varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

print (f"Hello {varName: <0s}")
print (f"{varRed: <0s}-{varGreen: <0s}-{varBlue: <0s}")
print (f"Is this {varGreen.lower(): <0s} or {varBlue.lower(): <0s}?")
print (f"My name is {varName.upper(): <0s}")
print (f"[{varRed:+^7s}]")
print (f"[{varGreen.lower():=<7s}]")
print (f"[{varBlue.lower():*>9s}]")
print (f"{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}")
print (f"{varLoot: <.7f}")
print (f"{varLoot: <.1f}")
print (f"I have ${varLoot: <.2f}")
print (f"[{varRed:$^10s}][{varGreen:$^10s}][{varBlue:$^10s}]")
print (f"[{varRed[::-1]: ^9s}] [{varGreen: ^9s}] [{varBlue[::-1]: ^10s}]")
print (f"First Color:[{varRed: <0s}] Second Color:[{varGreen: <0s}] Third Color:[{varBlue: <0s}]")
