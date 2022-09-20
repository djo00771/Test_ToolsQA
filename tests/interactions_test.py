from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage


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
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        text = droppable_page.check_droppable_simple()
        assert text == 'Dropped!', 'the element has not been dropped'

    def test_droppable_accept(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        non_accept, accept = droppable_page.check_droppable_accept()
        assert non_accept == 'Drop here', 'the dropped element has been accepted'
        assert accept == 'Dropped!', 'the dropped element has not been accepted'

    def test_droppable_prevent_propogation(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.check_droppable_propogation()
        assert not_greedy == 'Dropped!', 'the elements text has not been changed'
        assert not_greedy_inner == 'Dropped!', 'the elements text has not been changed'
        assert greedy == 'Outer droppable', 'the elements text has been changed'
        assert greedy_inner == 'Dropped!', 'the elements text has not been changed'

    def test_droppable_revent_draggable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        after_move, after_revert = droppable_page.check_revert_draggable('will')
        not_after_move, not_after_revert = droppable_page.check_revert_draggable('not_will')
        assert after_move != after_revert, 'The element has reverted'
        assert not_after_move == not_after_revert, 'The element has not reverted'


class TestDragabblePage:

    def test_dragabble_simple(self, driver):
        dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
        dragabble_page.open()
        before, after = dragabble_page.check_dragabble_simple()
        assert before != after, 'the position of the element has not changed'

    def test_restricted(self, driver):
        dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
        dragabble_page.open()
        before_x_top, after_x_top, before_y_left, after_y_left = dragabble_page.check_restricted()
        assert before_x_top == 'top: 0px', 'the position of the "top" has changed'
        assert after_x_top == 'top: 0px', 'the position of the "top" has changed'
        assert before_y_left == 'left: 0px', 'the position of the "left" has changed'
        assert after_y_left == 'left: 0px', 'the position of the "left" has changed'

    def test_container_restricted(self, driver):
        dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
        dragabble_page.open()
        pos_right = dragabble_page.check_container_restricted()
        assert pos_right == 'left: 698.005px; top: 107.005px', 'the position of the element outside the frame'
