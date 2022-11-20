xVar <- seq(-10,10, by=0.1)
length(xVar)

head(xVar)
tail(xVar)

yVar <- xVar
y2Var < xVar * 2
y3Var < xVar * 3
yhalfVar <- xVar/2

length(xVar)
length(yVar)
fivenum(xVar)
fivenum(yVar)
plot(x = xVar, y = yVar, ylim = c(-30,30))
plot(x = xVar, y = y2Var, ylim = c(-30,30))
