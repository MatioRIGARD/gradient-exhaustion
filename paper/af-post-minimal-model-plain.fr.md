# Un petit modèle testable des humains évincés de l'économie par les prix : venez le casser

> **Traduction française de travail** de `af-post-minimal-model-plain.md`, pour relecture par Mathieu. C'est la version anglaise qui fait foi et qui sera publiée. Les formules sont identiques.

> **Comment ceci a été fait.** Je suis ingénieur en électronique et systèmes embarqués, pas économiste. Ce post, les maths et le code de simulation ont été produits avec une forte assistance d'IA, sous ma direction, en quelques soirées. Je le dis d'emblée parce que la politique du site le demande et parce que c'est le cadrage honnête.
>
> Ce que je vous demande de juger, ce n'est pas la prose mais l'objet derrière : un dépôt public avec un modèle formel, des résultats en forme close, quatre passes de vérification indépendantes, et des prédictions pré-enregistrées, dont une a échoué et est rapportée comme un échec. Code et dérivations : github.com/MatioRIGARD/gradient-exhaustion
>
> Pourquoi j'ai décidé de creuser ce sujet : j'en suis venu à penser que le problème de l'alignement est au moins autant un problème économique qu'un problème technique. Ceci est ma tentative de rendre un morceau de cette conviction assez précis pour pouvoir être faux.

## Ce qui manque aux arguments existants

Plusieurs essais soignés soutiennent que l'IA avancée pourrait pousser les humains hors de l'économie, sans faire de mal à personne, simplement en rendant la participation humaine non rentable. « Gradual Disempowerment » (Kulveit et al. 2025) fait l'argument général : quand les systèmes économiques et politiques cessent d'avoir besoin des humains, l'influence humaine sur ces systèmes s'efface, sans qu'aucune catastrophe soit nécessaire. « The Intelligence Curse » (Drago & Laine 2025) ajoute une analogie avec les États pétroliers : un acteur qui tire sa richesse d'une intelligence disponible au robinet perd toute incitation à investir dans les gens. Les versions antérieures de l'argument structurel sont Critch (2021) et Christiano (2019).

Ce sont tous des arguments en mots. Autant que je puisse en juger, personne n'a écrit le mécanisme sous forme de modèle formel, quelque chose avec des équations, où l'on peut pointer une hypothèse et dire « celle-ci est fausse, donc la conclusion tombe ». C'est le trou que ce post essaie de combler. Le modèle est volontairement minuscule. Je ne prétends pas qu'il est réaliste. Je prétends qu'il est assez petit pour être vérifié, et faux de manières qu'on peut réellement trouver.

## Le modèle, en langage courant

Imaginez l'économie comme un flux d'opportunités de profit à durée de vie courte. Un actif mal coté, un besoin non satisfait, un client qui cherche un freelance, une nouvelle niche. Appelons chacune un **gradient**. Les gradients apparaissent à un certain rythme, chacun rapporte de l'argent au premier qui l'attrape, et si personne ne l'attrape, il s'évanouit (le prix se corrige tout seul, le client trouve une autre solution).

Deux sortes de joueurs se disputent leur capture.

