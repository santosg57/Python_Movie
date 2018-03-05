import pylab
import imageio
import time

filename = 'PELICULA_FINAL_PILOTO.m4v'
vid = imageio.get_reader(filename,  'ffmpeg')
print type(vid)

nums = [10, 287]
for num in range(10):
    print num
    image = vid.get_data(num)
    print image.shape
    fig = pylab.figure()
    fig.suptitle('image #{}'.format(num), fontsize=20)
    pylab.imshow(image)
    time.sleep(5)
pylab.show()
