from mezzanine import template
from mezzanine.utils.sites import current_site_id

from project.info.models import SitewideContent

register = template.Library()


@register.as_tag
def get_sitewide_content():
    """
    Adds the `SitewideContent` to the context
    """
    return SitewideContent.objects.get_or_create(site_id=current_site_id())[0]

