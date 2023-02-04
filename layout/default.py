from dash import page_container
from dash import clientside_callback
from dash import dcc
from dash_iconify import DashIconify
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
from dash_mantine_components import Accordion
from dash_mantine_components import AccordionItem
from dash_mantine_components import AccordionControl
from dash_mantine_components import AccordionPanel


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
                            leftIcon=DashIconify(icon="bx:log-in-circle"),
                        ),
                    ]
                ),
            ]
        ),
    ]
)

wrapper = Container(
    id="wrapper",
    my=57,
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
                Avatar(radius="xl", size="md"),
                Text("John Smith")
            ]
        ),
        Accordion(
            chevronPosition="right",
            children=[
                AccordionItem(
                    value="getting-started",
                    children=[
                        AccordionControl("Getting Started"),
                        AccordionPanel(),
                    ]
                ),
                AccordionItem(
                    value="evaluate",
                    children=[
                        AccordionControl("Evaluate"),
                        AccordionPanel(),
                    ]
                ),
                AccordionItem(
                    value="manage",
                    children=[
                        AccordionControl("Manage"),
                        AccordionPanel(
                            
                        ),
                    ]
                ),
            ]
        ),
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