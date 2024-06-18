import requests
import sys

def request_nop(nop):
    data = {
       "api_key" : "c9e1bb68ed823b23020f890e480b7d37",
       "nop" : nop
    }
    response = requests.post("http://ipbb.opensipkd.com/v2/index.php", json=data)
    hasil = response.json()
    if hasil['status']:
      return hasil
    return None

def print_detail_nop(data):
    if data is not None: 
        print("-------------------------------------------------------")
        print("NOP              : {}".format(data['op']['nop']))
        print("MILIK            : {}".format(data['op']['wp']))
        print("ALAMAT           : {}".format(data['op']['alamat']))
        print("KELURAHAN        : {}".format(data['op']['kelurahan']))
        print("KECAMATAN        : {}".format(data['op']['kecamatan']))
        print("RT/RW            : {}/{}".format(data['op']['rt'], data['op']['rw']))
        print("LUAS BUMI        : {}".format(data['op']['luas_bumi']))
        print("LUAS BANGUNAN    : {}".format(data['op']['luas_bng']))
        print("------------------ INFORMASI PAJAK --------------------")
        print("TOTAL POKOK    : Rp. {}".format(data['op']['tot_pokok']))
        print("TOTAL DENDA    : Rp. {}".format(data['op']['tot_denda']))
        print("SISA POKOK    : Rp. {}".format(data['op']['sisa_pokok']))
        print("SISA DENDA    : Rp. {}".format(data['op']['sisa_denda']))
        print("SISA TOTAL    : Rp. {}".format(data['op']['sisa_total']))
        print("-------------------- TABEL PAJAK ----------------------")

        print("|\tTAHUN\t|\tPOKOK\t|\tDENDA\t|\tBAYAR\t|\tSISA\t|\tTANGGAL BAYAR\t|\tLUNAS\t|")
        for tahun in data['data']:
            tanggal_bayar = tahun['tgl_bayar']
            print("|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|".format(
                tahun['tahun'], tahun['pokok'], tahun['denda'], 
                tahun['bayar'], tahun['sisa'], tanggal_bayar if tanggal_bayar != "" else "\t", 
                tahun['lunas']))

        print("-------------------------------------------------------")
    else:
        print("Tidak dapat menemukan data nop")

NOP = "361900000000000000"
USE_ARGUMENT = True
if USE_ARGUMENT:
    NOP = str(sys.argv[1])

print_detail_nop(request_nop(NOP))