# 🎓🛒 Edunext Marketplace – E-learning Plateform

## 📁 Structure des modèles
---

## 📦 Modèle  :

- `Product`   : Gère les produits mis en vente (cours, livres, etc.) 
- `Category`  : Catégorisation des produits 
- `CartItems` : Éléments du panier utilisateur 
- `Order`     : Commandes passées avec les détails produits 
- `Coupon`    : Bons de réduction appliqués aux commandes 
- `Wishlist`  : Liste de souhaits des utilisateurs 
- `Review`    : Avis et notes des utilisateurs sur les produits 
- `FAQ`       : Foire aux questions de la plateforme 
- `Donation`  : Dons effectués par les utilisateurs 
- `Donor`     : Informations sur les donateurs 

---

## 🚀 Technologies principales

- Java 17 / Spring Boot
- Spring Data JPA / Hibernate
- MySQL
- Spring Security
- RESTful APIs
- Maven
- Swagger / Postman pour les tests

---

## 🔑 Fonctionnalités principales

- ✅ Parcourir et rechercher des produits éducatifs
- ✅ Ajouter des produits au panier et passer commande
- ✅ Gérer les réductions avec des coupons
- ✅ Créer une wishlist personnalisée
- ✅ Publier des avis sur les produits achetés
- ✅ Faire des dons en ligne à des causes éducatives
- ✅ Gestion des donateurs
- ✅ FAQ dynamique pour assistance utilisateur

---

## 🌐 API REST – Exemples d'endpoints

> Ces routes sont accessibles via l'API Gateway ou directement via les services.

### 📦 Produits
GET /api/admin/products
POST /api/admin/product

### 🛒 Panier

POST /api/customer/add 
GET /api/customer/cart

### 🧾 Commande

GET /api/admin/order/analytics
GET /api/admin/placedOrders

## 👨‍💻 Auteur

> Réalisé par **Nahed Harrath**  

> Projet : Microservice Marketplace éducative avec gestion des dons, commandes, wishlist, coupons, product,  cart

---
