from django.core.context_processors import csrf
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

import os
import subprocess

def home(request):
  test_file = open(os.getcwd() + '/compiles/test.cpp', 'r')

  render_dict = {}
  render_dict['test_cpp'] = test_file.read()
  
  print test_file.read()
  test_file.close()

  if request.method == 'POST':
    return submit(request, render_dict)

  return render_to_response('oj/base.html', render_dict,
                            context_instance=RequestContext(request))

def submit(request, render_dict):
  code = request.POST.get('code', '')
  print code

  test_save_file = open(os.getcwd() + '/compiles/test_save.cpp', 'w')
  test_save_file.write(code)
  test_save_file.close()

  test_save_file_path = os.getcwd() + '/compiles/test_save.cpp'
  command = ["g++", test_save_file_path, "-o", os.getcwd() + "/compiles/test.out"]

  child = subprocess.Popen(command, stdout=subprocess.PIPE)
  print child.communicate()

  return render_to_response('oj/base.html',
                            context_instance=RequestContext(request))
