# normalizacao-enade

## Normalização dos dados do enade ##

Primeiramente baixe e instale o Sql Server.

O banco de dados tem que ser criado antes de iniciar o processo de normalização automatica.

Os seguintes dados serão pedido quando executado o main.

```
Host: 
User: 
Senha: 
Banco: 
executar processo de normalização: 
```

Depois de inserido os dados corretamente no programa, o sistema pega o arquivo enade no site, baixa e extrai. As tabelas são criadas e em seguida os dados são inseridos.

Obs: Os dados não são inseridos em paralelo pelo fato de as tabelas serem relacionadas entre si, e isso pode fazer voce esperar um pouco - dependendo da performance da sua maquina - quando começar a carregar a tabela aluno.
