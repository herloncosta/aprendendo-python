from database import init_db
from operations import add, edit, remove, list_one, list_completed, list_pending, list_all, mark_completed, mark_uncompleted


def main():
    init_db()

    # TODO: Criar menu de interação com o usuário, para interagir com as funções criadas.abs
    # Criar, editar, listar e excluir as tarefas

    # add("EstudarPython")
    # add("Ler livro")
    # add("Estudar IA")
    # add("Estudar JavaScript")


main()
