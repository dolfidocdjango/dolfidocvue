from django.contrib import admin
from .models import (
    Cardiologista,
    Endereco,
    Clinica,
    CBO,
    CBOEspecialidade,
    Medicos,
    Config,
)


# ============================================================
# CARDIOLOGISTA
# ============================================================
@admin.register(Cardiologista)
class CardiologistaAdmin(admin.ModelAdmin):
    list_display  = ("nome", "crm", "uf", "cidade", "especialidade", "valor")
    search_fields = ("nome", "crm", "cidade", "especialidade")
    list_filter   = ("uf", "cidade", "especialidade")
    ordering      = ("nome",)


# ============================================================
# ENDERECO
# ============================================================
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display  = ("no_logradouro", "nu_endereco", "no_bairro", "no_municipio", "co_sigla_estado", "co_cep")
    search_fields = ("no_logradouro", "no_bairro", "no_municipio", "co_cep")
    list_filter   = ("co_sigla_estado", "no_municipio")
    ordering      = ("no_logradouro",)


# ============================================================
# CLINICA
# ============================================================
@admin.register(Clinica)
class ClinicaAdmin(admin.ModelAdmin):
    list_display  = ("no_fantasia", "no_razao_social", "endereco")
    search_fields = ("no_fantasia", "no_razao_social")
    list_filter   = ()
    ordering      = ("no_fantasia",)


# ============================================================
# CBO
# ============================================================
@admin.register(CBO)
class CBOAdmin(admin.ModelAdmin):
    list_display  = ("cod_cbo", "cod_cbo_label")
    search_fields = ("cod_cbo", "cod_cbo_label")
    ordering      = ("cod_cbo",)


# ============================================================
# CBO ESPECIALIDADE
# ============================================================
@admin.register(CBOEspecialidade)
class CBOEspecialidadeAdmin(admin.ModelAdmin):
    list_display  = ("cbo", "cod_cbo_especialidades_label")
    search_fields = ("cod_cbo_especialidades_label",)
    ordering      = ("cod_cbo_especialidades_label",)


# ============================================================
# MEDICOS (NOVO ADMIN AJUSTADO)
# ============================================================
@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    list_display  = (
        "no_profissional",
        "nu_registro",
        "sg_uf_crm",
        "co_conselho_classe",
        "nu_telefone",
        "cod_cbo",
        "clinica",
    )

    search_fields = (
        "no_profissional",
        "nu_registro",
        "sg_uf_crm",
        "co_conselho_classe",
        "nu_telefone",
        "cod_cbo__cod_cbo_label",
        "clinica__no_fantasia",
    )

    list_filter = (
        "sg_uf_crm",
        "cod_cbo",
        "clinica",
    )

    ordering = ("no_profissional",)


# ============================================================
# CONFIG
# ============================================================
@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")


