// ---------- MAIN ---------- //
#include <cctype>
#include <cstdlib>
#include <iostream>
using namespace std;
#define TMAX 10

typedef struct sLiv {
    string titulo, autor, isbn;
    int qtde, emprestados;
} Livro;
typedef struct sEmp {
    string matricula, isbn, data;
} Emprestimo;

void ordenar(Livro[], int);
void cont0();
string lerIsbn();
void adicionarLivro(Livro[], int &);
void consulta(Livro[], int);
void exclusao(Livro[], int &);
void emprestimo(Livro[], Emprestimo[], int &, int &);
void devolucao(Livro[], Emprestimo[], int &, int);
void relatorio1(Livro[], int);
void relatorio2(Emprestimo[], int);

int main() {
    int cont = 0, contE = 0;
    char continuar, opcao;
    Livro livros[TMAX];
    Emprestimo emprestados[TMAX];

    do {
        system("cls");
        cout << "Titulos cadastrados: " << cont << endl;
        cout << "Opcao 1: Inclusao de um novo livro/titulo" << endl;
        cout << "Opcao 2: Consulta a um livro" << endl;
        cout << "Opcao 3: Exlusao de um livro" << endl;
        cout << "Opcao 4: Emprestimo de um exemplar" << endl;
        cout << "Opcao 5: Devolucao de um exemplar" << endl;
        cout << "Opcao 6: Relatorio1 (livros do acervo)" << endl;
        cout << "Opcao 7: Relatorio2 (emprestados ativos)" << endl;
        cout << "Opcao 8: Sair" << endl;
        cout << "Informe a opcao: ";
        do {
            opcao = cin.get();
            if (opcao < '1' or opcao > '8')
                cout << "Digite um numero dentro do intervalo 1-8" << endl;
        } while (opcao < '1' or opcao > '8');
        system("cls");
        switch (opcao) {
        case '1':
            adicionarLivro(livros, cont);
            ordenar(livros, cont);
            break;

        case '2':
            consulta(livros, cont);
            break;

        case '3':
            exclusao(livros, cont);
            ordenar(livros, cont);
            break;

        case '4':
            emprestimo(livros, emprestados, contE, cont);
            break;

        case '5':
            devolucao(livros, emprestados, contE, cont);
            break;

        case '6':
            relatorio1(livros, cont);
            break;

        case '7':
            relatorio2(emprestados, contE);
            break;
        }

        do {
            cout << "Pressione ENTER para continuar: ";
            continuar = cin.get();
        } while (continuar != '\n');
    } while (opcao != '8');
    cout << "Saindo..." << endl;
}