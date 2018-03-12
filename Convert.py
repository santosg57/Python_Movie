from PIL import Image
import os, sys

prefijo = 'seg_1_'

for ii in range(10):
   nombre_in = prefijo+str(ii)+'_rgb.png'
   print nombre_in
   im = Image.open(nombre_in)
   bg = Image.new("RGB", im.size, (255,255,255))
   bg.paste(im,im)
   nombre_out = prefijo+str(ii)+'.jpg'
   print nombre_out
   bg.save(nombre_out)


