# Workshop : Construire une API CRUD simple avec AWS

Ce workshop explique comment créer une API CRUD (Create, Read, Update, Delete) de base en utilisant des services AWS tels que DynamoDB, Lambda et API Gateway. Au lieu de créer chaque ressource manuellement dans la console AWS, ce workshop utilise **AWS CloudFormation** pour automatiser la création de l'infrastructure. Vous apprendrez à écrire un template CloudFormation pour déployer une table DynamoDB, une fonction Lambda, et une API HTTP Gateway, le tout en une seule étape. Ce workshop est conçu pour les personnes ayant peu d'expérience avec AWS, mais étant à l'aise avec la ligne de commande (copier-coller autorisé !).

---

## Objectifs du Workshop

L’API finale inclura les composants suivants :

1. **Table DynamoDB** – Une base de données pour stocker les données.
2. **Fonction Lambda** – Une fonction serverless pour gérer les requêtes de l'API.
3. **API Gateway** – Une API HTTP pour router les requêtes vers la fonction Lambda.

### Architecture

- **Client** : Les requêtes client sont envoyées via l'API Gateway HTTP API.
- **API Gateway** : Route les requêtes HTTP vers la fonction Lambda.
- **Fonction Lambda** : Gère les opérations CRUD en interagissant avec DynamoDB, puis retourne une réponse à API Gateway.
- **DynamoDB** : Stocke et renvoie les données demandées par la fonction Lambda.

---

## Prérequis

- Un compte AWS avec les permissions pour créer et utiliser les services AWS (DynamoDB, Lambda, API Gateway, CloudFormation).
- Des connaissances de base en ligne de commande et en infrastructure-as-code avec CloudFormation.
- Un IDE installé localement pour rédiger et déployer les templates CloudFormation.

---

## Étapes du Workshop

### Étape 1 : Écrire un template CloudFormation pour la table DynamoDB

1. Rédiger un template CloudFormation définissant une table DynamoDB.
2. Inclure les clés de partition et de tri nécessaires aux opérations CRUD.

### Étape 2 : Ajouter une fonction Lambda dans le template

1. Définir une ressource Lambda dans le template CloudFormation.
2. Configurer les permissions de la fonction Lambda pour accéder à la table DynamoDB.

### Étape 3 : Ajouter l'API Gateway dans le template

1. Définir une API HTTP Gateway dans le template CloudFormation qui redirige les requêtes vers la fonction Lambda.
2. Configurer les routes et méthodes (GET, POST, PUT, DELETE) pour chaque opération CRUD.

### Étape 4 : Déployer le template CloudFormation

1. Utiliser la ligne de commande AWS CLI pour déployer le template CloudFormation et créer toutes les ressources.

---

## Test de l'API

Une fois l'API configurée et les ressources créées, elle peut être testée avec des outils comme **curl** ou **Postman** pour envoyer des requêtes HTTP. Voici des exemples de requêtes :

- **Create** : Envoyer une requête POST pour créer un nouvel élément dans DynamoDB.
- **Read** : Utiliser une requête GET pour récupérer des éléments de la table DynamoDB.
- **Update** : Envoyer une requête PUT pour modifier un élément existant.
- **Delete** : Envoyer une requête DELETE pour supprimer un élément.

---

## Démarrage rapide

Si vous êtes dans le cadre d'un événement AWS (re:Invent, ServerlessDays, Immersion Day, ou autre événement AWS), suivez les instructions sur le portail AWS Workshop.

Si vous suivez ce workshop de façon autonome, commencez directement en suivant les étapes ci-dessus pour déployer votre API CRUD en utilisant CloudFormation.
