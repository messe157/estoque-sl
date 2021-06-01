from django.contrib import admin
from .models import (
    EstoqueEntrada, EstoqueSaida, EstoqueItens, ProtocoloEntrega,
    ProtocoloEntregaItens,
)
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse

class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0


@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'obs', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'obs', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'

   

class ProtocoloEntregaItensInline(admin.TabularInline):
    model = ProtocoloEntregaItens
    extra = 0
    

    
@admin.register(ProtocoloEntrega)
class ProtocoloEntregaAdmin(admin.ModelAdmin):
    inlines = (ProtocoloEntregaItensInline,)
    list_display = ('__str__', 'estoque_atualizado', 'usuario',)
    list_filter = ('usuario',)
    date_hierarchy = 'created'
    search_fields = ('estoque_atualizado',)

    
    

    

