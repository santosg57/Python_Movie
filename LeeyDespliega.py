from scipy import misc
import pylab
import imageio
import time
import random as ran
filename = 'PELICULA_FINAL_PILOTO.m4v'
vid = imageio.get_reader(filename,  'ffmpeg')

datos = vid.get_meta_data()
size = datos['size']
nframes = datos['nframes']
duracion = datos['duration']

prefijo = 'seg_1_'

#i1 = .1
#i2 = 58.
#i1 = 61.
#i2 = 180.
i1 = 189
i2 = 271
for ss in range(10):
   name = prefijo + str(ss)
   x = ran.uniform(i1,i2)
   corte = int(x*(nframes - 1)/duracion)
   print corte
   image = vid.get_data(corte)
   misc.imsave(name+'.jpg', image)
#   fig = pylab.figure()
#   fig.suptitle('image #{}'.format(corte), fontsize=20)
#   pylab.imshow(image)
#   #pylab.show()
#   pylab.savefig("%s_rgb.png" % name,bbox_inches='tight')
#   pylab.clf()
#plt.savefig('test.png',bbox_inches='tight',pad_inches=0)


