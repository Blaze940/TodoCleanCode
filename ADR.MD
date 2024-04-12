# Implementation de la TODODONE

### Statut : Proposé

### Contexte

> Nous avons besoin d'une architecture qui supporte l'application simple de gestion de nos TODO, qui doit être robuste, 
> maintenable et devrait fonctionner efficacement sans dépendances complexes.

### Decision

> Pour la mise en place de notre application nous avons donc décider d'adopter d'une architecture en couches. Celle-ci 
> séparera l'interface en ligne de commande, la logique de l'application, l'accès aux données, et le stockage.

### Raisonnement

> Nous avons choisi cette architecture car :
> - Faciliter les mises à jour et la correction de bugs.
> - Séparation des responsabilités.
> - Efficacité du développement.

### Implications

> - Structure Claire : Chaque couche a un rôle défini, rendant le système plus facile à comprendre et à maintenir.
> - Testabilité : Les couches individuelles peuvent être testées indépendamment.
> - Flexibilité : Les couches peuvent être modifiées indépendamment au fur à mesure que les exigences évoluent.

### Conclusion

> L'implémentation de cette application à été accepté par tous et après l'implémentation on peut voir tout les
> avantages que cela apporte au niveau de l'application.