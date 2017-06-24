# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse

from django.views.generic import View
from django.views.generic import TemplateView

from estacaometeorologica.core.models import EstacaoMeteorologica


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self):
        context = super(IndexView, self).get_context_data()
        context.update(EstacaoMeteorologica.objects.get_json())

        return context


class EstacaoMeteorologicaView(View):

    def get(self, request):
        EstacaoMeteorologica.objects.update_data()

        return JsonResponse(EstacaoMeteorologica.objects.get_json())

