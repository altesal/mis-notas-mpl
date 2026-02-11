# Reglas de protección de ramas

### Asegurar que los cambios pasen por una Pull Request antes de hacer merge a rama master

- Ir a Settings > Branches > Branch protection rules

  Branche name patterns = master

  ✔ Require a pull request before merging

Con lo anterior, nadie podrá hacer git push directo a master. Todos los cambios tendrán que pasar por una PR.

# Operaciones con ramas

### Ver diferencias en un fichero

```
$ git --no-pager diff ./src/App.jsx

```

### Listar ramas

1. Listar ramas locales
  ```
  git branch

  ```

2. Listar ramas remotas
  ```
  git branch -r

  ```


### Borrar rama

1. Eliminar rama si ha sido fusionada
  ```
  git branch -d nombre_rama

  ```

2. Eliminar rama aunque no haya sido fusionada
  ```
  git branch -D nombre_rama

  ```

