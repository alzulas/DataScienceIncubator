install.packages("sqldf")
library(sqldf)
library(ggplot2)

data = read.csv.sql()

data(titanic3, package="PASWR")
colnames(titanic3)
head(titanic3)

DF=sqldf('select age from titanic3 where age != "NA"')
qplot(DF$age,data=DF, geom="histogram")