
# GRAPH 

```
var userPages = await _graph.Users.GetAsync(q =>
{
  q.QueryParameters.Top = 999;
  q.QueryParameters.Filter = "...";
  //Añade el parámetro $count=true a la consulta Graph. Solicita que la respuesta incluya el recuento de elementos coincidentes (por ejemplo, usuarios o grupos).
  q.QueryParameters.Count = true; 
  //Añade la cabecera HTTP ConsistencyLevel: eventual, que permite utilizar determinadas consultas avanzadas de Microsoft Graph, como filtros y ordenaciones combinados con $count
  q.QueryParameters.Add("ConsistencyLevel", "eventual");

```
