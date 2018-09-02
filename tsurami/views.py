from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from tsurami.models import Note

# IndexViewというのは名前、本質はTemplateView
class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'tsurami/index.html'

    def get_context_data(self, **kwargs):

        # はじめにPostIndexViewの継承元のメソッドを呼び出す
        context = super().get_context_data(**kwargs)
        context['aaa'] = "from view"
        return context

# LoginRequiredMixinを継承する区間は常にログイン制御が行われる
class MyListView(LoginRequiredMixin, generic.ListView):
    model = Note

    def get_context_data(self, **kwargs):
        # はじめにPostIndexViewの継承元のメソッドを呼び出す
        context = super().get_context_data(**kwargs)
        context['data'] = "data exists"
        if self.model.objects == None:
            context['data'] = "no data"
        else:
            paginate_by = 5

        return context
