#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dash import register_page

from dash_mantine_components import Container

layout = Container(
	children=[]
)

register_page(
	__name__,
	path="/",
	title="Getting Started | LibreHTF",
	description="",
	layout=layout,
)