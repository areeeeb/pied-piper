class Node:
    def __init__(self,
                 frequency,
                 value=None,
                 left=None,
                 right=None,
                 is_leaf=False):
        """

        :type left: Node
        :type right: Node
        :type value: object
        :type frequency: int
        :type is_leaf: bool
        """
        self.left = left
        self.right = right
        self.value = value
        self.frequency = frequency
        self.is_leaf = is_leaf

    def __repr__(self):
        return f'Node(frequency: {self.frequency}, value: {self.value})'
