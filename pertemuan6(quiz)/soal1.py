def registrasi_gadget(merk, tipe, harga, sn):
    if harga < 1000000 & len(sn) >= 5:
        return({'merk':merk, 'tipe':tipe, 'harga':harga, 'sn':sn})
    else:
        print('error spesifik')
        return None
    
inventaris=[]

for i in range(3):    
    merk = input('merk:')
    tipe = input('tipe:')
    harga = input('harga:')
    sn = input('sn:')
    gadget = registrasi_gadget(merk, tipe, harga, sn)
    if gadget:
        inventaris.append(gadget)
    else:
         print('registrasi gagal')    
         
for item in inventaris:
    print(item)   
    
    

  
        
        
print(inventaris)
    


    
    