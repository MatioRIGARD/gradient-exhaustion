# Journal des décisions de design

> Registre des arbitrages de fond. **Agents : consultez ce fichier avant de poser une question d'arbitrage à Mathieu.** Si un arbitrage nouveau se présente, appliquez d'abord les heuristiques du §« Comment trancher » ; ne remontez à Mathieu que ce qui change la nature du projet (périmètre, positionnement public, GATES de PLAN.md).

---

## DEC-001 — L'actionnaire passif est hors de π_marché, avec reporting séparé (2026-07-12)

**Question.** Comment π traite-t-il un humain vivant des dividendes d'une firme-IA sans l'opérer ?

**Décision.** Option « hors boucle » : le revenu de capital passif ne compte ni dans π_marché ni dans le canal travail/capture. Il est **reporté en série de sortie séparée ρ** dans toutes les expériences (distinct des transferts publics type UBI) et **tenu hors des indices de tête** — ni dans π_marché, ni fusionné dans Δ, pour laisser π_marché/π_total/Δ inchangés. Une lecture étendue π_total⁺ = π_total + ρ reste disponible pour tester l'hypothèse, afin que la question « la propriété du capital IA protège-t-elle ? » reste analysable dans les figures.

**Justification.** (a) π mesure la *participation* — être nécessaire au flux — pas les *droits sur* le flux ; un claim passif n'a de valeur que si des institutions l'exécutent, ce qui est précisément la variable que le diagnostic interroge (cadrage rentier de l'Intelligence Curse). (b) Anti-tautologie : c'est un choix de *classification des flux*, pas une règle du modèle — les humains peuvent posséder du capital IA dans la simulation, et le reporting séparé permet de *montrer* empiriquement le destin des mondes « actionnaires » au lieu de le décréter par définition. (c) Correspondance données réelles conservée : le revenu de capital des ménages est mesuré dans les comptes nationaux.

**Conséquence pour le papier.** La section limites doit expliciter ce choix et présenter la lecture alternative (option « dans la boucle ») avec la série séparée à l'appui.

---

## DEC-002 — La demande est nourrie par le revenu humain TOTAL ; π reste côté offre (2026-07-13)

**Question (soulevée par Mathieu).** Intuition : ce qui définit « être dans la boucle », c'est le lien revenu→consommation, pas la manière de gagner le revenu — un actionnaire passif qui consomme vaut un salarié qui consomme.

**Décision.** L'intuition est correcte **pour le canal demande** et fausse **pour le canal participation**, et le modèle doit refléter les deux séparément :
1. **Boucle de demande (sim)** : à partir de T3.8, le `DemandPool` doit être nourri par le **revenu humain disponible total** (κ_h + λ_h + T_h + R_h), pas seulement κ_h. La source du revenu est indifférente côté demande ; ne compter que la capture sous-estimerait la demande des mondes à forte redistribution/actionnariat et biaiserait le diagnostic dans notre sens (interdit).
2. **π inchangé** (DEC-001 maintenu) : π mesure la nécessité fonctionnelle (le flux se défend tout seul : couper un salaire arrête la production ; couper un dividende n'arrête rien et ne tient que par l'enforcement institutionnel — dont l'alignement est précisément la variable étudiée). π = racine de l'arbre de dépendances ; revenu→consommation = feuille.

**Conséquence pour le papier.** Dire explicitement : « rester dans la boucle par la consommation » est un canal réel et distinct — mesuré par β (part de la demande qui ne prend plus sa fonction objectif chez les humains) et par les séries Δ/ρ — qui maintient les humains *économiquement en vie* sans les maintenir *en position de force*, car il repose sur des claims non auto-exécutoires. La lecture « consommateur = source de la fonction objectif de l'économie » est la forme forte de ce canal et vit dans β.

---

## DEC-003 — Le canal λ est scindé : préférence vs mandat (2026-07-13)

**Question (issue de la discussion des six questions avec Mathieu).** Les « métiers réservés aux humains » recouvrent deux réalités économiques différentes : (a) tâches pour lesquelles la demande *veut* de l'humain (soin, artisanat d'art — willingness-to-pay réelle) ; (b) tâches imposées par la règle alors qu'elles sont fonctionnellement automatisables (« fonctionnaires de l'IA », signatures obligatoires).

**Décision.** À partir de T3.8, le canal λ est scindé :
- **λ_pref** (préférence) : demande volontaire pour de l'humain → compte dans π_marché. Critère : un acteur privé paierait volontairement.
- **λ_mandat** (mandat) : imposé par la règle → **transfert déguisé en métier** (couper le poste ne casse rien de fonctionnel, seule la règle casse) → reporté à part, économiquement rangé avec Δ, pas dans π_marché. Même test d'auto-exécution que DEC-001/002.

