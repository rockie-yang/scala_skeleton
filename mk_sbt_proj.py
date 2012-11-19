#!/usr/bin/python
print('make an empty sbt project')

from optparse import OptionParser

usage = "usage: %prog [options] arg"
parser = OptionParser(usage)
parser.add_option("-n", "--name", dest="name",
				  default='example', help="sbt project name")
parser.add_option("-v", "--version", dest="version",
				  default='0.1', help="sbt project version")
parser.add_option("-s", "--scala_version", dest="scala_version",
				  default='2.9.2', help="scala version")
parser.add_option("-o", "--organization", dest="organization",
				  default='org.example', help="orgnization")
parser.add_option("-r", "--remove_path", default=True,
                      action="store_true", dest="remove_path")

(options, args) = parser.parse_args()


import sys
import os
from os import path
import shutil

template_path = 'template'
target_path = options.name


if path.exists(target_path) and options.remove_path:
	shutil.rmtree(options.name)

print('making default directory structure')

shutil.copytree(template_path, target_path)

def format_template(file_path, format_map):
	template_content = open(file_path, 'r').read()
	print(template_content)
	formated_content = template_content.format(**format_map)
	
	open(file_path, 'w').write(formated_content)
	

format_template(target_path + '/build.sbt', {
	'name' : options.name,
	'version' : options.version,
	'organization' : options.organization,
	'scala_version' : options.scala_version})

