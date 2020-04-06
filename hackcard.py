#author = mberr!
#team  = Loli4
import time,os,sys
from time import sleep as jd
m = '\x1b[1;31m'
p = '\x1b[1;37m'
i = '\x1b[1;32m'
banner = '''===================================
            >> author>> 1999dilan
            >> team>>> loLi FBI Xploit
            >> blog>>> lgi tydak ada bro
            >> email>> yoluwet@gmail.com
            >> awas lu hack email gw tabok lu!
            >> no  >>> 089691551748
            ==================================='''.format(m,p,m,p,m,p,m,p,m,p,m,p,m,p,m,p,m,p)


def menu():
  os.system('clear')
  print(banner)
  print('{}[{}>>>>>>{}]{} 3>>tellkom>>xL>>indosat>>  '.format(m,p,m,p))
  print('{}[{}>>>>>>{}]{} tembak paket all operator'.format(m,p,m,p))
  cor = str(input('{}[{}>>>>>>{}]{} masukan no hp lu >> '.format(m,p,m,p)))
  print('sabar dulu..')
  time.sleep(2)
  print(m + '[' + p +'>>>>>' + m +']' + p + 'ok siap kirim ke >> '+ i + cor )
  time.sleep(2)
  load()
def load():
        a = 0

        while a<=100: #MEMBUAT HITUNGAN BIASA
             sys.stdout.write('\rtunggu tod... '+str(a)+'%  ')
             sys.stdout.flush()
             a=a+1 #NILAI A DITAMBAH 1
             jd(0.1)  #Waktu Jeda
        done()
def done():
  time.sleep(3)
  print('\n{}[{}>>>>>>{}]{} selamat lu dapat 4GB untuk 1 detik..'.format(m,p,m,p))
if __name__ == '__main__':
  menu()
  input ('tekan ok untuk keluar dari system')
  input ('mau pergi ketik exit =')
  print ('tapi sebelum pergi')
  print ('sebaik nya lu ucapin salam dlu')
  input ('masukan asalamualaikum = ')
  print ('walaikum salam dadah!!')