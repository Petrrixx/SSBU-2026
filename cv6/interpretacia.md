# Interpretacia - Peter Bolecek

AI usage note:
Copilot was used only for support purposes, such as brainstorming implementation options, explaining ML libraries and methods, understanding teacher requirements, and planning the work before coding.

## Odpovede na zadanie

### Uloha 1 - Pouzity model a parametre
Bol doplneny model Random Forest.

Pouzity Grid Search:
- n_estimators: [100, 200, 300]
- max_depth: [None, 5, 10]
- min_samples_split: [2, 5]
- max_features: ["sqrt", "log2"]

### Uloha 2 - Doplnena metrika
Bola doplnena metrika Recall.

Recall je zapisovany do CSV logu a zaroven bol pridany do grafov:
- density graf pre recall
- priebeh recall cez replikacie

### Uloha 3 - Ukladanie grafov
Vsetky grafy sa ukladaju do priecinka outputs/plots.

### Uloha 4 - Zvyseny pocet replikacii a interpretacia
Pocet replikacii bol nastaveny na 12.

Suhnne vysledky (mean/std):
- Logistic Regression:
  - Accuracy: 0.9749 / 0.0070
  - F1 Score: 0.9755 / 0.0069
  - Recall: 0.9808 / 0.0118
  - ROC AUC: 0.9957 / 0.0024
- Random Forest:
  - Accuracy: 0.9633 / 0.0115
  - F1 Score: 0.9630 / 0.0125
  - Recall: 0.9580 / 0.0182
  - ROC AUC: 0.9941 / 0.0029

Interpretacia:
Logistic Regression dosiahol lepsie priemerne vysledky vo vsetkych sledovanych metrikach ako Random Forest. Najvacsi prakticky prinos je pri Recall, kde Logistic Regression lepsie zachytava pozitivnu triedu. Z grafov v priebehu cez replikacie je vidiet aj mensi rozptyl pri Logistic Regression =  stabilnejsie spravanie modelu.

## Linky na vystupy

### Logy a tabulkove vysledky
- [Application log](machine_learning/outputs/application.log)
- [Model accuracies CSV](machine_learning/outputs/model_accuracies.csv)

### Vygenerovane grafy
- [Density Accuracy](machine_learning/outputs/plots/density_accuracy.png)
- [Density F1 Score](machine_learning/outputs/plots/density_f1_score.png)
- [Density Recall](machine_learning/outputs/plots/density_recall_score.png)
- [Density ROC AUC](machine_learning/outputs/plots/density_roc_auc.png)
- [Replications Accuracy](machine_learning/outputs/plots/replications_accuracy.png)
- [Replications Recall](machine_learning/outputs/plots/replications_recall.png)
- [Confusion Matrix Logistic Regression](machine_learning/outputs/plots/confusion_matrix_logistic_regression.png)
- [Confusion Matrix Random Forest](machine_learning/outputs/plots/confusion_matrix_random_forest.png)

## Link na hlavny skript
- [Main script](machine_learning/main.py)
