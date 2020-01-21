#!/usr/bin/env python3
import cgi
import os
import cgitb
cgitb.enable()

print("Content-Type: text/plain\r\n\r\n")
#print()
#print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
for key in os.environ:
	print(key,os.environ[key])
#print(os.environ)
