import random
import time

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragabblePageLocators
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

    def check_droppable_propogation(self):
        self.is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.is_visible(self.locators.GREEDY_INNER_BOX)
        self.action_drag_and_drop_by_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drag_and_drop_by_element(drag_div, greedy_inner_box)
        text_greedy_box = self.is_visible(self.locators.GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    def check_revert_draggable(self, type_drag):
        drags = {
            'will': {'revert': self.locators.WILL_REVERT},
            'not_will': {'revert': self.locators.NOT_REVERT}
        }
        self.is_visible(self.locators.REVERT_TAB).click()
        revert = self.is_visible(drags[type_drag]['revert'])
        drop_div = self.is_visible(self.locators.REVERT_DROP_BOX)
        self.action_drag_and_drop_by_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert


class DragabblePage(BasePage):
    locators = DragabblePageLocators()

    def get_dragabble_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(100, 200), random.randint(100, 200))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(100, 200), random.randint(100, 200))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    def check_dragabble_simple(self):
        self.is_visible(self.locators.SIMPLE_TAB).click()
        drug_div = self.is_visible(self.locators.DRAG_DIV)
        before_position, after_position = self.get_dragabble_position(drug_div)
        return before_position, after_position

    def check_restricted(self):
        self.is_visible(self.locators.RESTRICTED_TAB).click()
        restricted_x = self.is_visible(self.locators.RESTRICTED_X)
        before_x, after_x = self.get_dragabble_position(restricted_x)
        restricted_y = self.is_visible(self.locators.RESTRICTED_Y)
        before_y, after_y = self.get_dragabble_position(restricted_y)
        return before_x[-9:-1], after_x[-9:-1], before_y[-22:-13], after_y[-22:-13]

    def check_container_restricted(self):
        self.is_visible(self.locators.CONTAINER_RESTRICTED_TAB).click()
        drag_div = self.is_visible(self.locators.RESTRICTED_DIV)
        self.action_drag_and_drop_by_offset(drag_div, 720, 120)
        pos_right = drag_div.get_attribute('style')
        return pos_right[-32:-1]
