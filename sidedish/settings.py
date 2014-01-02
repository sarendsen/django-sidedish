from django.conf import settings
from django.utils.translation import ugettext_lazy as _


SIDEDISH_SIDES = getattr(settings, 'SIDEDISH_SIDES', (
    ('left', _('Left')),
    ('right', _('Right')),
))

SIDEDISH_STATUS_DRAFT = getattr(settings, 'SIDEDISH_SIDES', 1)
SIDEDISH_STATUS_PUBLISHED = getattr(settings, 'SIDEDISH_SIDES', 2)
SIDEDISH_STATUS_CHOICES = getattr(settings, 'SIDEDISH_SIDES', (
    (SIDEDISH_STATUS_DRAFT, _("Draft")),
    (SIDEDISH_STATUS_PUBLISHED, _("Published")),
))
