import pyqrcode 
from pyqrcode import QRCode
import json
  
content = "@misc{ ldgonzalez,\n\t" + "name = { Lázaro Daniel González Martínez },\n\t" + "title = { Modelos de metapoblaciones para el análisis de epidemias }, \n\t" + 'advisors = { Dr. José A. Mesejo Chiong, Dra. Angela M. León Mecías },\n\t' + 'year = 2024,\n\t' + "university = { University of Havana },\n\t" + 'type = { Diploma Thesis }\n' + "}"

print (content)
  
#~ # Generate QR code
url = pyqrcode.create(content)
  
# Create and save the svg file naming "myqr.svg" 
url.svg("qrcode-tesis.svg", scale = 8) 


##Por algun motivo estas lineas no me compilaban asi que cree la funcion de abajo
##usando otras librerias para poder crear el QR como png
# Create and save the png file naming "myqr.png" 
# url.png('qrcode-tesis.png', scale = 6) 


import qrcode 
from PIL import Image 
   
def gen_qr_code(data):
    qr = qrcode.QRCode(version=1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10, border= 4)
    qr.clear()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "#000000", background_color="#f7f7fa")
    img.save(f"qrcode-tesis.png")
    print("salvado")

gen_qr_code(content)
