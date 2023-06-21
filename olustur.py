liste = ["Gonenc","Berkay","Yelda","Can","Eda","Ege","Elifnaz","Kubra","Onur","Baris","Cevaplar"]
import os
fileName = "app"
metin = """
"""
for item in liste:
    fPath = f"/workspace/APIDesign_Flask/Exercises/{item}"
    metin = f"""
\"\"\"
    ilk flask uygulamanızı yazmak ve başlatmak için port numarasını 452{liste.index(item)} kullanabilirsiniz.
    Hoşgeldiniz mesajı yerine isim ve soyisminizi yazmanız yeterlidir. 
\"\"\"
    """
    if not os.path.exists(fPath):
        os.mkdir(fPath)
    dosya = open(os.sep.join((fPath,f"{fileName}.py")),"w+")
    dosya.write(metin)


