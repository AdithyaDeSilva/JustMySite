from datetime import date
from django.shortcuts import render

allPosts = [
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
        "image": "embeded-systems.jpeg",
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
        "image": "processor.jpeg",
        "author": "DeHell",
        "date": date(2021, 5, 21),
        "title": "Processor Architectures.",
        "excerpt": """An embedded system is a computer system—a combination of a computer processor, computer memory, and input/output peripheral devices—that has a dedicated function within a larger mechanical or electronic system.""",
        "content": """ 
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa voluptatibus eum nemo, perspiciatis quis delectus eaque necessitatibus corrupti at modi doloribus, repudiandae fugit velit maiores vel minus aspernatur qui iure.
        Rerum similique et error, officiis illum beatae modi natus sapiente inventore quos aut suscipit quae commodi a optio tenetur! Adipisci quaerat, deserunt eveniet ipsa quos magni enim eum dignissimos maxime?
        """
    },    
    {
        "slug": "metaverse",
        "image": "metaverse.jpeg",
        "author": "DeHell",
        "date": date(2021, 2, 19),
        "title": "What is Metaverse?",
        "excerpt": """A metaverse is a network of 3D virtual worlds focused on social connection.""",
        "content": """ 
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa voluptatibus eum nemo, perspiciatis quis delectus eaque necessitatibus corrupti at modi doloribus, repudiandae fugit velit maiores vel minus aspernatur qui iure.
        Rerum similique et error, officiis illum beatae modi natus sapiente inventore quos aut suscipit quae commodi a optio tenetur! Adipisci quaerat, deserunt eveniet ipsa quos magni enim eum dignissimos maxime?
        """
    },
    {
        "slug": "AR",
        "image": "AR.jpeg",
        "author": "DeHell",
        "date": date(2021, 5, 2),
        "title": "Augmented Reality?",
        "excerpt": """Augmented reality is an interactive experience of a real-world environment where the objects that reside in the real world are enhanced by computer-generated perceptual information.""",
        "content": """ 
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa voluptatibus eum nemo, perspiciatis quis delectus eaque necessitatibus corrupti at modi doloribus, repudiandae fugit velit maiores vel minus aspernatur qui iure.
        Rerum similique et error, officiis illum beatae modi natus sapiente inventore quos aut suscipit quae commodi a optio tenetur! Adipisci quaerat, deserunt eveniet ipsa quos magni enim eum dignissimos maxime?
        """
    }

]

def getDate(post):
    return post['date']
# Create your views here.

def index(request):
    sortedPosts = sorted(allPosts , key= getDate)
    latestPosts = sortedPosts[-4:]
    return render(request, "blog/index.html",{
        "posts": latestPosts
    })

def posts(requset):
    return render(requset, "blog/all-posts.html",{
        "allPosts" : allPosts
    })

def postDetails(request, slug):
    requiredPost =next(post for post in allPosts if post['slug'] == slug)
    return render(request, "blog/post-detail.html",{
        "post" : requiredPost
    })
