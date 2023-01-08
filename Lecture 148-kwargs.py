# **Kwargs return a dictionary 

def info(**kwargs):
    for k,v in kwargs.items():
        print(k,":",v)

info(Name = 'Abhay', Age = 18, Section = 'KOC27')
