# Loja Luni - Sistema de E-commerce

## Descrição Geral

O sistema de e-commerce da Loja Luni é uma plataforma online desenvolvida em Django, criada para facilitar a gestão e a venda de roupas e acessórios. O objetivo é oferecer uma experiência de compra fácil e eficiente para os clientes, além de proporcionar ferramentas práticas para os administradores da loja.

## Funcionalidades

### Funcionalidades para Administradores

- **Gestão de Produtos**  
  - Adição, visualização, atualização e remoção de produtos.
  - Detalhes dos produtos incluem nome, descrição, tamanho, cor, preço, quantidade em estoque e imagem.

- **Gestão de Categorias**  
  - Criação, edição e exclusão de categorias como Masculino, Feminino, Unissex, Relógios, Bolsas e Acessórios.

- **Gestão de Estampas**  
  - Adição, visualização, atualização e exclusão de estampas.
  - Associação de estampas a produtos específicos.

- **Gestão de Pedidos**  
  - Registro e atualização do status dos pedidos ("Em Processamento", "Enviado", "Entregue").
  - Exclusão de pedidos, se necessário.

- **Gestão de Clientes**  
  - Cadastro, atualização de informações pessoais e visualização do histórico de pedidos.

- **Encerramento de Contas**  
  - Remoção de todas as informações associadas a uma conta quando um cliente decide encerrá-la.

### Funcionalidades para Clientes

- **Visualização do Catálogo**  
  - Navegação pelo catálogo de produtos, com exibição de detalhes como descrição, preço e imagem.

- **Carrinho de Compras**  
  - Adição de produtos ao carrinho de compras, com atualização em tempo real e cálculo automático do total.

- **Finalização de Compra**  
  - Processo de finalização de pedido rápido e seguro.

- **Pesquisa de Produtos**  
  - Barra de pesquisa para localizar produtos específicos com facilidade.

## Tecnologias Utilizadas

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Banco de Dados:** PostgreSQL (ou o banco de sua escolha)
- **Outras Ferramentas:** Django Admin, Django Rest Framework, etc.

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Ronygmb/Luni.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o banco de dados:**
   - Atualize o arquivo `settings.py` com as configurações do seu banco de dados.

4. **Execute as migrações:**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

6. **Acesse o sistema:**
   - Abra o navegador e vá para `http://localhost:8000/`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
