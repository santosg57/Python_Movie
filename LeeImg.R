library(png)

img <- readPNG("seg_1_0_rgb.png")
print(dim(img))
image(img[,,1:3])
print(class(img))

