# Reglas de protección de ramas

### Asegurar que los cambios pasen por una Pull Request antes de hacer merge a rama master

- Ir a Settings > Branches > Branch protection rules

  Branche name patterns = master

  ✔ Require a pull request before merging

Con lo anterior, nadie podrá hacer git push directo a master. Todos los cambios tendrán que pasar por una PR.


### Ver diferencias en un fichero

```
$ git --no-pager diff ./src/App.jsx

```


