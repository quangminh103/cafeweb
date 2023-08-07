from PIL import Image
 
ImgName = "download.png" # ten file
savedImgName = "history_icon.png" # ten file save
path = "images/" + ImgName
im = Image.open(path)

newsize = (30, 30) # kick co muon resize
im = im.resize(newsize)
im.save(savedImgName)
