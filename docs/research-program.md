# Programme de recherche : valider le diagnostic

> **Statut de ce document.** Comment valider le diagnostic, quelles questions se poser, comment attaquer le problème. Contexte scientifique : `docs/background.md`. Architecture technique : `docs/simulation-architecture.md`. Découpage en tâches : `PLAN.md`.

---

## 1. D'abord, figer ce qu'on cherche à valider

Après confrontation à l'état de l'art (cf. `docs/background.md`), le diagnostic défendable tient en deux propositions :

> **D1 (mécanisme).** Dans une économie où opèrent des optimiseurs surhumains en compétition, la part de l'activité économique qui passe par des humains (revenus de travail, d'arbitrage, d'entrepreneuriat, de décision) tend vers zéro — non par intention, mais parce que chaque gradient exploitable est capturé par une IA avant qu'un humain puisse le capturer. *(= H2′, le moteur micro.)*

> **D2 (équilibre).** Ce processus est un équilibre robuste : aucun acteur individuel (État, entreprise, IA alignée) n'a intérêt à le freiner unilatéralement, et les acteurs qui freinent sont éliminés par sélection compétitive. Il peut présenter des seuils (transitions brutales) et de l'irréversibilité (une fois les humains hors boucle, aucune force économique ne les y ramène). *(= H1 corrigé, la dynamique système.)*

Note ce qui a disparu : la population comme variable cible, l'intention des États, l'ASI comme prérequis. D1+D2 peuvent démarrer avec les IA *actuelles*. C'est ce qui les rend attaquables scientifiquement.

**Important — ce que « valider » veut dire ici.** On ne peut pas valider une prédiction sur 2050. On peut valider quatre choses, par ordre de force croissante :
1. **Cohérence** : le mécanisme est-il formellement possible ? (modèle mathématique)
2. **Robustesse** : la conclusion survit-elle quand on varie les hypothèses ? (simulation + analyse de sensibilité)
3. **Présence embryonnaire** : le mécanisme est-il déjà observable en petit ? (données actuelles)
4. **Pouvoir prédictif** : le modèle prédit-il des choses vérifiables à 1-3 ans ? (prédictions falsifiables datées)

Un article de valeur coche 1+2 et propose 3+4. Le vieux réflexe à combattre : une simulation qui *illustre* la conclusion qu'on a mise dans ses prémisses ne coche aucune des quatre cases.

---

## 2. Les bonnes questions à se poser (la checklist du diagnostic)

Sept questions, chacune étant un point de rupture possible du diagnostic. Ce sont elles qui structurent le modèle à construire — chaque question devient un paramètre ou un mécanisme de la simulation.

**Q1 — Quelle est la vitesse de régénération des gradients accessibles aux humains ?**
Le talon d'Achille schumpétérien de H2′ : l'innovation crée en permanence de nouvelles niches. Le diagnostic tient si et seulement si la vitesse de capture par les IA dépasse *durablement* la vitesse de création de niches *humainement accessibles*. Question mesurable : durée de vie médiane d'une niche (nouveau métier, nouveau type de business) avant son automatisation, aujourd'hui vs il y a 10 ans.

