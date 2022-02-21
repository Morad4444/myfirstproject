import emoji
def try_me(name):
    print('Hello to my first project Mr/Mrs')
    if len(name) == 1 :
        print(name.capitalize(), emoji.emojize(":upside-down_face:"))
    elif len(name) == 2 :
        print(name.capitalize() , emoji.emojize(":face_with_monocle:"))
    elif len(name) == 3 :
        print(name.capitalize(), emoji.emojize(":winking_face_with_tongue:"))
    elif len(name) == 4 :
        print(name.capitalize(), emoji.emojize(":slightly_smiling_face:"))
    elif len(name) == 5 :
        print(name.capitalize(), emoji.emojize(":smiling_face_with_sunglasses:"))
    elif len(name) > 5 :
        print(name.capitalize(), emoji.emojize(":zipper-mouth_face:"))
