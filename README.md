# Sudoku-CSP
Esercizio Sudoku CSP in Python.

### Domanda 1
___Quale dei 4 algoritmi funziona e quale no?___
- L'algoritmo di "_backtracking_search_" per tutte le 3 tipologie di Sudoku ha sempre trovato una soluzione. 
- L'algoritmo "_AC3_" ha trovato una soluzione solo al primo sudoku(quello più semplice).
- L'algoritmo "_min_conflicts_" non ha mai trovato una soluzione per i 3 sudoku, anche l'algoritmo "_depth_first_graph_search_" non ha mai trovato una soluzione, in particolare con il secondo sudoku va in esecuzione all'infinito.

### Domanda 2
___Che effetto produce la diversa configurazione delle euristiche per lo standard backtracking sul risultato? Quale di queste euristiche dovrebbe funzionare meglio per il sudoku? Quale combinazione di euristiche funziona meglio?___

- La migliore strategia per il sudoku è utilizzare il "_backtracking_" utilizzando "_minimum-remaining-values_" per velocizzare il processo, che sceglie la variabile con il dominio di cardinalità minore, utilizzare il "_forward_checking_" riducendo lo spazio di ricerca eliminando le opzioni che sono incompatibili con le assegnazioni correnti e effettuare l'ordinamento dei valori basato su una lista di valori vincolanti "_least_constraining_values_" (lcv).

- Sono state testate anche altre combinazioni con ricerca senza inferenza, "_select_unassigned_variable_" su "_first_unassigned_variable_" e "_order_domain_values_" su "_unordered_domain_values_".

- La migliore strategia risulta dopo vari test su tutte le combinazioni possibili, l'utilizzo della "_minimum-remaining-values_" e "_forward_checking_" e con ordinamento (least_constraining_values).

Qui sotto sono riportate alcune combinazioni, ordinate dal migliore peggiore risultato ottenuto:

- Soluzione sudoku 1  backtracking_search (con "minimum-remaining-values" , con "forward_checking", con "lcv")in : 0.002999544143676758
- Soluzione sudoku 1  backtracking_search (con "minimum-remaining-values" , con "forward_checking", con "unordered_domain_values")  in : 0.003003835678100586
- Soluzione sudoku 1  backtracking_search (con "first_unassigned_variable", con "lcv" e senza "forward_checking") in : 20.088945150375366

Tra le varia combinazione, la modifica che impatta di più è il "_forward_checking_".

### Domanda 3
___Valutare le performance dei vari casi in termini di tempo di esecuzione.___ 
I risultati in termini di tempo dei vari algoritmi utilizzando tutti i valori standard di default:
(select_unassigned_variable=first_unassigned_variable, order_domain_values=unordered_domain_values, inference=forward_checking):

SUDOKU 1
```
Fallito min_conflicts in :21.347442865371704
Fallito depth_first_graph_search in :33.18072533607483
Soluzione sudoku 1  AC3 in : 0.0060002803802490234
Soluzione sudoku 1  backtracking_search in : 0.0045087337493896484
```

SUDOKU 2
```
Fallito min_conflicts in :21.456703662872314
Fallito AC3 in :0.003999471664428711
Fallito depth_first_graph_search: Out of memory
Soluzione sudoku 2  backtracking_search in : 3.5277364253997803
```

SUDOKU 3
```
Fallito min_conflicts in :21.522000551223755
Fallito depth_first_graph_search in :203.44177293777466
Fallito AC3 in :0.005092144012451172 
Soluzione sudoku 3  backtracking_search in : 0.04404330253601074
```
