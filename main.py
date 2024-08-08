from fasthtml.fastapp import *

def boton(boton_texto, boton_link):
    return A(boton_texto, href=boton_link, _class="button")

posts = [
    {'imageUrl': '/img1.png', 'link': '/img1.png'},
    {'imageUrl': '/img2.png', 'link': '/img2.png'},
    # Add more posts as needed
]

def texto(title, statement, boton_texto, boton_link):
    return Div(
        H1(title),
        P(statement),
        boton(boton_texto, boton_link),
        cls="container-fluid"
    )

app, rt = fast_app(
    hdrs=(
        Title("My Custom Tab Title"),  # Set the title here
        Meta(name="description", content="This is a custom description for my webpage."),
        Link(rel='stylesheet', href='/main.css', type='text/css'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.blue.css', type='text/css')
    )
)

# Routes
@rt("/")
def get():
    return Div(texto("Hi, my name is Jefferson 😎", "Multimedia Designer.. Kinda, 3D noob and aspiring programmer.", "Know what things I do when I get bored 🐱‍👤", "/about"))

@rt("/about")
def get():
    return Div(
        texto("INSERT PORTFOLIO 🐱‍🚀", "A 'Place' to show what I'm interested in", "Back to The Casa", "/"),
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
        ),
        cls='container-fluid'
    )

@rt("/egg")
def get():
    return Div(
        texto("Nuevo componente", "Pasando componentes XD", "Volver a la pagina principal", "/")
    )

serve()
