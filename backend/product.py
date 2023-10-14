from PIL import Image

class Product:
    #" instance variables:
    # list - words extracted from image 
    # set - hidden sugars
    # set - carcinogens
    # ... potentially more 
    # "

    #constructor:
    def __init__():
        self.yay = 1

    def __init__(image):
        #instance variable of type Image called image
        self.image = image
        self.ingredients = ' '.join(reader.readtext('./ingredients.jpg', paragraph="True", detail = 0))
        

    def processIngreds():
        words = re.split(r'[,()\[\]_\;\\]', ingredients)
        for i in range(len(words)):
            words[i] = words[i].strip()
        words.remove("")
        words[len(words)-1] = words[len(words)-1].replace("and ", "")

    #" methods:
    # constructor
    # sugars - makes set w/ hidden sugars in the product
    # carcinogens - same as sugar
    # getSugars, getCarcinogens, getName
    # 
    # "