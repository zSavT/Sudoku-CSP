from csp import Sudoku, min_conflicts, AC3, backtracking_search, mrv, lcv, first_unassigned_variable, \
    unordered_domain_values, forward_checking, no_inference
from search import depth_first_graph_search
import time
import itertools
import threading
import sys


# Sudoku 3
def soluzione(sudo, n):
    tempoInizio = time.time()
    min_conflicts(sudo)
    tempoFine = time.time()
    if sudo.goal_test(sudo.infer_assignment()):
        print("Soluzione sudoku", n, " min_conflicts in :", tempoFine - tempoInizio)
        sudo.display(sudo.infer_assignment())
    else:
        print("Sudoku " + str(n) +
              " fallito min_conflicts in :" + str(tempoFine - tempoInizio) + " - Dominio: " + str(sudo.curr_domains))
        sudo.display(sudo.infer_assignment())

    tempoInizio = time.time()
    depth_first_graph_search(sudo)
    tempoFine = time.time()
    if sudo.goal_test(sudo.infer_assignment()):
        print("Soluzione sudoku", n, " depth_first_graph_search in :", tempoFine - tempoInizio)
        sudo.display(sudo.infer_assignment())
    else:
        print("Sudoku " + str(n) +
              " fallito depth_first_graph_search in :" + str(tempoFine - tempoInizio) + " - Dominio: " + str(
            sudo.curr_domains))
        sudo.display(sudo.infer_assignment())

    tempoInizio = time.time()
    AC3(sudo)
    tempoFine = time.time()
    if sudo.goal_test(sudo.infer_assignment()):
        print("Soluzione sudoku", n, " AC3 in :", tempoFine - tempoInizio)
        sudo.display(sudo.infer_assignment())
    else:
        print("Sudoku " + str(n) +
              " fallito AC3 in :" + str(tempoFine - tempoInizio) + " - Dominio: " + str(sudo.curr_domains))
        sudo.display(sudo.infer_assignment())

    tempoInizio = time.time()

    backtracking_search(sudo)

    tempoFine = time.time()
    if sudo.goal_test(sudo.infer_assignment()):
        print("Soluzione sudoku", n, " backtracking_search in :", tempoFine - tempoInizio)
        sudo.display(sudo.infer_assignment())
    else:
        print("Sudoku " + str(n) +
            " fallito backtracking_search in :" + str(tempoFine - tempoInizio) + " - Dominio: " + str(sudo.curr_domains))
        sudo.display(sudo.infer_assignment())

def soluzioneBacktracking(sudo,n):

    print("Seleziona la tipologia di ricerca per il paramentro \"select_unassigned_variable\":")
    print("\t1:first_unassigned_variable")
    print("\t2:mrv")
    scelta = int(input())
    match scelta:
        case 1:
            select = first_unassigned_variable
        case 2:
            select = mrv
        case _:
            select = first_unassigned_variable

    print("Seleziona la tipologia di ricerca per il paramentro \"order_domain_values\":")
    print("\t1:unordered_domain_values")
    print("\t2:lcv")
    scelta = int(input())
    match scelta:
        case 1:
            select2 = unordered_domain_values
        case 2:
            select2 = lcv
        case _:
            select2 = unordered_domain_values

    print("Seleziona la tipologia di ricerca per il paramentro \"inference\":")
    print("\t1:forward_checking")
    print("\t2:=no_inference")
    scelta = int(input())
    match scelta:
        case 1:
            select3 = forward_checking
        case 2:
            select3 = no_inference
        case _:
            select3 = forward_checking

    tempoInizio = time.time()

    backtracking_search(sudo, select_unassigned_variable=select, order_domain_values=select2, inference=select3)

    tempoFine = time.time()
    if sudo.goal_test(sudo.infer_assignment()):
        print("Soluzione sudoku", n, " backtracking_search in :", tempoFine - tempoInizio)
        sudo.display(sudo.infer_assignment())
    else:
        print("Sudoku " + str(n) +
              " fallito backtracking_search in :" + str(tempoFine - tempoInizio) + " - Dominio: " + str(
            sudo.curr_domains))
        sudo.display(sudo.infer_assignment())

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rIn esecuzione ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rTerminato!     ')


done = False
sudo1 = Sudoku('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
sudo2 = Sudoku('4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
sudo3 = Sudoku('1....7.9..3..2...8..96..5....53..9...1..8...26....4...3......1..4......7..7...3..')
print("Seleziona uno dei sudoku oppure inserisci 4 per personallizare la ricerca con il backtracking_search sul primo "
      "sudoku:")
print("Sudoku 1")
sudo1.display(sudo1.infer_assignment())
print("Sudoku 2")
sudo2.display(sudo2.infer_assignment())
print("Sudoku 3")
sudo3.display(sudo3.infer_assignment())
print("Seleziona:>")
scelta = int(input())
t = threading.Thread(target=animate)
if scelta == 1:
    t.start()
    soluzione(sudo1, 1)
elif scelta == 2:
    t.start()
    soluzione(sudo2, 2)
elif scelta == 3:
    t.start()
    soluzione(sudo3, 3)
elif scelta == 4:
    soluzioneBacktracking(sudo1,1)
else:
    print("Errore")
done = True
