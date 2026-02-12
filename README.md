# Conversor de Moedas Simples

Este projeto consiste em um script Python desenvolvido para realizar a conversão de valores em **Real (BRL)** para **Dólar Americano (USD)** e **Euro (EUR)**. O código utiliza entrada direta do usuário e processa os valores com base em taxas de câmbio pré-definidas.

---

### Funcionamento Detalhado do Script

O script executa uma sequência lógica de três etapas principais para garantir a conversão correta dos valores monetários:

1.  **Entrada de Dados e Tipagem:** O programa utiliza a função `input()` para receber o valor do usuário. Este valor é imediatamente convertido para **float** (ponto flutuante). Essa conversão é **obrigatória** para permitir que o sistema realize cálculos matemáticos e aceite centavos.

2.  **Processamento Matemático e Câmbio:**
    O cálculo é baseado em divisões simples utilizando taxas estáticas:
    * **Cálculo do Dólar:** O valor inserido em Real é dividido por **5.5**.
    * **Cálculo do Euro:** O valor inserido em Real é dividido por **0.92**.

3.  **Saída e Formatação de Dados:** A exibição final utiliza o método `.format()` com a máscara `{:.2f}`. Isso garante que os valores monetários sejam apresentados sempre com **duas casas decimais**, mantendo o padrão visual financeiro.

---

### Código Fonte

O script completo segue a estrutura abaixo:

```python
real = float(input('Qual o valor em real? R$: '))

dolar = real / 5.5
euro = real / 0.92

print('Com R${:.2f}, pode comprar US${:.2f} e EUR{:.2f}'.format(real, dolar, euro))
