
# it works video/audio files
# pillow library to handle images
with open("guido.jpg", "rb") as f:
    data= f.read()
    print(type(data))
    print(data)
    with open("guido_copy.jpg", "wb") as f1:
        f1.write(data)
        print("image is ready...")