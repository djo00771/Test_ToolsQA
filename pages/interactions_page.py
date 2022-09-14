import random

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def change_list_order(self):
        """ Замена в списке элементов """
        self.is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_text_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.is_all_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_by_element(item_what, item_where)
        order_after = self.get_text_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        """ Замена в сетке элементов """
        self.is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_text_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.is_all_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_by_element(item_what, item_where)
        order_after = self.get_text_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def check_selectable_list_and_grid(self):
        """ Выбор элемента в списке и сетке """
        self.click(self.is_visible(self.locators.TAB_LIST))
        self.click_random_selectable_item(self.locators.LIST_ITEM)
        active_list_element = self.is_visible(self.locators.LIST_ITEM_ACTIVE).text
        self.click(self.is_visible(self.locators.TAB_GRID))
        self.click_random_selectable_item(self.locators.GRID_ITEM)
        active_grid_element = self.is_visible(self.locators.GRID_ITEM_ACTIVE).text
        return active_list_element, active_grid_element


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_max_min_size(self, element):
        """ Вернуть атрибут тега """
        size = self.is_visible(element)
        size_value = size.get_attribute('style')
        return size_value

    def check_size_resizable_box(self):
        """ Проверка изменения размера бокса с фиксированными значениями """
        self.action_drag_and_drop_by_offset(self.is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_max_min_size(self.locators.RESIZABLE_BOX)
        self.action_drag_and_drop_by_offset(self.is_present(self.locators.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_max_min_size(self.locators.RESIZABLE_BOX)
        return max_size, min_size

    def check_size_resizable(self):
        """ Проверка изменения размера бокса с произвольными значениями """
        self.action_drag_and_drop_by_offset(self.is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 200), random.randint(1, 200))
        max_size = self.get_max_min_size(self.locators.RESIZABLE)
        self.action_drag_and_drop_by_offset(self.is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_max_min_size(self.locators.RESIZABLE)
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def check_droppable_simple(self):
        drag_div = self.is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_by_element(drag_div, drop_div)
        return drop_div.text

    def check_droppable_accept(self):
        self.is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.is_visible(self.locators.ACCEPTABLE)
        not_acceptable_div = self.is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_by_element(not_acceptable_div, drop_div)
        drop_text_not_accept = drop_div.text
        self.action_drag_and_drop_by_element(acceptable_div, drop_div)
        drop_text_accept = drop_div.text
        return drop_text_not_accept, drop_text_accept
