from django.apps import AppConfig

# 修改organization显示为“机构管理”
class OrganizationConfig(AppConfig):
    name = 'organization'
    verbose_name = "机构管理"
