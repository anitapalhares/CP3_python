# Anita Palhares
# Checkpoint 3: Computational Thinking With Python

def check_product_size(product_id: int, size_label: str) -> dict | str:

    """Validates and formats a user's birth state for Brazil.

    Args:
        product_id: um int unico pra identificar o cliente.
        size label: uma string para as abreviações dos tamanhos de roupas.

    Returns:
        Um dicionario com o id do fornecedor e

        a validação se os dados são bem sucedidos, se não, há mensagens de exeção """

    valid_sizes = (
        'PP', 'P', 'M', 'G', 'GG', 'XG'
    )

    try:
        new_sizes = size_label.strip().upper()
         # --- Validation Rules ---

        if len(new_sizes) != 2:
            raise ValueError(f"O tamanho '{new_sizes}' não é válido, use apenas duas letras")

        if new_sizes not in valid_states:
            raise ValueError(f"O tamanho '{new_sizes}' não é válido, use apenas os tamanhos: {valid_sizes}")

        # Success return
        return {
            "client_id": product_id,
            "tamanho": new_sizes
        }

    except ValueError as error:
        return f"erro de validação: {error}"

    except Exception:
        return "erro: formato invalido."

# _________ testes de cada caso ______________
print(check_product_size(1, " pp "))    # Successo: {'client_id': 1, 'tamanho': 'PP'}
print(check_product_size(2, "xxl"))     # Erro: tamanho do textoo
print(check_product_size(3, "LL"))      # Erro: tamanho não existe
print(check_product_size(4, "GG"))      # Successo: {'client_id': 4, 'tamanho': 'GG'}
print(check_product_size(5, "Pequeno")) # Erro: tamanho do textoo
print(check_product_size(6, "s"))       # Erro: tamanho não existe
print(check_product_size(7, "M"))       # Successo: {'client_id': 7, 'tamanho': 'M'}