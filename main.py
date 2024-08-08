from fasthtml.fastapp import *

app, rt = fast_app(
    hdrs=(
        Title("Jefferson Web"),  # Set the title here
        Meta(name="description", content="Portfolio of 3d  experiments and stuff i do when i get bored"),
        Link(rel='stylesheet', href='/main.css', type='text/css'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.blue.css', type='text/css')
    )
)


def boton(boton_texto, boton_link):
    return A(boton_texto,href=boton_link,_class="button")

posts = [
     {'imageUrl': '/img1.png', 'link': '/img1.png'},
    {'imageUrl': '/img2.png', 'link': '/img2.png'},
   
]



def texto(title, statement,boton_texto,boton_link):
    return Div(H1(title),P(statement),boton(boton_texto,boton_link),cls="container-fluid")


#Routes


@rt("/")
def get():
    return Div(Title("Jefferson Rodriguez"),
        texto("Hi, my name is Jefferson 😎",P("Multimedia Designer.. Kinda, 3D noob and aspiring programmer."),"Know what things I do when I get bored 🐱‍👤","/MyStuff"))

@rt("/MyStuff")
def get():
    return Div(Title("My Stuff"),
        texto("INSERT PORTFOLIO 🐱‍🚀","A  'Place' to show what I'm interested in ","Back to The Casa","/"),
               Div(
            *[Div(
                A(
                    Img(src=post['imageUrl']),
                    href=post['link'],
                    target='_blank'
                ),
                cls='grid-item'
            ) for post in posts],
            cls='grid-container'
        )
    )





serve()