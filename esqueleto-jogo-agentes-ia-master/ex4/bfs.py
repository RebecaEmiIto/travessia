from node import Node

"""
public String bfs() {

        if (self.root == null) {
            return "";
        }
        Queue<Node> fila = new LinkedList<>();
        fila.add(self.root);

        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("[");
        while (!fila.isEmpty()) {
            Node aux = fila.remove();

            stringBuilder.append(" " + aux + " ");

            if (aux.getLeft() != null) {
                fila.add(aux.getLeft());
            }

            if (aux.getRight() != null) {
                fila.add(aux.getRight());
            }
        }

        stringBuilder.append("]");
        return stringBuilder.toString();

    }


    public String dfs() {

        if (self.root == null) {
            return "";
        }
        Stack<Node> pilha = new Stack();
        pilha.add(self.root);

        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("[");
        while (!pilha.isEmpty()) {
            Node aux = pilha.pop();

            stringBuilder.append(" " + aux + " ");

            if (aux.getLeft() != null) {
                pilha.push(aux.getLeft());
            }

            if (aux.getRight() != null) {
                pilha.push(aux.getRight());
            }
        }

        stringBuilder.append("]");
        return stringBuilder.toString();
"""
class Arvore_bfs():
    def bfs():
        root = Node.__init__()