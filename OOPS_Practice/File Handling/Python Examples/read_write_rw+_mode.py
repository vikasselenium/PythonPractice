
with open("test_r+_mode.txt", 'r+') as f:
   f.write("All Students are Nice")
   print(f.seek(0))
   print(f.read())
   f.seek(17)
   f.write("Gem!")
   f.seek(0)
   print(f.read())