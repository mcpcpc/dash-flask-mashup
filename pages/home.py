#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dash import register_page

from dash_mantine_components import Container
from dash_mantine_components import Text
from dash_mantine_components import Title

layout = Container(
	children=[
		Title("Getting Started", order=1),
		
	]
)

register_page(
	__name__,
	path="/",
	title="Getting Started | LibreHTF",
	description="",
	layout=layout,
)