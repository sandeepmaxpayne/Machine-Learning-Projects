library(warbleR)
global1 <- data.frame(matrix(ncol = 25, nrow = 0))
colnames(global1)=c("class","sound.files","selec","duration","meanfreq","sd","median","Q25","Q75",
"IQR","skew","kurt","sp.ent","sfm","mode",
"centroid","peakf","meanfun","minfun","maxfun","meandom","mindom","maxdom","dfrange","modindx")

##########################################################################################


setwd("C:\\Users\\affsa\\training\\day 1\\DIATM 2019\\Hello")

for (i in 32:48){
	print(i)
	track  = paste("Track",i,sep="")
	track  = paste(track,".wav",sep="")
	X = data.frame(sound.files=track,selec=0,start=0,end=1)
	a <- specan(X,, bp = c(0,22), wl = 512, threshold = 15)
	a["class"] = "Hello"
	print(a)
	global1 = rbind(global1,a)
}

##########################################################################################

setwd("C:\\Users\\affsa\\training\\day 1\\DIATM 2019\\Goodbye")

for (i in 54:66){
	print(i)
	track  = paste("Track",i,sep="")
	track  = paste(track,".wav",sep="")
	X = data.frame(sound.files=track,selec=0,start=0,end=1)
	a <- specan(X,, bp = c(0,22), wl = 512, threshold = 15)
	a["class"] = "Goodbye"
	print(a)
	global1 = rbind(global1,a)
}

##########################################################################################

setwd("C:\\Users\\affsa\\training\\day 1\\DIATM 2019\\Banana")

for (i in 70:87){
	print(i)
	track  = paste("Track",i,sep="")
	track  = paste(track,".wav",sep="")
	X = data.frame(sound.files=track,selec=0,start=0,end=1)
	a <- specan(X,, bp = c(0,22), wl = 512, threshold = 15)
	a["class"] = "Banana"
	print(a)
	global1 = rbind(global1,a)
}

##########################################################################################

setwd("C:\\Users\\affsa\\training\\day 1\\DIATM 2019\\Chair")

for (i in 106:118){
	print(i)
	track  = paste("Track",i,sep="")
	track  = paste(track,".wav",sep="")
	X = data.frame(sound.files=track,selec=0,start=0,end=1)
	a <- specan(X,, bp = c(0,22), wl = 512, threshold = 15)
	a["class"] = "Chair"
	print(a)
	global1 = rbind(global1,a)
}

##########################################################################################

setwd("C:\\Users\\affsa\\training\\day 1\\DIATM 2019\\IceCream")

for (i in 89:101){
	print(i)
	track  = paste("Track",i,sep="")
	track  = paste(track,".wav",sep="")
	X = data.frame(sound.files=track,selec=0,start=0,end=1)
	a <- specan(X,, bp = c(0,22), wl = 512, threshold = 15)
	a["class"] = "IceCream"
	print(a)
	global1 = rbind(global1,a)
}

########################################################################################## 



global2 = na.omit(global1)

write.csv(global2,"C:\\Users\\affsa\\training\\day 1\\DIATM 2019\\audio_data_model.csv")


##########################################################################################
##########################################################################################

validation <- data.frame(matrix(ncol = 25, nrow = 0))
colnames(validation )=c("class","sound.files","selec","duration","meanfreq","sd","median","Q25","Q75",
"IQR","skew","kurt","sp.ent","sfm","mode",
"centroid","peakf","meanfun","minfun","maxfun","meandom","mindom","maxdom","dfrange","modindx")

setwd("C:\\Users\\affsa\\training\\day 1\\DIATM 2019\\Validation")
path="C:\\Users\\affsa\\training\\day 1\\DIATM 2019\\Validation"

file.names <- dir(path, pattern =".wav")
for(i in 1:length(file.names)){
  filename = unlist(strsplit(file.names[i],"_"))[1]
  X = data.frame(sound.files=file.names[i],selec=0,start=0,end=1)
  a <- specan(X,, bp = c(0,22), wl = 512, threshold = 15)
  a["class"] = filename
  validation = rbind(validation ,a)
}
	
###########################################################################################

validation = na.omit(validation)

write.csv(validation ,"C:\\Users\\affsa\\training\\day 1\\DIATM 2019\\audio_validation.csv")  