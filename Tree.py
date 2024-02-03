class TreeNode:
    def __init__(self, data):
        self.data=data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level_of_tree(self):
        level = 0
        prnt=self.parent
        while prnt:
            level+=1
            prnt=prnt.parent
        return level


    def print_tree(self):
        spaces = ' ' * self.get_level_of_tree() * 3
        print(spaces + self.data)
        for child in self.children:
            child.print_tree()




root = TreeNode("Artificial Intelligence")
machine_learning = TreeNode("Machine Learning")
machine_learning.add_child(TreeNode("Linear Regression"))
machine_learning.add_child(TreeNode("K nearest neighbour"))
machine_learning.add_child(TreeNode("Naive Bayes"))
machine_learning.add_child(TreeNode("Clustering"))

deep_learning = TreeNode("Deep Learning")
deep_learning.add_child(TreeNode("Convolutional Neural Networks"))
deep_learning.add_child(TreeNode("Recurrent Neural Networks"))
deep_learning.add_child(TreeNode("Multilayer Perceptrons"))

computer_vision = TreeNode("Computer Vision")
computer_vision.add_child(TreeNode("Scale-Invariant Feature Transform"))
computer_vision.add_child(TreeNode("Canny Edge Detection"))
computer_vision.add_child(TreeNode("You Only Look Once"))

natural_language_processing = TreeNode("NLP")
natural_language_processing.add_child(TreeNode("Tokenization"))
natural_language_processing.add_child(TreeNode("Text Classification"))
natural_language_processing.add_child(TreeNode("Stemming"))

root.add_child(machine_learning)
root.add_child(deep_learning)
root.add_child(computer_vision)
root.add_child(natural_language_processing)
root.print_tree()
