class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.right is not None:
                temp = temp.right
            temp.right = new_node
            new_node.left = temp

    
    def convert_array_to_doubly_linked_list(self, array, i=0):
        if i < len(array):
            self.insert_at_end(array[i])

            # Add left child if exists
            left_child_index = 2 * i + 1
            if left_child_index < len(array):
                self.left = Node(array[left_child_index])
                self.left.convert_array_to_doubly_linked_list(array, left_child_index)

            # Add right child if exists
            right_child_index = 2 * i + 2
            if right_child_index < len(array):
                self.right = Node(array[right_child_index])
                self.right.convert_array_to_doubly_linked_list(array, right_child_index)

    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

# # Example usage:
# array = [1, 2, 3, 4, 5, 6, 7]
# doubly_linked_list = Node(array[0])
# doubly_linked_list.convert_array_to_doubly_linked_list(array)
# doubly_linked_list.display()