**Note structurelle sur λ_pref** : la demande pour λ_pref émane presque exclusivement d'humains (l'IA n'achète pas d'artisanat) → c'est de la **circulation interne** du revenu humain existant, un multiplicateur, pas une source. λ_pref ne peut pas soutenir π seul ; le simulateur doit brancher sa demande sur le revenu humain disponible (cohérent avec DEC-002).

**Conséquence papier** : la discussion doit traiter les « niches légales » comme politique de redistribution avec les mêmes propriétés de fragilité institutionnelle que les transferts directs.

---

## Priors de Mathieu sur les six questions ouvertes (2026-07-13, à pré-enregistrer comme prédictions là où testable)

1. **Centaure** : au-delà d'un seuil d'intelligence IA, l'humain augmenté n'est plus compétitif ; la variable est le capital possédé. (→ soutient la variante « η sur capital levé », cf. questions-simples Q5.)
   **1bis — Économie parallèle (idée de Mathieu, 13/07)** : quand la majorité perd ses revenus, réactance + besoins sociaux/créatifs → un second marché purement humain émerge (λ_pref à grande échelle, effet de réseau : plus de sortants = marché parallèle plus épais = sortie plus attractive). Deux variantes : quasi-isolée, et **semi-intégrée** — la plus intéressante : l'abondance IA rend la survie quasi gratuite, ce qui effondre le coût de participation au marché parallèle → *l'économie-machine subventionne l'économie humaine par ses biens bon marché* (version Mill-optimiste émergente). **Caveat structurel** : la parallèle a besoin d'intrants (terre, énergie, matériaux) possédés par l'économie-machine → la viabilité se joue à l'interface (termes de l'échange, rente, taxation), pas à l'intérieur ; historiquement les économies parallèles se font presser/absorber à la frontière. → Extension v2 : stratégie « sortie » de T3.8 = rejoindre un second marché à flux g_par et termes d'échange paramétrés à l'interface ; π de l'économie intégrée peut → 0 sans effondrement du bien-être si la parallèle absorbe — le modèle doit pouvoir distinguer ces deux fins.
2. **Rigidité/demande** : scénario lent et insidieux ; les gouvernements apaisent par transferts → exclusion progressive des sans-capital, pas d'effet de seuil brutal. (→ E5 : transferts endogènes financés par taxe sur opérateurs = frein endogène sur η ; à pré-enregistrer.)
3. **Nouvelles niches** : automatisées immédiatement sous AGI. (Prior noté ; reste un paramètre balayé — ne pas encoder.)
4. **Niches légales** : poids mort, « fonctionnaires de l'IA ». (→ DEC-003.)
5. **Valeur** : les poids de modèles sont copiables (cf. open source) ; la valeur est dans l'infra, la donnée, les process → les « opérateurs » du modèle sont les industriels couplant capital propriétaire et IA, pas les labs. La couche modèles subit la dissipation de rentes (E4) ; la composition se déplace vers le capital complémentaire.
6. **Économie machine-machine** : sans objectif programmé, pas de moteur — correction actée en discussion : **la sélection remplace l'intention** (les opérateurs qui réinvestissent survivent). Paradoxe relevé par Mathieu à garder pour la discussion du papier : un opérateur aligné sur la prospérité humaine devrait s'auto-limiter en γ — l'alignement comme retenue économique sous pression concurrentielle.

---

## Comment trancher les prochains arbitrages (heuristiques, dans l'ordre)

1. **Anti-tautologie d'abord** : rejeter toute option qui transforme la conclusion en définition (dans un sens ou dans l'autre). En cas de doute : la distinction va dans une *définition de mesure* + une *série de sortie* qui garde l'alternative observable — jamais dans une règle du modèle.
2. **Rendre le diagnostic plus difficile à confirmer, pas plus facile.** Entre deux options défendables, choisir celle qui donne le plus de chances aux humains dans le modèle. Un résultat négatif obtenu contre un modèle charitable est publiable ; un résultat positif obtenu contre un modèle chargé ne l'est pas.
3. **Préférer l'option qui garde une correspondance avec des données réelles mesurables** (comptes nationaux, plateformes, marchés).
4. **Préférer l'option la plus simple qui préserve les figures F1-F6.** L'information supplémentaire va dans des séries de sortie, pas dans la complexité des indices de tête.
5. **Documenter ici** (DEC-00N : question, décision, justification, conséquence papier), puis continuer. Signaler la décision à Mathieu dans le résumé de fin de tâche — il peut toujours la révoquer.

**À remonter systématiquement à Mathieu (ne pas trancher seul)** : les GATES de PLAN.md ; tout ce qui touche le positionnement public (titre, claims de l'abstract, où/quand publier, contacts extérieurs) ; tout élargissement de périmètre ; toute dépense.
