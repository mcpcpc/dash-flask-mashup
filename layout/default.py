from dash import page_container
from dash import clientside_callback
from dash import dcc

from dash_mantine_components import Navbar
from dash_mantine_components import Header
from dash_mantine_components import MantineProvider
from dash_mantine_components import NotificationsProvider
from dash_mantine_components import Button
from dash_mantine_components import Container
from dash_mantine_components import Group

header = Header(
    height=57,
    fixed=True,
    children=[
        Group(
            position="apart",
            align="flex-start",
            children=[
                Group(
                    children=[
                        Button(
                            "Getting Started",
                            variant="subtle",
                        ),
                        Button(
                            "Evaluation",
                            variant="subtle",
                        ),
                        Button(
                            "Manage",
                            variant="subtle",
                        ),
                    ]
                ),
                Group(
                    children=[
                        Button(
                            "Log In",
                            variant="light",
                        ),
                    ]
                ),
            ]
        ),
    ]
)

wrapper = Container(children=page_container)

navbar = Navbar(
    fixed=True,
    top=57,
    children=[
    ]
)

def layout(data):
    return MantineProvider(
        id="theme-provider",
        withGlobalStyles=True,
        withNormalizeCSS=True,
        theme={
            "colorScheme": "light",
            "fontFamily": "'Inter', sans-serif",
            "primaryColor": "indigo",
        },
        children=[
            dcc.Store(id="theme-store", storage_type="local"),
            NotificationsProvider(
                children=[
                    header,
                    navbar,
                    wrapper, 
                ]
            )
        ],
    )