from fasthtml.fastapp import *

app, rt = fast_app(
    hdrs=(
        Meta(name="description", content="This is a custom description for my webpage."),
        Link(rel='stylesheet', href='/main.css', type='text/css'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.blue.css', type='text/css')
    )
)

def boton(boton_texto, boton_link):
    return A(boton_texto, href=boton_link, _class="button")

posts = [
    {'imageUrl': '/img1.png', 'link': '/img1.png'},
    {'imageUrl': '/img2.png', 'link': '/img2.png'},
]

def texto(title, statement, boton_texto, boton_link):
    return Div(H1(title), P(statement), boton(boton_texto, boton_link), cls="container-fluid")

# Function to create the HTML head section
def html_head(title):
    return Head(
        Title(title),
        Meta(name="description", content="a portfolio to show what im doing."),
        Link(rel='stylesheet', href='/main.css', type='text/css'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.blue.css', type='text/css')
    )

# Routes
@rt("/")
def get():
    return Html(
        html_head("Jefferson"),  # Set the title for this route
        Body(
            texto("Hallo,people call me Jefferson.", "Multimedia Designer.. Kinda, 3D noob and aspiring programmer.", "Know what things I do when I get bored 🐱‍👤", "/portfolio")
        )
    )

@rt("/portfolio")
def get():
    return Html(
        html_head("Portfolio"),  # Set the title for this route
        Body(
            texto("PORTFOLIO 🐱‍🚀", "A 'Place' to show what I'm interested in.", "Back", "/"),
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
    )

serve()
