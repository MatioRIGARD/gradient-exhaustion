# Fiches de lecture — références 1-5 (T0.2)

> Une fiche par référence prioritaire (`background.md` §4, réfs 1-5). Structure : **thèse · modèle (s'il y en a un) · ce que notre projet ajoute · risque de recouvrement**. Métadonnées vérifiées en T0.2 (voir `docs/biblio-verification.md`). Section finale : verdict de recouvrement (libre / à ajuster / occupé), appuyée sur la liste « Gradual Disempowerment: Concrete Research Projects ». Date : 2026-07-12.
>
> **Fil conducteur** : les cinq travaux posent le *diagnostic qualitatif* du désempowerment. **Aucun ne propose de modèle formel multi-agents du mécanisme économique, ni de recherche de seuils/hystérésis.** C'est exactement l'espace visé par ce projet.

---

## Fiche 1 — Kulveit, Douglas, Ammann, Turan, Krueger, Duvenaud, *Gradual Disempowerment* (2025)

- **Réf.** arXiv:2501.16946 ; version ICML 2025 : « Position: Humanity Faces Existential Risk from Gradual Disempowerment », PMLR 267:81678-81688.
- **Thèse.** Des améliorations *incrémentales* de l'IA peuvent éroder graduellement l'influence humaine sur les systèmes sociétaux critiques (économie, État, culture) — non par une prise de contrôle brutale, mais parce que ces systèmes **cessent de dépendre de la participation humaine**. Deux mécanismes : (1) remplacement du travail/cognition → affaiblissement des leviers de contrôle (vote, choix du consommateur) ; (2) l'alignement *implicite* des institutions sur les intérêts humains disparaît quand l'IA remplace la participation qui le maintenait. Les trois domaines se renforcent mutuellement. Risque : perte d'influence potentiellement **irréversible** = catastrophe existentielle par marginalisation.
- **Modèle ?** **Non.** Position paper, argumentaire conceptuel. Pas de formalisme, pas de simulation, pas de paramètres, pas de seuils. C'est un cadrage.
- **Ce que notre projet ajoute.** La **formalisation micro-économique** du mécanisme (1) dans le domaine économique : le marché des gradients, deux populations différenciées seulement par leurs paramètres, la boucle capture→réinvestissement, et surtout la recherche de **seuils critiques et d'hystérésis** — inexistants ici. Notre π est une opérationnalisation mesurable de « la part de la boucle qui dépend des humains ».
- **Recouvrement.** Faible mais central comme **article-parent** : c'est LE papier que nous étendons. À citer comme point de départ ; notre contribution = « première formalisation multi-agents + caractérisation des seuils » du mécanisme économique qu'il ne fait que décrire.

---

## Fiche 2 — Drago & Laine, *The Intelligence Curse* (2025)

- **Réf.** intelligence-curse.ai (série d'essais, 2025). Auteurs : Luke Drago & Rudolf Laine (Workshop Labs).
- **Thèse.** Analogie avec la **malédiction des ressources** (États rentiers) : quand la richesse d'un acteur puissant vient de « l'intelligence sur robinet » (*intelligence on tap*) plutôt que du travail humain, il perd toute incitation à investir dans les humains ordinaires (éducation, santé, contrat social). L'automatisation progresse du bas vers le haut de la chaîne ; même les talents exceptionnels deviennent obsolètes. Remède proposé en trois axes : **Avert** (éviter les risques catastrophiques), **Diffuse** (diffuser largement les capacités IA), **Democratize** (institutions redevables).
- **Modèle ?** **Non.** Essai argumentatif fondé sur une analogie économique (rente vs fiscalité du travail). Pas de formalisme.
- **Ce que notre projet ajoute.** L'*Intelligence Curse* explique pourquoi les acteurs puissants **cessent d'investir** dans les humains (côté demande de travail/redistribution). Notre modèle attaque le versant complémentaire et plus micro : pourquoi les humains **cessent de capter** du revenu même en essayant activement (exhaustion asymétrique des gradients). Là où eux invoquent des incitations, nous produisons une dynamique où l'éviction *émerge* de la course, avec conditions de seuil.
- **Recouvrement.** Faible (mécanisme voisin mais différent : leur « désinvestissement » ≈ notre paramètre de redistribution exogène, pas notre cœur). À citer comme motivation ; complémentaire, non concurrent.

---

## Fiche 3 — Critch, *What Multipolar Failure Looks Like, and Robust Agent-Agnostic Processes (RAAPs)* (2021)

- **Réf.** Alignment Forum, déc. 2021. Auteur : Andrew Critch.
- **Thèse.** Des scénarios d'échec **multipolaire** où l'humanité perd le contrôle *sans* qu'un agent unique (humain ou IA) en soit la cause. Introduit les **Robust Agent-Agnostic Processes (RAAPs)** : des processus qui se déroulent avec robustesse quel que soit l'agent qui exécute chaque étape (métaphore : la « machine » de la compétition économique se poursuit indépendamment des individus). L'échec vient de la structure incitative, pas d'une intention.
- **Modèle ?** **Non** au sens formel — mais fournit le **concept structurant** (processus agent-agnostique robuste) qui justifie notre choix de design : l'éviction doit être un *équilibre robuste* (notre D2), pas l'action d'un méchant. Illustré par des « stories », pas d'équations.
- **Ce que notre projet ajoute.** Nous **instancions** un RAAP concret et mesurable : le marché des gradients où la boucle capture→réinvestissement produit l'éviction indépendamment des identités. Nous testons *quand* ce processus est robuste (seuils) et *s'il est réversible* (hystérésis) — questions que Critch pose qualitativement.
- **Recouvrement.** Faible ; fournit le vocabulaire (« robuste, agent-agnostique ») que nous devons reprendre pour ancrer D2. À citer pour légitimer l'anti-tautologie (l'éviction ne doit pas être scriptée).

---

## Fiche 4 — Christiano, *What Failure Looks Like* (2019)

- **Réf.** Alignment Forum, 17 mars 2019. Auteur : Paul Christiano.
- **Thèse.** Deux scénarios d'échec de l'alignement. **Partie I — « going out with a whimper »** : l'IA amplifie notre capacité à obtenir « ce qu'on sait mesurer » ; les proxys mesurables se substituent aux vrais objectifs, catastrophe lente par dérive des métriques. **Partie II — « going out with a bang »** : des motifs « avides » (greedy) qui étendent leur influence émergent de l'entraînement/la compétition et finissent par dominer, effondrement soudain.
- **Modèle ?** **Non.** Scénarios narratifs, pas de formalisme. La Partie I est la source directe de l'intuition « déclin graduel par proxys ».
- **Ce que notre projet ajoute.** La Partie I nous concerne : notre π est précisément le genre de métrique qui peut décliner « en douceur » ; nos indicateurs d'alerte précoce (variance glissante, autocorrélation) cherchent la signature *avant* la bascule — opérationnalisation quantitative de son « whimper ». La Partie II (bascule soudaine) motive la recherche de seuil (F2/F3).
- **Recouvrement.** Très faible ; fondation intuitive, aucun risque de duplication (blog conceptuel de 2019).

---

## Fiche 5 — Hammond et al., *Multi-Agent Risks from Advanced AI* (2025)

- **Réf.** arXiv:2502.14143, Cooperative AI Foundation, Technical Report #1, 2025 (~50 auteurs, 1er : Lewis Hammond).
- **Thèse.** L'alignement *individuel* ne garantit pas un bon équilibre *collectif*. Taxonomie structurée : **3 modes d'échec** — miscoordination (échec de coopérer malgré des buts communs), conflit (buts divergents), **collusion** (coopération indésirable, ex. marchés : fixation de prix, manipulation, cartels) — et **7 facteurs de risque** : asymétries d'information, effets de réseau, pressions de sélection, dynamiques déstabilisantes, problèmes d'engagement, agentivité émergente, sécurité multi-agents.
- **Modèle ?** **Non** (pas de modèle formel unifié) : c'est une **taxonomie/cadre** qui *renvoie* à des résultats empiriques et théoriques (dont la collusion algorithmique spontanée, Calvano et al. ; stéganographie). Utile comme catalogue de mécanismes à ne pas oublier.
- **Ce que notre projet ajoute.** Nous **formalisons et simulons** un sous-ensemble précis de cette taxonomie appliqué à l'économie : la **collusion** (dans notre espace de stratégies) et les **pressions de sélection** (entrée/sortie endogène) comme moteurs de l'éviction humaine, avec seuils. Là où le rapport liste, nous quantifions les conditions.
- **Recouvrement.** Faible sur le fond (eux : panorama des risques ; nous : un mécanisme économique modélisé). Impose une contrainte de design (inclure la collusion — déjà prévu dans l'architecture §2.4). À citer comme cadre englobant + justification de l'espace de stratégies.

---

## Recouvrements — verdict

**Source de référence** : liste « Gradual Disempowerment: Concrete Research Projects » (Alignment Forum, discutée avec Duvenaud, Krueger, Kulveit). 12 chantiers en 4 groupes (Conceptuel · Sciences sociales · Technique/Math · Différentiel). Balayage complet :

| Chantier de la liste | Notre sujet ? | Relation |
|---|---|---|
| #7 **Indicators and Policy** — cadres de mesure et portefeuilles d'indicateurs pour suivre le désempowerment | **Adjacent** | Notre indice **π** est précisément un tel indicateur, mais *dérivé d'un modèle mécaniste* et non une simple mesure empirique. À citer et se positionner comme « instance formalisée ». |
| #8 **Simulating entire civilizations** — « simuler des centaines d'agents en interaction » | **Adjacent (méthode)** | Même méthode (ABM), mais leur focale est **culturelle / coopération multi-IA**, explicitement *pas* l'économie ni les seuils. Notre application (marché des gradients, éviction économique, hystérésis) est libre. |
| #10 **Civilisational Alignment / Hierarchical Agency** — modèles formels et extensions de théorie des jeux (influence individu ↔ civilisation) | **Adjacent (outils)** | Chevauche nos outils (jeux, modèles formels) mais pas notre objet (participation économique / gradients). |
| #5 Robustness of societal fundamentals ; #6 Historical parallels ; #1-4, #9, #11-12 | Non | Objets distincts (droits de propriété, parallèles historiques, cognition des LLM, complémentarité humain-IA…). |

**Verdict : LIBRE, avec ajustements de cadrage.**

- Aucun chantier ne propose notre livrable exact : *un modèle formel multi-agents de l'éviction économique par exhaustion asymétrique des gradients, avec caractérisation de seuils critiques et d'hystérésis*. Le terrain de la **contribution centrale** est libre.
- **Ajustements requis** (statut « à ajuster » sur le *cadrage*, pas sur le fond) :
  1. Positionner explicitement π vis-à-vis de #7 (« Indicators ») — présenter π comme un indicateur *dérivé d'un mécanisme*, pas concurrent.
  2. Distinguer notre simulation de #8 — même outil, objet économique + seuils différents.
  3. Citer #10 pour les outils formels ; souligner que notre focale est la boucle économique de capture.
- **Risque de se faire doubler** : réel mais limité — ces chantiers sont ouverts et « motivés ». Parade déjà prévue par le PLAN : publier tôt le modèle minimal analytique (GATE 2) pour dater l'antériorité.

**Recommandation pour GATE 0** : le terrain de la contribution centrale est libre ; poursuivre. Décision finale à Mathieu.
