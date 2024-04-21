# Análise de mercado para montagem de um PC gamer
Projeto Final da eletiva Análise de texto de fontes desestruturadas e web.

# Integrantes
Rafael Malcervelli
Manuel 

# Descricao
A montagem de um PC gamer envolve a escolha criteriosa de componentes que não apenas ofereçam o melhor desempenho, mas também representem um custo-benefício atraente. Com a volatilidade dos preços de hardware e a variedade de produtos disponíveis, consumidores enfrentam dificuldades em identificar as melhores opções de compra em um dado momento. Este projeto visa desenvolver uma prova de conceito que utilize técnicas de web scraping e análise de texto para extrair dados de múltiplos marketplaces e avaliações de produtos, permitindo uma comparação de preços, disponibilidade de estoque, e a qualidade percebida dos componentes através das reviews de usuários.

# Origem dos dados
Os dados serão extraídos de vários marketplaces e sites de e-commerce especializados em hardware de computador, tais como Amazon, Kabum, Mercado Livre, Aliexpress etc. As páginas de produtos individuais fornecerão informações sobre preços, especificações técnicas, disponibilidade, e avaliações de usuários.

# Técnicas para extrair e tratar os dados
1. Extração de Dados:
- Web Scraping: Utilizar bibliotecas como BeautifulSoup, Scrapy ou Selenium para extrair informações das páginas de produtos nos marketplaces selecionados. Isso incluirá preços, descrições, avaliações, e metadados como categorias e tags de produtos.
- APIs: Quando disponíveis, usar APIs dos sites de e-commerce para uma coleta de dados mais estruturada e eficiente, usando a biblioteca Requests para realizar uma conexão direta com os endpoints fornecidos.

2. Tratamento de Dados:
- Limpeza de Dados: Remover dados duplicados, corrigir erros de formatação e tratar valores ausentes.
- Normalização: Padronizar unidades de medida e formatos de moedas para facilitar comparações.

3. Análise de Dados:
- Comparação de Preços: Desenvolver algoritmos que comparem os preços entre diferentes fornecedores para identificar as melhores ofertas.
- Análise de Tendências: Avaliar a variação de preços ao longo do tempo e identificar padrões de disponibilidade de estoque.
- Insights dos Usuários: Extrair insights qualitativos das avaliações dos usuários sobre a qualidade e desempenho dos componentes.

