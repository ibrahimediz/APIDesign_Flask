liste = ["Gonenc","Berkay","Yelda","Can","Eda","Ege","Elifnaz","Kubra","Onur","Baris","Cevaplar"]
import os
fileName = "app"
metin = """
"""
for item in liste:
    fPath = f"/workspace/APIDesign_Flask/Exercises/{item}"
    if not os.path.exists(fPath):
        os.mkdir(fPath)
    if not os.path.exists(os.sep.join((fPath,"app"))):
        os.mkdir(os.sep.join((fPath,"app")))
    if not os.path.exists(os.sep.join((fPath,"app","templates"))):
        os.mkdir(os.sep.join((fPath,"app","templates")))
    # open(os.sep.join((fPath,"app","__init__.py")),"a+")
    # open(os.sep.join((fPath,"app","routes.py")),"a+")
    with open(os.sep.join((fPath,f"config.py")),"w+") as dosya:
        dosya.write("""
import os
class Config(object):
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'tahmin-edemezsin'
""")
    # open(os.sep.join((fPath,f"runweb{item}.py")),"a+")

