class BinaryTree:
    #el constructor del arbol necesita el valor del nodo e identificarlos 
    #subarbol
    def __init__(self, value ):
        self.value = value 
        self.left_node = None
        self.right_node = None

    #insertar un nodo en el arbol
    def insert(self, root, node):
        #si no existe raiz en el arbol
        if root is None:
            root = node
        else:
            #si el valor del nodo es que el valor de la raiz
            if root.value > node.value:
                #si no existe nodo izquierdo
                if root.left_node is None:
                    root.left_node = node
                else:
                    #si existe el nodo izquierdo
                    self.insert(root.left_node, node)
            else:
                if root.right_node is None:
                    root.right_node = node
                else:
                    self.insert(root.right_node, node)
    
    def print_tree(self, root):
        #valor menor | raiz |valor mayor|
        if root is not None:
            self.print_tree(root.left_node)
            print(root.value)
            self.print_tree(root.right_node)



""" class BinaryTree:
    #El constructor del arbol necesita el valor del nodo e indentificar el subarbol
    def __init__(self,value):
        self.value= value
        self.left_node = None
        self.right_node = None

    #Insertar un nodo en el arbol
    def insert(self,root,node):
        #Si no existe raiz en el arbol
        if root is None:
            root = node
        else:
            #Si el valor del nodo es menor que la raiz
            if root.value > node.value:
                #Si no existe el nodo izquierdo
                if root.left_node is None:
                    root.left_node = node
                else:
                    #Si existe nodo izquierdo se inserta en el subarbol izquierdo
                    self.insert(root.left_node,node)
            else:
                #Si no existe nodo derecho
                if root.right_node is None:
                    root.right_node = node
                else:
                    #Si existe nodo derecho, se inserta en el subarbol derecho
                    self.insert(root.right_node, node)

    def print_tree(self,root):
        #Valor menor | raiz | valor mayor
        if root is not None:
            self.print_tree(root.left_node)
            print(root.value)
            self.print_tree(root.right_node) """
        


