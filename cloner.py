
     #AAHIL WRITES


import platform, os
os.system ('pip2 install requests')
rana=platform.architecture()[0]
if rana=="64bit":
    import clonerb
    clonerb.menu()
elif rana=="32bit":
    import cloners
    cloners.menu()
