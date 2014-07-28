from django.core.context_processors import csrf
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

import simplejson

from util import *

def home(request):
  return render_to_response('oj/home.html',
                            context_instance=RequestContext(request))

def code(request):
  template_file = open(CODES_DIR + '/test_C.c', 'r')

  render_dict = {}
  render_dict['template_text'] = template_file.read()
  
  template_file.close()

  return render_to_response('oj/code.html', render_dict,
                            context_instance=RequestContext(request))

def about(request):
  return render_to_response('oj/about.html',
                            context_instance=RequestContext(request))

def submit(request):
  if request.method != 'POST':
    return render_to_response('oj/code.html',
                              context_instance=RequestContext(request))

  code = request.POST.get('code', '')
  lang = request.POST.get('language', '')
  lang = transfer(lang)
  print code, lang, type(lang)

  file_name = 'test_' + LANGUAGE[lang]
  save_path = CODES_DIR + '/' + file_name + '.' + POSTFIX[lang]
  print save_path

  save_file = open(save_path, 'w')
  save_file.write(code)
  save_file.close()

  compileit(file_name, save_path, lang)

  return render_to_response('oj/code.html',
                            context_instance=RequestContext(request))

def ajax_get_templates(request, language):
  language = int(language)
  return HttpResponse(simplejson.dumps({'text': get_templates(language)}))
