from datetime import date
from django.shortcuts import render

posts = [
    {
        "slug" : "arduino-is-fun",
        "image": "arduino.jpeg",
        "author" : "DeHell",
        "date" : date(2022, 2, 13),
        "title" : "Arduino Programming",
        "excerpt": """Arduino is an open-source hardware and software company, project, and user community that designs and manufactures single-board microcontrollers and microcontroller kits for building digital devices.""",
        "content":""" 
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa voluptatibus eum nemo, perspiciatis quis delectus eaque necessitatibus corrupti at modi doloribus, repudiandae fugit velit maiores vel minus aspernatur qui iure.
        Rerum similique et error, officiis illum beatae modi natus sapiente inventore quos aut suscipit quae commodi a optio tenetur! Adipisci quaerat, deserunt eveniet ipsa quos magni enim eum dignissimos maxime?
        """        
    },
    {
        "slug": "embeded-systems",
        "image": "embede-systems.jpeg",
        "author": "DeHell",
        "date": date(2022, 3, 13),
        "title": "What is a Embeded System?",
        "excerpt": """An embedded system is a computer system—a combination of a computer processor, computer memory, and input/output peripheral devices—that has a dedicated function within a larger mechanical or electronic system.""",
        "content": """ 
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa voluptatibus eum nemo, perspiciatis quis delectus eaque necessitatibus corrupti at modi doloribus, repudiandae fugit velit maiores vel minus aspernatur qui iure.
        Rerum similique et error, officiis illum beatae modi natus sapiente inventore quos aut suscipit quae commodi a optio tenetur! Adipisci quaerat, deserunt eveniet ipsa quos magni enim eum dignissimos maxime?
        """
    },
    {
        "slug": "processors",
        "image": "processors.jpeg",
        "author": "DeHell",
        "date": date(2021, 5, 21),
        "title": "Modern Processor Architectures.",
        "excerpt": """An embedded system is a computer system—a combination of a computer processor, computer memory, and input/output peripheral devices—that has a dedicated function within a larger mechanical or electronic system.""",
        "content": """ 
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa voluptatibus eum nemo, perspiciatis quis delectus eaque necessitatibus corrupti at modi doloribus, repudiandae fugit velit maiores vel minus aspernatur qui iure.
        Rerum similique et error, officiis illum beatae modi natus sapiente inventore quos aut suscipit quae commodi a optio tenetur! Adipisci quaerat, deserunt eveniet ipsa quos magni enim eum dignissimos maxime?
        """
    }
]

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def posts(requset):
    return render(requset, "blog/all-posts.html")

def postDetails(request, slug):
    return render(request, "blog/post-detail.html")