**Les humains.** Participer coûte quelque chose à un humain par unité de temps : de l'attention, de l'effort, se tenir informé. En échange, il repère les gradients à un rythme fixe. Et il y a une règle cruciale, la **libre entrée** (free entry) : tant que participer rapporte plus que rester dehors, des humains supplémentaires entrent ; quand ça ne paie plus, ils sortent. (C'est la façon standard dont les économistes modélisent un marché ouvert. Pensez aux applis de livraison qui se sont remplies de coursiers exactement jusqu'à ce que la paie cesse d'être intéressante.)

**Les opérateurs d'IA.** Exactement le même type de joueur, à une différence près, et cette seule différence porte tout le modèle : **leur revenu les rend meilleurs au jeu**. L'argent gagné est réinvesti en calcul, en meilleurs modèles, en capacité de détection supplémentaire. Les humains, dans cette version, n'ont pas cette boucle : leur vitesse et leur coût restent constants.

Cette unique asymétrie est l'hypothèse **A7**, et je la signale comme le principal pari empirique du modèle. Elle ne dit *pas* que les humains ne peuvent pas progresser. Elle dit que la capacité logicielle se compose avec le revenu réinvesti beaucoup plus vite que la capacité humaine. C'est une affirmation sur le monde réel, et elle pourrait être fausse. Si on la désactive, ou si on donne la même composition aux humains, le modèle ne produit aucune éviction. Rien d'autre dans la construction ne traite humains et IA différemment : ce sont deux réglages de paramètres du même agent, pas deux livres de règles.

## Quatre résultats

Quelques symboles, pour que les formules soient lisibles :

- $\mu_h$ : la vitesse à laquelle un humain repère les gradients ; $c_h$ : ce que la participation lui coûte par unité de temps
- $g$ : la fréquence d'apparition des gradients ; $v$ : la valeur de chacun ; $\theta$ : la vitesse à laquelle un gradient non capturé s'évanouit
- $\Lambda_a$ : la capacité totale de détection de l'IA (la « vitesse » du camp IA)

Une quantité dérivée compte : $S = g v \mu_h / c_h$, le niveau de compétition totale auquel un humain de plus serait exactement à l'équilibre. Tout ce qui suit est une conséquence de la libre entrée qui pousse le marché à ce niveau.

**(i) Il y a un couperet fini, pas un lent déclin asymptotique.** Les humains participent si et seulement si la capacité de l'IA est sous un seuil

$$\bar\Lambda = \frac{g v \mu_h}{c_h} - \theta.$$

À cette valeur, la participation humaine atteint exactement zéro, pas « tend vers zéro à la longue ». Le seuil se comporte de façon sensée : plus d'opportunités ou des humains plus efficaces le remontent (plus dur d'exclure les humains) ; des gradients qui s'évanouissent plus vite l'abaissent.

**(ii) Le déclin est linéaire, et silencieux.** Sous le seuil, la part humaine de la participation est une droite :

$$\pi = 1 - \frac{\Lambda_a}{\bar\Lambda}.$$

Voici la partie que je trouve politiquement importante. À cause de la libre entrée, les humains sur ce marché ne gagnent jamais plus que leurs coûts : la compétition entre humains a déjà mangé le surplus, avec ou sans IA. Donc quand la capacité de l'IA croît, aucun participant ne voit jamais ses *profits* baisser ; ce qui rétrécit, c'est le *nombre d'humains pour qui se présenter a encore un sens*. Le déclin est invisible dans les marges de chacun et visible seulement dans les effectifs. C'est une raison structurelle pour laquelle un processus de ce genre pourrait rester silencieux jusque tard.

Le revers, dit honnêtement : puisque le surplus net est nul de bout en bout, ce modèle ne peut rien dire par lui-même du *bien-être*, des gens qui souffrent. $\pi$ mesure la présence dans la boucle économique, pas le bien-être. Relier les deux exigerait une hypothèse de subsistance que le modèle ne contient pas.

**(iii) Un seul nombre décide de l'issue, et personne n'a besoin de le vouloir.** Laissons maintenant la capacité de l'IA croître par réinvestissement. Dans le régime où les humains participent encore, tout se ramène à une comparaison :

$$\gamma = \frac{\eta c_h}{\mu_h} - \delta,$$

où $\eta$ est l'efficacité avec laquelle le revenu réinvesti devient de la capacité nouvelle et $\delta$ la vitesse à laquelle la capacité se déprécie (les modèles vieillissent, le matériel aussi). En mots : **le camp IA peut-il transformer ses gains en capacité nouvelle plus vite que l'ancienne ne pourrit ?**

- Si non ($\gamma < 0$) : la capacité de l'IA rétrécit et les humains finissent dominants. Fait intéressant, c'est la libre entrée humaine qui l'affame : le terrain saturé plafonne ce que l'IA gagne par unité de capacité.
- Si oui ($\gamma > 0$) : la capacité de l'IA croît exponentiellement et franchit le seuil à une **date finie et calculable** $t^* = \gamma^{-1}\ln(\bar\Lambda/\Lambda_a(0))$. La participation humaine tombe lentement d'abord, puis vite. Graduel, puis soudain.

