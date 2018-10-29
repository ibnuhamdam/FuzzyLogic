
# buka file untuk dibaca dan ditulis
file_data = open("DataTugas2.csv", "r+")
# arpdt = array pendapatan
# arhtg = array Hutang
# idpdt = array indeks pendapatan
# idhtg = array indeks hutang
arpdt = [] 
arhtg = []
indeks = []
arb = []
i = 0
n = 0
x = 0
m = 0
kata = ""
spasi = 0
baris = 0
data = (file_data.readlines())
# convert dari scv kedalam tupple
for teks in data:
    arb.append(data[i])
    i+= 1
for teks in arb:
    for n in (arb[m]):
        if(str(n) != ',') and (str(n) != ' ') and (str(n) != '\n'):
            kata += str(n)
        elif(str(n) == ' '):
            if(spasi == 1):
                if (m>0):
                    arpdt.append(float(kata))
                else:
                    arpdt.append(kata)
            kata = ''
            spasi += 1  
        elif (str(n) == '\n'):
            baris = 0
            if (m>0):
                arhtg.append(float(kata))
            else:
                arhtg.append(kata)
            pass
        else:
            pass   
    spasi = 0  
    indeks.append(m)
    m += 1
del (arhtg[0]) #hapus array pertama yang bukan float
del (arpdt[0]) #hapus array pertama yang bukan float
del (indeks) #Mulai dari 1
# Pdptan : 
# Range : [0,2]
# GPA > 1.40 (tinggi)
# GPA <= 0.6 (rendah)
# GPA (0.6,1.4] = fuzzy area (sedang)

# Hutang : 
# Range : [0,100]
# GPA > 67.5 (banyak)
# GPA <= 33.5 (sedikit)
# GPA (33.5,67.5] = fuzzy area (sedang)

GPApdt = []
GPAhtg = []
mungkin = 0
diterima = 0
tidak = 0
print (arpdt[0])
print (arhtg[0])

for angka in range(0,100):
    if(arpdt[angka] > 1.40):
        GPApdt.append('tinggi')
    elif (arpdt[angka] <= 0.6):
        GPApdt.append('rendah')
    elif (arpdt[angka] > 0.6) and (arpdt[angka] <= 1.40):
        GPApdt.append('sedang')

for angka in range(0,100):
    if(arhtg[angka] > 67.5):
        GPAhtg.append('banyak')
    elif (arhtg[angka] <= 33.5):
        GPAhtg.append('sedikit')
    elif (arhtg[angka] > 33.5) and (arhtg[angka] <= 67.5):
        GPAhtg.append('sedang')
#inference
GPAscore = []
GPAditerima = []
inference = [],[],[]
for z in range(0,100):
    if (GPApdt[z] == 'tinggi') and (GPAhtg[z] == 'banyak'):
        GPAscore.append('mungkin')
        mungkin += 1
    elif (GPApdt[z] == 'tinggi') and (GPAhtg[z] == 'sedang'):
        GPAscore.append('mungkin')
        mungkin += 1
    elif (GPApdt[z] == 'tinggi') and (GPAhtg[z] == 'sedikit'):
        GPAscore.append('tidak')
        tidak += 1
    elif (GPApdt[z] == 'sedang') and (GPAhtg[z] == 'banyak'):
        GPAscore.append('diterima')
        GPAditerima.append(str(z+1)+ ' diterima\n')
        diterima += 1
    elif (GPApdt[z] == 'sedang') and (GPAhtg[z] == 'sedang'):
        GPAscore.append('mungkin')
        mungkin += 1
    elif (GPApdt[z] == 'sedang') and (GPAhtg[z] == 'sedikit'):
        GPAscore.append('tidak')
        tidak += 1
    elif (GPApdt[z] == 'rendah') and (GPAhtg[z] == 'banyak'):
        GPAscore.append('diterima')
        GPAditerima.append(str(z+1)+ ' diterima \n')
        diterima += 1
    elif (GPApdt[z] == 'rendah') and (GPAhtg[z] == 'sedang'):
        GPAscore.append('diterima')
        GPAditerima.append(str(z+1)+ ' diterima \n')
        diterima += 1
    elif (GPApdt[z] == 'rendah') and (GPAhtg[z] == 'sedikit'):
        GPAscore.append('mungkin')
        mungkin += 1

#deffuzzy (sugeno)
x = (100*diterima)
y = (75*mungkin)
z = (60*tidak)
fuzzy = ((x+y+z)/(diterima+mungkin+tidak))
print (fuzzy)


file_data2 = open("20Penerima.csv","w")

file_data2.write('DAFTAR PENERIMA BANTUAN BLT : ')
for data_diterima in range(0,20):
    file_data2.write(GPAditerima[data_diterima])

file_data2.close()

file_data.close()