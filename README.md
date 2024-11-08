# Déploiement d'une architecture Serverless avec CloudFormation

Ce projet vous guide à travers le déploiement automatisé d'une architecture **serverless** sur AWS en utilisant **CloudFormation Nested Stacks**. L'infrastructure inclut **DynamoDB**, **Lambda** et **API Gateway**, le tout orchestré via des templates CloudFormation.

## Architecture Déployée

L'architecture déployée comprend les ressources suivantes :

- **DynamoDB** : Une base de données NoSQL pour stocker des items.
- **Lambda** : Des fonctions serverless pour exécuter du code en réponse à des événements HTTP via l'API Gateway.
- **API Gateway** : Un service pour créer et gérer des API RESTful afin de communiquer avec les fonctions Lambda.

## Prérequis

- Un compte AWS
- AWS CLI configurée avec des permissions suffisantes pour déployer des stacks CloudFormation, créer des rôles IAM, et accéder à S3.
- Un éditeur de texte pour travailler sur les fichiers YAML de CloudFormation.

## Étapes de Déploiement

1. **Téléchargez les fichiers dans S3** : Téléchargez les templates CloudFormation et le code Lambda dans un bucket S3.
2. **Déployez la stack principale** : Utilisez AWS CLI pour déployer la stack principale avec la commande suivante :

   ```bash
   aws cloudformation create-stack --stack-name http-crud-main-stack --template-body file://./main.yaml --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
   ```