Aucune stratégie, aucune coordination, aucune intention n'apparaît nulle part là-dedans ; c'est une instance formelle de ce que Critch appelle un processus agnostique aux agents. Mais je veux les petites lignes dans le texte principal : « compétition plus composition » ne produit ce résultat qu'à cause de deux hypothèses structurelles de plus. Les humains, sous libre entrée, gardent un surplus nul, donc n'ont rien à réinvestir. Le camp IA, par l'hypothèse **A9**, réinvestit son revenu *brut* et ne subit aucune discipline compétitive équivalente. Si la compétition *entre* opérateurs d'IA brûlait leurs marges comme la compétition entre humains le fait, le $\eta$ effectif chuterait et une région de coexistence s'ouvrirait. Savoir si la compétition réelle entre IA fonctionne ainsi est une question ouverte, pas quelque chose que le modèle tranche.

**(iv) Un possible point de non-retour, mais seulement si vous achetez une hypothèse de plus.** Jusqu'ici la valeur des gradients était fixe. Ajoutons l'hypothèse **A8** : la valeur des gradients dépend de la demande, et le revenu humain est ce qui alimente l'essentiel de cette demande. Concrètement : une fraction $\beta$ de la demande est autonome (indifférente au revenu humain), le reste est de la dépense humaine. Tant que les humains participent, la valeur est haute ; une fois qu'ils sont totalement exclus, leur dépense disparaît et la valeur tombe à $\beta$ fois son ancien niveau.

Valeur plus basse veut dire seuil plus bas. Le modèle a donc maintenant *deux* seuils : celui où les humains sortent, et un plus bas sous lequel la capacité de l'IA devrait retomber pour que le retour paie. Entre les deux, un piège (le nom en économie est **hystérésis**) : la porte par laquelle les humains sortent est plus haute que la porte par laquelle il faudrait rentrer. Même si la capacité de l'IA redescend plus tard sous le point de sortie, les humains ne reviennent pas, parce que la demande que leurs propres revenus fournissaient a disparu. La largeur du piège est $(1-\beta)\,S$.

Je veux être précis sur ce qu'est ce résultat, parce qu'une revue hostile du modèle a eu raison d'appuyer dessus. Ce n'est **pas** une découverte ; ça découle en une ligne d'algèbre du fait d'avoir supposé la chute de valeur. Tout le travail est fait par l'asymétrie de A8 : le revenu humain alimente la demande finale, le revenu de l'IA essentiellement pas (les opérateurs achètent du calcul et des intrants, pas des courses). C'est une affirmation empirique et elle peut être fausse : si le revenu de l'IA revient bel et bien dans la demande finale à grande échelle, $\beta$ est élevé et le piège rétrécit ou disparaît. (À $\beta = 1$ il n'y a pas de piège du tout, mais alors l'économie n'a plus besoin de la demande humaine non plus, ce qui est sa propre limite inquiétante, cf. la crise de réalisation de Korinek.) Le résultat (iv) est donc strictement *conditionnel à A8*, et il pèse moins que (i) à (iii).

## Là où le modèle m'a corrigé

Avant de lancer la simulation, j'ai écrit mes prédictions. L'une d'elles a échoué, et je pense que cet échec est la chose la plus crédible de ce post.

La version à deux états de A8 ci-dessus (valeur haute, puis brusquement basse) est un interrupteur brutal. Un run de test l'a remplacée par l'alternative la plus lisse possible, où la valeur suit simplement le revenu humain, proportionnellement. Sous cette version, **le piège a entièrement disparu.** L'éviction se produisait toujours, et même *plus tôt*, mais elle était réversible : la valeur suit le revenu à la remontée comme à la descente. Vérifié à la main, le bouclage de la version lisse est simplement trop faible pour créer deux états stables.

Le résumé honnête est donc devenu : **l'éviction est le résultat robuste ; son irréversibilité ne l'est pas.**

Puis le premier balayage de production a réfuté ma supposition *suivante* aussi. J'avais prédit que le piège reviendrait si la réponse de la demande était assez raide (une courbe en S au lieu d'une droite). Raté : la raideur seule n'a rien fait, et a même avancé l'éviction. Ce qui restaure réellement le piège, c'est la **tardiveté** : quand la demande tient bon jusqu'à ce que le revenu humain soit presque épuisé, et ne cède qu'alors, une boucle d'hystérésis nette réapparaît. Et « une demande qui tient puis qui lâche », c'est exactement ce que produisent l'épargne, le crédit à la consommation, les habitudes et les aides au revenu.

