Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.




class MiClase:
    pass


obj = MiClase()

type(obj)
<class '__main__.MiClase'>


type(Miclase)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type(Miclase)
NameError: name 'Miclase' is not defined. Did you mean: 'MiClase'?
type(MiClase)
<class 'type'>



obj.__class__
<class '__main__.MiClase'>
 MiClase.__class__
 
SyntaxError: unexpected indent
MiClase.__class__
<class 'type'>
obj.__class__.__name__
'MiClase'
obj.__name__
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    obj.__name__
AttributeError: 'MiClase' object has no attribute '__name__'. Did you mean: '__ne__'?
MiClase.__name__
'MiClase'
 'MiClase'
 
SyntaxError: unexpected indent






CLEAR
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    CLEAR
NameError: name 'CLEAR' is not defined
Miclase.var_cls = 0
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    Miclase.var_cls = 0
NameError: name 'Miclase' is not defined. Did you mean: 'MiClase'?
 NameError: name 'Miclase' is not defined. Did you mean: 'MiClase'?
 
SyntaxError: unexpected indent



MiClase.var_cls = 0
MiClase
<class '__main__.MiClase'>
<class '__main__.MiClase'>
SyntaxError: invalid syntax


MiClase.__dict__
mappingproxy({'__module__': '__main__', '__dict__': <attribute '__dict__' of 'MiClase' objects>, '__weakref__': <attribute '__weakref__' of 'MiClase' objects>, '__doc__': None, 'var_cls': 0})


pprint(MiClase.__dict__)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    pprint(MiClase.__dict__)
NameError: name 'pprint' is not defined. Did you mean: 'print'?
print(MiClase.__dict__)
{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'MiClase' objects>, '__weakref__': <attribute '__weakref__' of 'MiClase' objects>, '__doc__': None, 'var_cls': 0}
print(MiClase.__dict__)