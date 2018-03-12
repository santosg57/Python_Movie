rm(list=ls())

color = 3
tabla1 <- read.table("Promedio_SEG1.txt", header=F, sep=',')
#print(tabla1)

tabla2 <- read.table("Promedio_SEG2.txt", header=F, sep=',')
#print(tabla2)

tabla3 <- read.table("Promedio_SEG3.txt", header=F, sep=',')
#print(tabla3)

R = c(tabla1[,color], tabla2[,color], tabla3[,color])
G = c(rep(1,10), rep(2,10), rep(3,10))
boxplot(R ~ as.factor(G), main='AZUL', xlab='Segmentos')

res = aov (R ~ as.factor(G))
print(summary(res))

resT = TukeyHSD(res)

w=resT[1]
w1 = as.data.frame(w)
print(dim(w1))

nom = rownames(w1)
val = round(w1[,4],3)

dely = 10

text(.5, 40-dely, 'TukeyHSD, p-value', pos=4)
del = 2.5
y0 = 36-dely
for (ii in 1:3) {
   text(.5, y0, paste(nom[ii], ' : ', val[ii]), pos=4)
   y0 = y0 - del
}


