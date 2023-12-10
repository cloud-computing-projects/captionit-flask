from transformers import pipeline

def captioning(image):
    captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    return captioner(image)

if __name__ == '__main__':
   print( captioning('nature4.jpeg'))