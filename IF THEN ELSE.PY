            harga_baju = 200000
uang_dompet = 98000

if uang_dompet >= harga_baju :
    print ("Anda bisa membeli baju ini.")
    sisa_uang = uang_dompet - harga_baju
    print ("Sisa uang anda adalah:", sisa_uang)
else:
    print ("Maaf, uang anda tidak cukup untuk membeli baju ini.")
    kekurangan_uang = harga_baju - uang_dompet
    print ("Anda kekurangan:", kekurangan_uang)

