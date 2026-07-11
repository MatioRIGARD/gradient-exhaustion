# Journal des décisions de design

> Registre des arbitrages de fond. **Agents : consultez ce fichier avant de poser une question d'arbitrage à Mathieu.** Si un arbitrage nouveau se présente, appliquez d'abord les heuristiques du §« Comment trancher » ; ne remontez à Mathieu que ce qui change la nature du projet (périmètre, positionnement public, GATES de PLAN.md).

---

## DEC-001 — L'actionnaire passif est hors de π_marché, avec reporting séparé (2026-07-12)

**Question.** Comment π traite-t-il un humain vivant des dividendes d'une firme-IA sans l'opérer ?

**Décision.** Option « hors boucle » : le revenu de capital passif ne compte ni dans π_marché ni dans le canal travail/capture. Il est compté dans π_total (canal perfusion) **et reporté en série de sortie séparée** dans toutes les expériences (distinct des transferts publics type UBI), afin que la question « la propriété du capital IA protège-t-elle ? » reste analysable dans les figures.

**Justification.** (a) π mesure la *participation* — être nécessaire au flux — pas les *droits sur* le flux ; un claim passif n'a de valeur que si des institutions l'exécutent, ce qui est précisément la variable que le diagnostic interroge (cadrage rentier de l'Intelligence Curse). (b) Anti-tautologie : c'est un choix de *classification des flux*, pas une règle du modèle — les humains peuvent posséder du capital IA dans la simulation, et le reporting séparé permet de *montrer* empiriquement le destin des mondes « actionnaires » au lieu de le décréter par définition. (c) Correspondance données réelles conservée : le revenu de capital des ménages est mesuré dans les comptes nationaux.

**Conséquence pour le papier.** La section limites doit expliciter ce choix et présenter la lecture alternative (option « dans la boucle ») avec la série séparée à l'appui.

---

## Comment trancher les prochains arbitrages (heuristiques, dans l'ordre)

1. **Anti-tautologie d'abord** : rejeter toute option qui transforme la conclusion en définition (dans un sens ou dans l'autre). En cas de doute : la distinction va dans une *définition de mesure* + une *série de sortie* qui garde l'alternative observable — jamais dans une règle du modèle.
2. **Rendre le diagnostic plus difficile à confirmer, pas plus facile.** Entre deux options défendables, choisir celle qui donne le plus de chances aux humains dans le modèle. Un résultat négatif obtenu contre un modèle charitable est publiable ; un résultat positif obtenu contre un modèle chargé ne l'est pas.
3. **Préférer l'option qui garde une correspondance avec des données réelles mesurables** (comptes nationaux, plateformes, marchés).
4. **Préférer l'option la plus simple qui préserve les figures F1-F6.** L'information supplémentaire va dans des séries de sortie, pas dans la complexité des indices de tête.
5. **Documenter ici** (DEC-00N : question, décision, justification, conséquence papier), puis continuer. Signaler la décision à Mathieu dans le résumé de fin de tâche — il peut toujours la révoquer.

**À remonter systématiquement à Mathieu (ne pas trancher seul)** : les GATES de PLAN.md ; tout ce qui touche le positionnement public (titre, claims de l'abstract, où/quand publier, contacts extérieurs) ; tout élargissement de périmètre ; toute dépense.
