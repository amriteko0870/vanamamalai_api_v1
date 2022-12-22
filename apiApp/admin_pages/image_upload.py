from django.core.files.storage import FileSystemStorage
import os



def image_upload(img,img_path):
    fs = FileSystemStorage()
    img_path = 'media/' + img_path
    list_files = os.listdir(img_path)
    print('------------------- PATH -------------------------')
    print(list_files)
    print('--------------------------------------------------')
    # if img.name in list_files:
    #     os.remove(img_path+img.name)    
    file = fs.save(img.name, img)
    return (file)