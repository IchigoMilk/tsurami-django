from django.shortcuts import render
from django.views import generic

class PostIndexView(generic.TemplateView):
  template_name = 'tsurami/index.html'

  def get_context_data(self, **kwargs):
    # はじめに継承元のメソッドを呼び出す
    context = super().get_context_data(**kwargs)
    context['aaa'] = "from view"
    return context
