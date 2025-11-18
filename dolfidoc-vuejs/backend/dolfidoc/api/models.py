from django.db import models


# ============================================================
# 1) CARDIOLOGISTA (permanece como está hoje, com índices)
# ============================================================
class Cardiologista(models.Model):
    nome          = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    crm           = models.CharField(max_length=50,  blank=True, null=True)
    uf            = models.CharField(max_length=50,  blank=True, null=True, db_index=True)
    cidade        = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    cnpj          = models.CharField(max_length=255, blank=True, null=True)
    especialidade = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    numero        = models.CharField(max_length=20,  blank=True, null=True)
    valor         = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_index=True)
    fid           = models.CharField(max_length=255, blank=True, null=True)
    logradouro    = models.CharField(max_length=255, blank=True, null=True)
    complemento   = models.CharField(max_length=255, blank=True, null=True)
    foto          = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table            = 'cardiologista'
        verbose_name        = 'Cardiologista'
        verbose_name_plural = 'Cardiologistas'
        ordering            = ['valor', 'nome']
        indexes             = [
            models.Index(fields=['nome'],          name='idx_cardio_nome'),
            models.Index(fields=['cidade'],        name='idx_cardio_cidade'),
            models.Index(fields=['uf'],            name='idx_cardio_uf'),
            models.Index(fields=['especialidade'], name='idx_cardio_espec'),
        ]

    def __str__(self):
        return f"{self.nome} - {self.crm}/{self.uf}"


# ============================================================
# 2) ENDERECO
# ============================================================
class Endereco(models.Model):
    no_complemento  = models.CharField(max_length=255, null=True, blank=True)
    nu_endereco     = models.CharField(max_length=50,  null=True, blank=True)
    no_logradouro   = models.CharField(max_length=255, null=True, blank=True)
    no_bairro       = models.CharField(max_length=255, null=True, blank=True)
    no_municipio    = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    co_sigla_estado = models.CharField(max_length=2,   null=True, blank=True, db_index=True)
    co_cep          = models.CharField(max_length=20,  null=True, blank=True, db_index=True)

    def __str__(self):
        endereco = self.no_logradouro or "Sem logradouro"
        num      = self.nu_endereco or ""
        return f"{endereco}, {num}".strip()

    class Meta:
        verbose_name        = "Endereço"
        verbose_name_plural = "Endereços"
        ordering            = ["no_logradouro"]
        indexes             = [
            models.Index(fields=['co_cep'],          name='idx_endereco_cep'),
            models.Index(fields=['no_municipio'],    name='idx_endereco_mun'),
            models.Index(fields=['co_sigla_estado'], name='idx_endereco_uf'),
        ]


# ============================================================
# 3) CLINICA
# ============================================================
class Clinica(models.Model):
    no_razao_social = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    no_fantasia     = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    endereco        = models.ForeignKey(
        Endereco,
        on_delete    = models.SET_NULL,
        null         = True,
        blank        = True,
        related_name = "clinicas"
    )

    def __str__(self):
        return self.no_fantasia or self.no_razao_social or "Clínica"

    class Meta:
        verbose_name        = "Clínica"
        verbose_name_plural = "Clínicas"
        ordering            = ["no_fantasia"]
        indexes             = [
            models.Index(fields=['no_razao_social'], name='idx_clinica_razao'),
            models.Index(fields=['no_fantasia'],     name='idx_clinica_fant'),
        ]


# ============================================================
# 4) CBO
# ============================================================
class CBO(models.Model):
    cod_cbo       = models.CharField(max_length=10, primary_key=True)
    cod_cbo_label = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return f"{self.cod_cbo} - {self.cod_cbo_label}"

    class Meta:
        verbose_name        = "CBO"
        verbose_name_plural = "CBOs"
        ordering            = ["cod_cbo"]
        indexes             = [
            models.Index(fields=['cod_cbo_label'], name='idx_cbo_label'),
        ]


# ============================================================
# 5) CBO ESPECIALIDADE
# ============================================================
class CBOEspecialidade(models.Model):
    cbo                          = models.ForeignKey(
        CBO,
        on_delete    = models.CASCADE,
        related_name = "especialidades"
    )
    cod_cbo_especialidades_label = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.cbo.cod_cbo} - {self.cod_cbo_especialidades_label}"

    class Meta:
        verbose_name        = "Especialidade CBO"
        verbose_name_plural = "Especialidades CBO"
        ordering            = ["cod_cbo_especialidades_label"]
        unique_together     = ("cbo", "cod_cbo_especialidades_label")
        # unique_together já cria índice composto, então não precisa de outro.

# ============================================================
# 6) MEDICOS (novo modelo normalizado)
# ============================================================
class Medicos(models.Model):
    no_profissional    = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    nu_registro        = models.CharField(max_length=50,  null=True, blank=True)
    co_conselho_classe = models.CharField(max_length=50,  null=True, blank=True)
    sg_uf_crm          = models.CharField(max_length=2,   null=True, blank=True, db_index=True)
    nu_telefone        = models.CharField(max_length=50,  null=True, blank=True)

    cod_cbo = models.ForeignKey(
        CBO,
        on_delete    = models.SET_NULL,
        null         = True,
        blank        = True,
        related_name = "medicos"
    )

    clinica = models.ForeignKey(
        Clinica,
        on_delete    = models.SET_NULL,
        null         = True,
        blank        = True,
        related_name = "medicos"
    )

    def __str__(self):
        return self.no_profissional

    class Meta:
        db_table            = "medicos"
        verbose_name        = "Médico"
        verbose_name_plural = "Médicos"
        ordering            = ["no_profissional"]
        indexes             = [
            models.Index(fields=['no_profissional'], name='idx_medicos_nome'),
            models.Index(fields=['cod_cbo'],         name='idx_medicos_cbo'),
            models.Index(fields=['clinica'],         name='idx_medicos_clinica'),
        ]


# ============================================================
# 7) CONFIG (permanece)
# ============================================================
class Config(models.Model):
    backgroundfoto = models.BinaryField(blank=True, null=True)
    name           = models.CharField(max_length=255, blank=True, null=True)
    email          = models.CharField(max_length=255, blank=True, null=True)
    feedback       = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    comment        = models.TextField(blank=True, null=True)

    class Meta:
        db_table            = 'config'
        verbose_name        = 'Configuração'
        verbose_name_plural = 'Configurações'

    def __str__(self):
        return f"Config: {self.name}"


