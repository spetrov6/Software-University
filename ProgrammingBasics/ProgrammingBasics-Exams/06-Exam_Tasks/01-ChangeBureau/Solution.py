bitcoin = int(input())
china = float(input())
comision = float(input()) * 0.01
bitcoin_leva = bitcoin * 1168
china_leva = (china * 0.15) * 1.76
euro = (bitcoin_leva + china_leva) / 1.95
total = euro - (euro * comision)
print(f"{total:.2f}")
