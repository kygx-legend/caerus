# All helper tools are here.

import os
import subprocess

BASE_DIR = os.getcwd()
ASSETS_DIR = BASE_DIR + '/assets'
CODES_DIR = ASSETS_DIR + '/codes'
TARGETS_DIR = ASSETS_DIR + '/targets'

LANGUAGE = {0: 'C', 1: 'Cpp', 2: 'Java', 3: 'Python'}
POSTFIX = {0: 'c', 1: 'cpp', 2: 'java', 3: 'py'}
COMPILER = {0: 'gcc', 1: 'g++', 2: 'javac', 3: 'python'}

def check_directory():
  if not os.path.exists(ASSETS_DIR):
    os.mkdir(ASSETS_DIR)
    print ASSETS_DIR + ' is created!'

  if not os.path.exists(CODES_DIR):
    os.mkdir(CODES_DIR)
    print CODES_DIR + ' is created!'

  if not os.path.exists(TARGETS_DIR):
    os.mkdir(TARGETS_DIR)
    print TARGETS_DIR + ' is created!'

check_directory()

def get_templates_path(lang):
  return CODES_DIR + '/test_' + LANGUAGE[lang] + '.' + POSTFIX[lang]

def get_templates(lang):
  template_file = open(get_templates_path(lang), 'r')
  return template_file.read()

def transfer(lang):
  if lang == 'C' or lang == 'c':
    return 0
  elif lang == 'C++' or lang == 'Cpp' or lang == 'cpp':
    return 1
  elif lang == 'Java' or lang == 'java':
    return 2
  elif lang == 'Python' or lang == 'python':
    return 3

def compileit(source_file, path, lang):
  command = []
  if lang == 0:
    command = [COMPILER[lang], path, "-o", TARGETS_DIR + "/" + source_file + ".o"]
  elif lang == 1:
    command = [COMPILER[lang], path, "-o", TARGETS_DIR + "/" + source_file + ".out"]
  elif lang == 2:
    command = [COMPILER[lang], path, "-d", TARGETS_DIR]
  elif lang == 3:
    command = [COMPILER[lang], path]

  if len(command) == 0:
    return

  child = subprocess.Popen(command, stdout=subprocess.PIPE)
  print child.communicate()
