def xkcd():
    from PIL import Image
    import xkcd
    from changeDir import changeDirectory as cd
    from os import getcwd
    comic=xkcd.getRandomComic()
    cd("resources")
    outputDir=getcwd()
    comic.download(output=outputDir,outputFile='xkcd.jpg',silent=False)
    img=Image.open('xkcd.jpg')
    img.show()
    cd("code")
    return img
    
    
