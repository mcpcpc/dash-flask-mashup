#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dash import register_page

from dash_mantine_components import Container
from dash_mantine_components import Text
from dash_mantine_components import Title
from dash_mantine_components import PasswordInput
from dash_mantine_components import TextInput

layout = Container(
	children=[
		Title("Log In", order=1, weight=400),
		Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus euismod sem lorem, in fermentum magna auctor eget. Duis molestie dignissim ullamcorper. Aliquam cursus felis in lobortis auctor."),
		TextInput(
			placeholder="Username",
		),
		PasswordInput(
			label="Password",
			description="Password must include at least one letter, number and special character",
			placeholder="Password",
			required=True,
			error=True,
		),
	]
)

register_page(
	__name__,
	path="/login",
	title="Log In | LibreHTF",
	description="",
	layout=layout,
)