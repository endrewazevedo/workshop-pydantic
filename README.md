# workshop-pydantic
Repositório de apoio para o Worshop ministrado sobre Pydantic

## O que é Pydantic?

Pydantic é uma biblioteca Python para definir modelos de dados ricos, validá-los e transformá-los.

* **Tipos estáticos:** Para melhor legibilidade e segurança.
* **Validação automática:** Garantindo a integridade dos dados.
* **Serialização:** Convertendo modelos em JSON, dict e outros formatos.

## Exemplo Simples

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str