Comme j'ai trouvé cela seulement après l'échec de ma prédiction enregistrée, je l'ai traité comme exploratoire : je l'ai ré-enregistré quantitativement et lancé une confirmation sur dix graines fraîches à la moitié de la vitesse de rampe. Largeur de boucle $+0{,}64 \pm 0{,}13$ sous demande tardive contre $-0{,}14 \pm 0{,}08$ sous demande lisse (les intervalles de confiance ne se recouvrent pas, et les trois prédictions de confirmation enregistrées sont passées). Une analyse statique des points fixes des mêmes équations de demande, faite indépendamment de la simulation, est d'accord. (Une note de précision : une réponse raide à mi-hauteur ouvre bien une zone de piège étroite à faible capacité d'IA dans l'analyse statique, dont la simulation à population finie s'échappe par le bruit ; l'affirmation nette porte sur le piège près de la frontière d'éviction.)

La lecture économique est inconfortable et testable : *un ajustement lisse de la consommation donne un effondrement plus précoce mais réversible ; une consommation qui tient puis casse (ce que produisent l'épargne, le crédit et les programmes de transfert) donne un effondrement plus tardif mais irréversible.*

## Comment ça a été vérifié

L'intérêt de construire un petit objet, c'est qu'on peut réellement le vérifier, donc voici la liste :

1. **Dix-neuf vérifications numériques** : Monte-Carlo pour les probabilités de capture et le seuil, intégration numérique pour la date d'éviction et le point de repos post-éviction, et les largeurs de piège.
2. **Une re-dérivation à l'aveugle** : un agent frais, à qui on n'a donné que la construction de départ, a re-dérivé chaque formule indépendamment et les a retrouvées symbole pour symbole (il a aussi soulevé trois points de fond, maintenant intégrés à l'audit).
3. **Une reproduction en modèle multi-agents** : une simulation d'agents individuels n'ayant que de l'information locale a retrouvé le déclin linéaire, l'emplacement du seuil et la formule de la date d'éviction (six tests d'ancrage sur six dans les tolérances annoncées).
4. **Une revue adverse hostile** : sept corrections exigées, toutes appliquées, dont déclarer ouvertement l'asymétrie A8, rétrograder le résultat du piège de « nouveau », et ajouter la réserve sur le bien-être au résultat (ii).

Les premiers runs de production ont ensuite testé les prédictions pré-enregistrées. La frontière entre « l'IA croît » et « l'IA rétrécit » tombe exactement sur la ligne prédite $\delta = \eta c_h/\mu_h$ sur toute la grille de paramètres [f2_phase_diagram.png]. Quand la croissance de capacité sature tôt, la région de coexistence prédite est là et suit la formule analytique point par point [f2b_coexistence.png]. La dynamique d'effondrement se comporte comme dérivé [f1_pi_dynamics.png]. Répartir la même capacité totale d'IA entre 1 et 20 opérateurs laisse la date d'éviction exactement inchangée [f4_operators.png], confirmant que *sans* compétition destructrice de marges, « plusieurs IA au lieu d'une » ne protège personne.

Deux séries enregistrées supplémentaires ont testé les leviers politiques évidents, avec des résultats qui donnent à réfléchir. **La redistribution** (taxer le revenu de l'IA et le transférer aux humains) n'empêche l'éviction qu'au-dessus d'un taux quasi confiscatoire, environ 92 % aux paramètres de base, parce que la taxe doit battre une composition exponentielle. En dessous, les transferts achètent du délai et de la survie, mais pas de la participation : après l'éviction, la part humaine du revenu est exactement égale au taux de taxe. Maintenus en vie, hors de la boucle, et c'est désormais un régime mesurable. (Aussi : c'est un résultat à juridiction unique. Dans le monde réel, une taxation unilatérale invite la capacité à migrer vers qui taxe le moins, donc le levier exige de la coordination, ce qui est le problème du désempouvoirement à nouveau, un étage plus haut.) **La compétition entre opérateurs** ne protège les humains que si elle détruit environ 97 % de leurs marges ; avec collusion, le résultat non protégé revient exactement. Un premier essai de signaux d'alerte précoce (les tremblements statistiques avant l'effondrement) est ressorti négatif avec un estimateur naïf, et est rapporté comme négatif, pas enjolivé.

