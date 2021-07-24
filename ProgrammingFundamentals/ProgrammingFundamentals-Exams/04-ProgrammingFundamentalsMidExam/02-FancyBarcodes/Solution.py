import re
number_of_barcodes = int(input())
pattern = r"@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+"
for _ in range(number_of_barcodes):
    barcode = re.findall(pattern,input())
    if not barcode:
        print("Invalid barcode")
    else:
        barcode = str(barcode)
        group = [i for i in barcode if i.isdigit()]
        if len(group) > 0:
            print(f"Product group: {''.join(group)}")
        else:
            print("Product group: 00")
