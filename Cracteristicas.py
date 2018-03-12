import pylab
import imageio
import time

filename = 'PELICULA_FINAL_PILOTO.m4v'
vid = imageio.get_reader(filename,  'ffmpeg')
print dir(vid)
datos = vid.get_meta_data()
size = datos['size']
print size
nframes = datos['nframes']
print type(nframes)
print nframes
duracion = datos['duration']
print type(duracion)
print duracion

