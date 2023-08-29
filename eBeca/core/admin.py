from django.contrib import admin

from core.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

# Criando inline para adicionar informações adicionais sobre o usuário na
# página de usuários do admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class AccountUserAdmin(AuthUserAdmin):
    # Apenas a view de alterar o usuário deve ter os inlines
    # Pois o inline causa um erro na add_view, pois o UserProfile só é criado depois do user
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AccountUserAdmin, self).add_view(*args, **kwargs)
    
    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super(AccountUserAdmin, self).change_view(*args, **kwargs)

    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, AccountUserAdmin)