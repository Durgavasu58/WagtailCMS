from django import template

from wagtail.core.models import Page, Site
# from ..models import Menu

register = template.Library()

# @register.simple_tag()
# def get_menu(slug):
#     return Menu.objects.get(slug=slug)

@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return Site.find_for_request(context['request']).root_page

def has_menu_children(page):
    # This is used by the top_menu property
    # get_children is a Treebeard API thing
    # https://tabo.pe/projects/django-treebeard/docs/4.0.1/api.html
    return page.get_children().live().in_menu().exists()


def has_children(page):
    # Generically allow index pages to list their children
    return page.get_children().live().exists()


def is_active(page, current_page):
    # To give us active state on main navigation
    return (current_page.url_path.startswith(page.url_path) if current_page else False)


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent



@register.inclusion_tag('menus/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.localized.get_children().filter(
        live=True,
        show_in_menus=True
    )
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }



# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('menus/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent,sub=False, level=0, calling_page=None):
    menuitems_children = parent.localized.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    for menuitem in menuitems_children:
        menuitem.has_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url_path.startswith(menuitem.url_path)
                           if calling_page else False)
        menuitem.children = menuitem.get_children().live().in_menu()

        levelstr= "".join('a' for i in range(level)) # for indentation
        level += 1

    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        'sub': sub,
        'level':level,
        'levelstr':levelstr,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