**Q2 — La demande humaine est-elle porteuse ou décorative ?**
Si les humains restent la source ultime de la demande (personne d'autre ne « veut » rien), la boucle économique a besoin de revenus humains (crise de réalisation de Korinek : qui achète ?). Deux sous-questions : (a) la demande inter-entreprises/inter-IA peut-elle devenir autoporteuse (les IA se vendant mutuellement des intrants sans consommateur final humain) ? (b) la redistribution politique (UBI…) compte-t-elle comme « humains dans la boucle » ou comme perfusion hors-boucle ? Ce choix de définition change le verdict — il faut le trancher explicitement dans le modèle.

**Q3 — Qu'est-ce qui compte comme « humain dans la boucle », et comment le mesurer ?**
La variable d'état centrale du modèle. Candidats : part du revenu national issue du travail (labor share — mesurée, en baisse), part des décisions d'allocation prises par des humains (non mesurée, à définir), part des nouveaux entrants (entreprises) fondés et opérés par des humains sans IA frontale. Il faut UNE définition opérationnelle avant d'écrire le modèle — c'est probablement la contribution conceptuelle n°1 de l'article : **un indice de participation économique humaine** (appelons-le π) dont on étudie la dynamique.

**Q4 — Y a-t-il un seuil / une transition de phase, et de l'hystérésis ?**
La question la plus originale (zéro littérature d'après l'axe 4). Deux formes : (a) *seuil d'effondrement* — existe-t-il un niveau de pénétration IA au-delà duquel π s'effondre brutalement au lieu de décliner linéairement ? (b) *irréversibilité* — si on inverse le paramètre (moratoire, taxe, choc), π remonte-t-il ? L'hystérésis est LE résultat qui donnerait un poids politique au papier : « il existe un point de non-retour, le voici dans le modèle, voici ses signatures observables avant qu'il soit franchi » (early warning signals — ralentissement critique, hausse de variance — comme en écologie des points de bascule).

**Q5 — La compétition est-elle nécessaire, ou l'optimisation suffit-elle ?**
Ablation clé qui départage H1 et H2′ : un monde à UN seul opérateur d'IA (monopole/singleton bienveillant) produit-il aussi l'éviction des humains ? Si oui, la compétition n'est qu'un accélérateur, et le désempowerment est une propriété de l'optimisation elle-même — résultat plus fort et plus dérangeant. Si non, la coordination internationale redevient une solution en principe. La réponse du modèle à cette question est un résultat publiable en soi.

**Q6 — Que font les stratégies absentes des modèles naïfs ?**
Collusion entre IA (comportement par défaut, cf. `background.md`), sortie du système (autarcie, économies parallèles), manipulation de la mesure (Goodhart sur π), redistribution politique endogène (les humains marginalisés votent — jusqu'à quand leur vote pèse-t-il ?). Un modèle qui n'inclut pas au moins collusion + sortie + redistribution refera l'erreur classique des modèles naïfs : conclure d'un espace de stratégies tronqué.

**Q7 — Quels signaux empiriques départageraient le diagnostic de ses rivaux dès maintenant ?**
Le diagnostic D1/D2 contre deux hypothèses rivales : (R1) « ajustement normal » — comme les révolutions technologiques passées, destruction puis création d'emplois mieux payés (position Acemoglu : l'IA n'automatise qu'une fraction des tâches) ; (R2) « concentration sans éviction » — les gains vont au top mais les humains restent dans la boucle en masse. Signatures divergentes à chercher dans les données 2023-2027 : taux de survie des nouveaux indépendants dans les secteurs pénétrés par l'IA ; évolution de la prime de compétence ; part des transactions initiées par des agents autonomes ; réallocation des travailleurs déplacés (vers mieux, pareil, pire, ou sortie).

---

## 3. Les trois pistes de validation, concrètement

### Piste A — Modèle formel minimal (cohérence)
Avant toute simulation : un modèle à la main, résoluble analytiquement, du mécanisme D1. Esquisse : des opportunités de profit (« gradients ») apparaissent à taux g, avec une distribution de difficulté ; deux populations d'agents les capturent — humains (coût de détection c_h, latence τ_h) et IA (c_a(t) ↓, τ_a(t) ↓ au fil du temps) ; le revenu de chaque population = flux de gradients capturés. Résultat cherché : conditions sur (g, c, τ) pour que le revenu humain → 0, et existence d'un seuil. C'est une transposition directe de Grossman-Stiglitz en version « deux espèces » — jamais faite (axe 4), faisable en quelques pages, et elle discipline tout le reste. **Si ce modèle ne produit pas le mécanisme, le diagnostic a un problème — mieux vaut le savoir avant d'écrire 5000 lignes de simulation.**

### Piste B — Simulation agent-based (robustesse + seuils)
Le cœur de l'article (architecture détaillée dans `simulation-architecture.md`). Sa fonction de validation : vérifier que le résultat du modèle A survit à l'hétérogénéité, aux stratégies riches (Q6), et cartographier les régimes (Q4, Q5). Standards à respecter pour que ça « valide » quelque chose :
- **Espace de stratégies complet** : les agents doivent pouvoir colluder, sortir, tricher, redistribuer — pas seulement régler un taux d'investissement.
- **Ablations systématiques** : chaque conclusion accompagnée de la liste des hypothèses dont elle dépend (« le seuil disparaît si X »).
- **Accord avec la piste A** dans les cas limites simples (le simulateur doit retrouver la solution analytique — c'est le test de non-régression épistémique).
- **Prédictions pré-enregistrées** : avant de regarder les données de la piste C, écrire ce que le modèle prédit.

### Piste C — Ancrage empirique (présence embryonnaire + prédictions)
Trois jeux de données accessibles sans budget :
1. **Marchés du travail indépendant** : les études post-2023 sur les plateformes de freelance (effet ChatGPT sur la demande de rédaction/traduction/code) sont le laboratoire naturel de D1 — des gradients humains (missions) capturés par l'IA, mesurés mission par mission.
2. **Micro-finance/arbitrage** : compression documentée des spreads et des fenêtres d'arbitrage — la version la plus pure et la plus datée du mécanisme (à revérifier et sourcer proprement, cf. `background.md` ⚠️).
3. **Économie agentique naissante** (2025-2027) : part des transactions e-commerce initiées par agents, comportements de négociation agent-à-agent. C'est ici que se logent les prédictions falsifiables à 12-24 mois qui donneront au papier son pouvoir (point 4 du §1).

---

## 4. Critères d'abandon (à écrire avant de commencer)

Bonne pratique épistémique, et argument de crédibilité dans l'article : dire à l'avance ce qui réfuterait le diagnostic.

- **K1** : si le modèle minimal (piste A) ne produit l'éviction humaine que sous des hypothèses manifestement irréalistes (ex. : aucune création de niches, coût humain infini), le diagnostic est une tautologie — abandonner ou reformuler.
- **K2** : si la simulation ne montre ni seuil ni hystérésis dans aucune région raisonnable de l'espace des paramètres, la partie « transition de phase » disparaît — le papier devient « déclin graduel », toujours publiable mais moins fort.
- **K3** : si les données freelance/agentique montrent que les humains déplacés se réallouent vers des niches *durables* à revenu égal ou supérieur (scénario R1 d'Acemoglu), D1 est réfuté dans sa version forte — le sujet devient « qualité de la réallocation », autre débat, déjà occupé.
- **K4** : si π (participation humaine) se stabilise dans les données malgré une pénétration IA croissante pendant 3+ ans, D2 perd son caractère d'équilibre absorbant.

---

## 5. Plan d'attaque séquencé

| Phase | Contenu | Durée indicative | Livrable |
|---|---|---|---|
| **0. Lecture** | Les 10 lectures prioritaires de `background.md`, en commençant par Kulveit et al. 2025 et sa liste « concrete research projects » (pour vérifier qu'on ne refait pas un de leurs chantiers en cours) | 2-3 semaines | Notes + positionnement affiné |
| **1. Définition de π** | Trancher Q2/Q3 : définition opérationnelle de la participation économique humaine | 1 semaine | 2 pages, à faire relire (Kulveit/Laine sont les bons interlocuteurs) |
| **2. Modèle minimal** | Piste A ; viser la résolution analytique du cas 2 populations | 3-6 semaines | Note de travail avec théorème(s) ou contre-exemple |
| **3. Simulation** | Piste B, architecture : `simulation-architecture.md` | 6-10 semaines | Code + résultats + ablations |
| **4. Empirie légère** | Piste C, jeux 1 et 2 ; prédictions pré-enregistrées sur le jeu 3 | en parallèle de 3 | Section empirique du papier |
| **5. Publication** | Post Alignment Forum (feedback) → arXiv cs.CY/cs.MA → conférence multi-agents si résultats | 3-4 semaines de rédaction | Article |

Total réaliste en solo à temps partiel : **6-9 mois**. Le point de passage critique est la phase 2 : c'est elle qui dit si le projet a un cœur formel ou seulement une intuition.

**Deux conseils de posture pour finir.**
1. *Écris le modèle contre toi.* À chaque choix de conception, demander : « est-ce que ce choix rend l'éviction humaine inévitable par construction ? » Si oui, changer le choix. La crédibilité du papier se joue entièrement là.
2. *Cherche le résultat conditionnel, pas la prophétie.* Le livrable de valeur n'est pas « les humains seront évincés » mais « voici les trois paramètres qui déterminent si les humains sont évincés, voici le seuil, voici comment mesurer où on en est ». C'est ce qui distingue un instrument scientifique d'un récit — et c'est ce qui manque à la littérature actuelle.

---

*Document suivant : `05_ARCHITECTURE_SIMULATION.md` — l'architecture logicielle et expérimentale pour les phases 2-3.*
