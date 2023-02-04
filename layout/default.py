from dash import page_container
from dash import clientside_callback
from dash import dcc

from dash_mantine_components import Avatar
from dash_mantine_components import Anchor
from dash_mantine_components import Navbar
from dash_mantine_components import Header
from dash_mantine_components import MantineProvider
from dash_mantine_components import NotificationsProvider
from dash_mantine_components import Button
from dash_mantine_components import Container
from dash_mantine_components import Group
from dash_mantine_components import Stack
from dash_mantine_components import Text

header = Header(
    height=57,
    fixed=True,
    p="md",
    children=[
        Group(
            position="apart",
            align="flex-start",
            spacing="xs",
            children=[
                Group(
                    children=[
                        Button(
                            "Getting Started",
                            id="getting-started",
                            compact=True,
                            variant="subtle",
                        ),
                        Button(
                            "Evaluation",
                            id="evaluation",
                            compact=True,
                            variant="subtle",
                        ),
                        Button(
                            "Manage",
                            id="manage",
                            compact=True,
                            variant="subtle",
                        ),
                    ]
                ),
                Group(
                    children=[
                        Button(
                            "Log In",
                            id="login",
                            compact=True,
                            variant="light",
                        ),
                    ]
                ),
            ]
        ),
    ]
)

wrapper = Container(
    id="wrapper",
    pt=57,
    children=page_container
)

navbar = Navbar(
    id="navbar",
    fixed=True,
    position={"top": 57},
    width={"base": 200},
    children=[
        Group(
            p="xl",
            spacing="xl",
            children=[
                Avatar(radius="xl", size="lg"),
                Text(
                    size="xs",
                    children=[
                        Stack(
                            spacing="xs",
                            children=[
                                "John Smith",
                                Anchor("Log Out", href=""),
                            ]
                        )
                    ]
                )
            ]
        )
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