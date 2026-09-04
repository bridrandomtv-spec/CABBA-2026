import re

with open("firestore.rules", "r") as f:
    content = f.read()

content = content.replace("match /products/{id} { allow read: if true; allow write: if isAdmin(); }", "match /products/{id} { allow read: if true; allow update: if isAuthenticated(); allow create, delete: if isAdmin(); }")

with open("firestore.rules", "w") as f:
    f.write(content)
