library(igraph)

make.chain<-function(g, l, nv)
{
  g=add.vertices(g,1)
  nv=as.integer(nv+1)
  for (i in 2:l)
  {
    g=add.vertices(g,1)
    g=add.edges(g,c(nv,nv+1))
    nv=nv+1
  }
  return(g)
}

link.chain=function(g,v1,l)
{
  v<-v1
  g=add.edges(g,c(v1,v1+l))
  v1=v1-1
  while(v1>(v-l)+1)
  {
    g=add.edges(g, c(v1,v1+l,v1,v1+l+1))
    v1=v1-1
  }
  g=add.edges(g,c(v1,v1+l+1,v1,v1+l))
  return(g)
}

g<-make_empty_graph(n=0)
nv=0 #last added vertex id
size=129
g=make.chain(g,size,nv)
nv=nv+size
for (col in 1:size){
  g=make.chain(g,size,nv)
  g=link.chain(g,nv,size)
  nv=nv+size
}
g=as.undirected(g)
##Now g is a 128 wide hex network

#plot(g)

#ec <- eigen_centrality(g, directed = TRUE)$vector
#pg <- page_rank(g, damping = 0.999)$vector
#distList(100)
randomWalks <- function(){
  w = 0
  w <- random_walk(g, start = (size^2)/2, steps = 64)

  distance_table=distances(g) #table of pairwise distances between nodes

  dist=distance_table[w[1],w[16]]#get the distance between walk start and end

  return <- dist
}
  
distList<-c()

for (i in 1:1000 ) {
  distList <- c(distList, randomWalks())
}

print(distList)

mean(distList)
sd(distList)

print(distance_table)


plot(g)


## These are similar, but not exactly the same
cor(table(w), ec)

## But these are (almost) the same
cor(table(w), pg)