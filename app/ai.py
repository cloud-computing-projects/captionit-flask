from transformers import pipeline

def captioning(image):
    captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    return captioner(image)