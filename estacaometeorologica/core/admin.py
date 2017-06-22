# -*- coding:utf-8 -*-

from django.contrib import admin

from estacaometeorologica.core.models import EstacaoMeteorologica


@admin.register(EstacaoMeteorologica)
class EstacaoMeteorologicaAdmin(admin.ModelAdmin):

    pass
