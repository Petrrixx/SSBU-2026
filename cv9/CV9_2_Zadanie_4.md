## Zadanie 4 (5b)

V tomto zadaní budete pracovať s nástrojom MetaboAnalyst a datasetom: **NMR spectral bins**
    
`Binned 1H NMR spectra of 50 urine samples using 0.04 ppm constant width (Psihogios NG, et al.) Group 1- control; group 2 - severe kidney disease.`
    
Tento dataset je dostupný v sekcii 'Try our test data' v nástroji pre Jednofaktorovú štatistickú analýzu. 

Dataset pochádza z NMR-metabolomickej štúdie: Hodnotenie závažnosti tubulointersticiálnych lézií u pacientov s glomerulonefritídou. Začiatok tubulointersticiálnych lézií je charakterizovaný zníženým vylučovaním citrátu, hipurátu, glycínu a kreatinínu, zatiaľ čo po ďalšom zhoršení nasleduje glykozúria, selektívna aminoacidúria, úplné vyčerpanie citrátu a hipurátu a postupné zvyšovanie vylučovania laktátu, acetátu a trimetylamín-N-oxidu. Metabonomická analýza moču založená na NMR by mohla prispieť k včasnému hodnoteniu závažnosti poškodenia obličiek a prípadne k monitorovaniu ich funkcie. [1]


Načítajte množinu údajov v nástroji MetaboAnalyst. Pri filtrovaní údajov (Data filter) môžete použiť predvolené nastavenia.

### Úloha 1 (1b)

Normalizujte distribúciu datasetu (pre premenné aj vzorku).
(Vyberte akúkoľvek kombináciu operácií, ktorá je podľa Vás najlepšia).

**Ktoré operácie ste pri normalizácii použili?**

*Pokus 1:*
- Sample normalization: None
- Data Transformation: Log transformation (base 2)
- Data Scaling: Auto scaling
- *Výsledok:* Hustota pravdepodobnosti (density plot) sa celkom pekne vyrovnala bližšie k normálnemu rozdeleniu. Pred normalizáciou boli dáta kvôli silným extrémom (ako napr. Bin.4.06) potlačené k nule. Aplikovaná transformácia a škálovanie centrovali priemery premenných na nulu, no v boxplotoch stále ostalo na koncoch pomerne dosť odľahlých hodnôt (outlierov).

*Pokus 2 (Finálny výber):*
- Sample normalization: Normalization by sum
- Data Transformation: Log transformation (base 10)
- Data Scaling: Pareto scaling
- *Výsledok:* Normalizácia podľa súčtu (sum) výborne kompenzovala rozdiely v zriedení močových vzoriek. Logaritmická transformácia (base 10) a Pareto scaling vytvorili krásnu, hladkú zvonovú krivku (ukážkové normálne rozdelenie). Boxploty sú stabilné, centrované okolo nuly s plynulou varianciou naprieč binnami bez zbytočného zveličenia šumu. Tento stav je pre ďalšiu analýzu ideálny.

*Finálny výber:*
Sample normalization: Normalization by sum
Data Transformation:  Log transformation (base 10)
Data Scaling:         Pareto scaling

### Úloha 2 (4b)

Použite ľubovoľné štatistické metódy na analýzu datasetu (napr. t-test, correlations, PCA, PLS-DA, Dendrogram, Heatmap, K-means, RandomForest, ..) 

**Uveďte aspoň 4 skutočnosti (z 4 rôznych metód), ktoré ste zistili analýzou datasetu:**

1: T-test (unpaired, unequal variance) identifikoval spolu 95 signifikantných premenných pri zvolenom p-value threshold, čo naznačuje výrazné rozdiely medzi kontrolnou skupinou a skupinou so závažným ochorením obličiek.
2: PCA pairwise score plot pre top 5 hlavných komponentov ukazuje zreteľné oddelenie kontrolnej skupiny a pacientov najmä na osiach PC1 a PC2, pričom PC1 vysvetľuje 32 % variability a PC2 ďalších 14 %.
3: PLS-DA pairwise score plot pre top 5 komponentov ešte výraznejšie oddeľuje kontrolnú skupinu od pacientov; Component 1 vysvetľuje 20.5 % a Component 2 ďalších 21.7 % variability, čo potvrdzuje dobrú diskriminačnú silu modelu.
4: Hierarchické zhlukovanie (Hierarchical Clustering) vizualizované heatmapou top 25 premenných jasne rozdeľuje vzorky do dvoch klastrov podľa skupiny: kontrolná skupina sa charakterizuje nižšími hodnotami metabólitov (modrá), zatiaľ čo pacientska skupina má vyššie hodnoty (červená), čo potvrdzuje výrazne metabolické rozdiely medzi skupinami.

Report z analýzy je vložený do priečinku cv9 - Analysis Report.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions’ severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
