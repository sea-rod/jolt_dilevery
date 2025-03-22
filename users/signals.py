from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser


@receiver(post_migrate)
def create_roles_and_permissions(sender, **kwargs):
    """Create roles and assign permissions after migration."""
    user_types = ["admin_1", "admin_2", "admin_3", "shop", "delivery"]

    for user_type in user_types:
        group, _ = Group.objects.get_or_create(name=user_type)

    # Define specific permissions
    affliated_admin = ["change_user", "view_user"]
    shop_perms = ["view_products", "add_products"]
    delivery_perms = ["view_orders"]

    permissions = {
        "affliated_admin": affliated_admin,
        "shop": shop_perms,
        "delivery": delivery_perms,
    }

    for role, perms in permissions.items():
        group = Group.objects.get(name=role)
        for perm in perms:
            permission, _ = Permission.objects.get_or_create(
                codename=perm,
                name=f"Can {perm}",
                content_type=ContentType.objects.get_for_model(CustomUser),
            )
            group.permissions.add(permission)
