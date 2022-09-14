from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


class TestSortablePage:

    def test_sortable_list(self, driver):
        """ Тест сортировка элементов списка """
        sortable_list_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_list_page.open()
        before, after = sortable_list_page.change_list_order()
        assert before != after, 'fuck, the condom broke again!'

    def test_sortable_grid(self, driver):
        """ Тест сортировка элементов сетки """
        sortable_grid_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_grid_page.open()
        before, after = sortable_grid_page.change_grid_order()
        assert before != after, 'fuck, the condom broke again!'


class TestSelectablePage:

    def test_selectable_list_and_grid(self, driver):
        """ Тест выбора элемента в списке и сетке """
        selectable_list_page = SelectablePage(driver, 'https://demoqa.com/selectable')
        selectable_list_page.open()
        element_list, element_grid = selectable_list_page.check_selectable_list_and_grid()
        assert len(element_list) > 0, 'No elements were selected'
        assert len(element_grid) > 0, 'No elements were selected'


class TestResizablePage:

    def test_resizable(self, driver):
        """ Тест изменения размера боксов """
        resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
        resizable_page.open()
        max_box, min_box = resizable_page.check_size_resizable_box()
        max_size, min_size = resizable_page.check_size_resizable()
        assert 'width: 500px; height: 300px;' == max_box, 'maximum size noy equal to "500px", "300px"'
        assert 'width: 150px; height: 150px;' == min_box, 'maximum size noy equal to "150px", "150px"'
        assert max_size != min_size, 'resizable has not been changed'


class TestDroppablePage:

    def test_droppable_simple(self, driver):
        droppable_simple = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_simple.open()
        text = droppable_simple.check_droppable_simple()
        assert text == 'Dropped!', 'the element has not been dropped'

    def test_droppable_accept(self, driver):
        droppable_accept = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_accept.open()
        non_accept, accept = droppable_accept.check_droppable_accept()
        assert non_accept == 'Drop here', 'the dropped element has been accepted'
        assert accept == 'Dropped!', 'the dropped element has not been accepted'

    def test_droppable_prevent_propogation(self, driver):
        droppable_accept = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_accept.open()

    def test_droppable_revent_draggable(self, driver):
        droppable_accept = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_accept.open()
