from pages.interactions_page import SortablePage


class TestInteraction:

    class TestSortablePage:

        def test_sortable_list(self, driver):
            sortable_list_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_list_page.open()
            before, after = sortable_list_page.change_list_order()
            assert before != after, 'Что-то пошло не так'

        def test_sortable_grid(self, driver):
            sortable_grid_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_grid_page.open()
            before, after = sortable_grid_page.change_grid_order()
            assert before != after, 'Что-то пошло не так'