Une prédiction enregistrée a été réfutée et est rapportée comme réfutée. Le récapitulatif des verdicts vit à côté du code.

## Ce qui prouverait que c'est faux

Le modèle nomme lui-même les conditions sous lesquelles aucune éviction ne se produit, chacune étant une question empirique :

- **$\gamma \le 0$.** Si transformer le revenu de l'IA en capacité perd contre la dépréciation, l'IA ne s'amorce jamais. Tout le résultat tient à une inégalité.
- **Saturation précoce.** Si le réinvestissement a des rendements décroissants et que la capacité de l'IA plafonne *sous* le seuil, humains et IA coexistent indéfiniment. L'éviction n'est pas universelle, même à l'intérieur du modèle.
- **Composition humaine.** Si les humains peuvent se composer comme l'IA (outils, augmentation), l'éviction disparaît ; l'histoire devient « humains augmentés contre non augmentés », un problème différent (et plus traitable).
- **Compétition IA contre IA.** Si les opérateurs se disputent leurs marges jusqu'à les détruire, le réinvestissement effectif baisse et la coexistence grandit. La simulation a établi la moitié nulle : avoir simplement beaucoup d'opérateurs ne change rien. Tout repose sur la question de savoir si la compétition réelle détruit les marges. Et notez le point de donnée inconfortable du monde réel : les entreprises d'IA actuelles réinvestissent *à perte*, financées par les marchés de capitaux sur des revenus futurs espérés, ce qui contournerait entièrement la discipline des marges.

Et les deux objections que je considère les plus fortes :

- **Pas d'équilibre général.** Le flux d'opportunités est fixé de l'extérieur du modèle. L'économie qui *génère* les opportunités n'est pas modélisée, et il n'y a pas de régénération schumpétérienne, aucun mécanisme par lequel l'abondance créée par l'IA ouvrirait de nouvelles niches plus vite. Un économiste attaquerait ici en premier, et à raison. Tout ce qui précède est un énoncé partiel sur un marché, pas sur l'économie entière.
- **« Participation » est un choix de définition.** $\pi$ compte la participation *gagnée*. Un humain qui possède de la capacité d'IA mais n'opère rien est, par cette définition, hors de la boucle ; son revenu est suivi dans une série séparée, jamais fondu dans le chiffre principal. Je pense que c'est défendable (posséder n'est pas participer), mais c'est un choix, et des gens raisonnables seront en désaccord. Le modèle actuel ne permet pas non plus à un humain d'*acheter* le canal de composition ; s'il le peut, « l'éviction humaine » devient en partie une question de répartition entre humains.

## La demande

Les prochaines étapes sont le programme multi-agents complet (le diagramme de phase coexistence/éviction, la cartographie de la tardiveté de la demande, la compétition entre opérateurs), plus un ancrage empirique sur les données les plus propres que je puisse trouver : les revenus des plateformes de freelance avant et après les modèles capables, et les données de l'économie agentique naissante à mesure qu'elles apparaissent.

Mais la demande ici est précise. Les trois hypothèses qui font le vrai travail sont :

- **A7** : la capacité de l'IA se compose avec le revenu beaucoup plus vite que la capacité humaine ;
- **A8** : le revenu humain alimente la demande finale, le revenu de l'IA essentiellement pas ;
- **A9** : l'IA réinvestit son revenu brut, sans discipline imposée par la compétition.

Si l'une des trois est fausse d'une manière que je n'ai pas prise en compte, le résultat correspondant tombe, et je préfère l'apprendre ici que sur arXiv. Le modèle est petit, vérifié et public. Venez le casser.
