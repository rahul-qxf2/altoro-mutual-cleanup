"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Altoro Mutual Main Page
"""

from page_objects.zero_mobile_page import Zero_Mobile_Page
from page_objects.zero_page import Zero_Page
from page_objects.altoro_mutual_main_page import Altoro_Mutual_Main_Page
import conf.base_url_conf


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=conf.base_url_conf.base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name in ["zero","zero page","agent zero"]:
            test_obj = Zero_Page(base_url=base_url)
        elif page_name in ["zero mobile","zero mobile page"]:
            test_obj = Zero_Mobile_Page()
        elif page_name=="altoro_mutual_main_page":
            test_obj = Altoro_Mutual_Main_Page(base_url=base_url)
        return test_obj

    get_page_object = staticmethod(get_page_object)