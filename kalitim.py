# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:22:46 2022
Python'da sınıf, nesne ve kalıtım

Ebeveyn classını üst sınıf olarak tanımlıyoruz. Daha sonra oluşturacağımız classlarda kalıtım yoluyla ebevenynin özelliklerini içinde barındırmasını saglayacagız.
super metoduyla önceki classta tanımladığımız nesneler silinmeden yeni nesne ekleyecegiz

"""

class Ebeveyn:
    def __init__(self,isim,memleket): #ilk parametre her zaman self olmak zorunda
        self.isim=isim
        self.memleket=memleket
        
    def goster(self):
        print("adım {0} ve memleketim {1}".format(self.isim,self.memleket))
        
class Cocuk(Ebeveyn):
    def __init__(self,isim,memleket,yas):
        super().__init__(isim,memleket) #yukarıdan gelen isim ve memleket nesnelerinin silinmemesini saglıyoruz
        self.yas=yas
        
    def goster(self):
        super().goster()
        print("yasım: ",self.yas)
            
c1=Cocuk("berna","istanbul",21)
c1.goster()