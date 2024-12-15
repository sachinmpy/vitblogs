import random

image_link = [
    "https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/1f9f2f9c-ae7a-4e0f-892e-ba35983a68dd/4-learnings-coding-artwork.gif",
    "https://cursus.edu/storage/thumbnails/u9MS9AJcyvDNie3onfWCoaCrjThoruWrwtHRHuzY.jpeg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSH_oVSGTI6fZSNGkEcycEFrmNKRSmKh01tzA&s",
    "https://blog.kadenze.com/wp-content/uploads/2018/12/180827_Sphere3D_frame-000125.png",
    "https://miro.medium.com/v2/resize:fit:1400/1*3eHEjMiT1ou-5kPOeC2OkQ.png",
    "https://blog.kadenze.com/wp-content/uploads/2018/12/Algorithmic-Sketches-04-724x1024.png",
    "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/9d0cbf133927413.61ca3c69b918e.gif",
    "https://art-from-code.netlify.app/day-1/session-1/index_files/figure-html/simple-composition-1.png",
    "https://i.pinimg.com/originals/2c/82/e2/2c82e2b93fb894326e61b324a984c8d1.gif",
    "https://i.pinimg.com/originals/b5/17/fb/b517fbc2fbde6f876d88740adf891d04.gif",
    "https://i.pinimg.com/originals/2f/66/ed/2f66edebc84cc96b7614cf81d33713df.gif",
    
    
]

def get_random_image():
    return random.choice(image_link)

print(get_random_image())