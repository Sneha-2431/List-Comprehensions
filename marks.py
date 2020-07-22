markss=[223,222,-999,221]
new_markss=[marks/10 if marks != -999 else 0 for marks in markss]
print(new_markss)