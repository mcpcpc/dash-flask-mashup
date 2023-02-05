#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dash import register_page

from dash_mantine_components import Container
from dash_mantine_components import Text
from dash_mantine_components import Title
from dash_mantine_components import PasswordInput
from dash_mantine_components import TextInput
from dash_mantine_components import Button
from dash_mantine_components import Stack
from dash_mantine_components import Group

layout = Container(
	children=[
		Title("Log In", order=1, weight=400),
		Stack(
			spacing="lg",
			children=[
				Text("Welcome back! Please provide valid credentials to access additional tools."),
				TextInput(
					id="username",
					placeholder="Username",
					style={"max-width": 250},
				),
				PasswordInput(
					id="password",
					placeholder="Password",
					style={"max-width": 250},
				),
				Group(
					children=[
						Button(
							id="submit",
							children="Log In",
							variant="light",
						),
						Button(
							id="cancel",
							children="Cancel",
							variant="subtle",
						),
					]	
				)
			]
		)
	]
)

register_page(
	__name__,
	path="/login",
	title="Log In | LibreHTF",
	description="",
	layout=layout,
)