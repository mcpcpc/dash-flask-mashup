#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dash import register_page

from dash_mantine_components import Container
from dash_mantine_components import Text
from dash_mantine_components import Title

layout = Container(
	children=[
		Title("Getting Started", order=1),
		Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus euismod sem lorem, in fermentum magna auctor eget. Duis molestie dignissim ullamcorper. Aliquam cursus felis in lobortis auctor.", size="xl"),
	]
)

register_page(
	__name__,
	path="/",
	title="Getting Started | LibreHTF",
	description="",
	layout=layout,
)