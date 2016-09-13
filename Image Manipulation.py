pics=[] #list
makeEmptyPicture(495,557) #setting the range of y and x for the new Picture
folder="/home/anita/project1/Project1/Project1Images/" #path to the folder containing the pictures

for ix in range(1,10): #for loop irriate through the whole pics 
  pics.append(makePicture(folder + str(ix) +".png")) 
  print pics

makePic=makeEmptyPicture(495,557) #initializing makePic 
redPixelList=[]#making a list for the red pixels list for it to get stored
greenPixelList=[] #make a list for Green pixel list
bluePixelList=[]# make a list for the blue pixels
median = 9/2 #finding the median of 9 images 

for x in range(0,495):
  for y in range(0,557):
    redPixelList=[]
    greenPixelList=[]
    bluePixelList=[]
    for index in range (0,9):
   
  
      pixel =getPixel(pics[index],x,y)
    
      red = getRed(pixel)
      green = getGreen(pixel)
      blue = getBlue(pixel)
    
    
      redPixelList.append(red)
      greenPixelList.append(green)
      bluePixelList.append(blue)
    redPixelList.sort()
    greenPixelList.sort()
    bluePixelList.sort()    
    
    rmedian=redPixelList[4]
    gmedian=greenPixelList[4]
    bmedian=greenPixelList[4]
    
    
    
    pixel =getPixel(makePic,x,y)
    
    setRed(pixel,rmedian)
    setGreen(pixel,gmedian)
    setBlue(pixel,bmedian)

    #print makePic
    


show (makePic)
