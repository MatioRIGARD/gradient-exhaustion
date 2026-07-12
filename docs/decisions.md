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

## Comment trancher les prochains arbitrages (heuristiques, dans l'ordre)

1. **Anti-tautologie d'abord** : rejeter toute option qui transforme la conclusion en définition (dans un sens ou dans l'autre). En cas de doute : la distinction va dans une *définition de mesure* + une *série de sortie* qui garde l'alternative observable — jamais dans une règle du modèle.
2. **Rendre le diagnostic plus difficile à confirmer, pas plus facile.** Entre deux options défendables, choisir celle qui donne le plus de chances aux humains dans le modèle. Un résultat négatif obtenu contre un modèle charitable est publiable ; un résultat positif obtenu contre un modèle chargé ne l'est pas.
3. **Préférer l'option qui garde une correspondance avec des données réelles mesurables** (comptes nationaux, plateformes, marchés).
4. **Préférer l'option la plus simple qui préserve les figures F1-F6.** L'information supplémentaire va dans des séries de sortie, pas dans la complexité des indices de tête.
5. **Documenter ici** (DEC-00N : question, décision, justification, conséquence papier), puis continuer. Signaler la décision à Mathieu dans le résumé de fin de tâche — il peut toujours la révoquer.

**À remonter systématiquement à Mathieu (ne pas trancher seul)** : les GATES de PLAN.md ; tout ce qui touche le positionnement public (titre, claims de l'abstract, où/quand publier, contacts extérieurs) ; tout élargissement de périmètre ; toute dépense.
