---
marp: true
paginate: true
theme: default
# testar gaia ou uncover
math: mathjax
---

<style>
    section {
        font-family: "Fira Sans", Arial;
    }
    h1, h2 {
        font-family: "Fira Sans", monospace;
        color: black;
        /* font-size: 62px */
    }
</style>

<br>

# Transformada de cossenos <br> e compressão de sinais


## Hallison Paz

#### 28 de janeiro de 2024

![bg](img/bg-impatech.jpg)

<!-- _paginate: false -->

---

# Consegue ver a diferença?


<table>
  <tr>
    <td> <img src="img/placeholder.png"  alt="1" > <p align="center">(A)</p> </td>
    <td><img src="img/placeholder.png" alt="2"><p align="center">(B)</p></td>
    </p></td>
   </tr> 
</table>

<!-- _footer: mostrar uma imagem sem compressão e outra com compressão com perda, usando DCT, lado a lado. Perguntar se conseguem ver a diferença. -->

---

# Consegue ver a diferença?


<table>
  <tr>
    <td> <img src="img/placeholder.png"  alt="1" > <p align="center"><b>(A) XXXXX MB</b></p> </td>
    <td><img src="img/placeholder.png" alt="2"><p align="center"><b>(B) XXXXX MB</b></p></td>
    </p></td>
   </tr> 
</table>

---

# Objetivo

- Entender os fundamentos de compressão
- Derivar a transformada de cossenos a partir da transformada de Fourier
- Compreender as propriedades da transformada de cossenos
- Aplicar a DCT na compressão de sinais

---

# Recapitulando

### Compressão: redundância - percepção

- mostrar exemplos redundancia

<table>
  <tr style="border: none;">
    <td style="border: none;"> <img src="img/placeholder.png"  alt="1" > </td>
    <td style="border: none;"><img src="img/placeholder.png" alt="2"></td>
    </p></td>
   </tr> 
</table>

----


# Fundamentos

<!-- _backgroundColor: #ff8aef -->
![bg opacity:0.15](img/impatech.jpg)
<!-- _paginate: false -->

---

# Transformada Discreta de Cossenos (DCT)

<br/>

$$X_{\text{DCT}}[k] = \sum_{n=0}^{N-1} x[n] \cdot \cos\left(\frac{\pi}{N} \left(n + \frac{1}{2}\right) k\right)$$


---

# Transformada de cossenos a partir da transformada de Fourier

## assumir sinal é par

---

# Transformada de cossenos discreta (DCT)

- mostrar como ela vem da versão contínua

---

# DCT na prática!

<!-- _backgroundColor: #bfff8c -->

<!-- _class: lead -->
<!-- _paginate: false -->

---

# brincando com Cosseno

---

# Perlin Noise

---

# Aplicação - Compressão de Imagens

<!-- _backgroundColor: #ffc556 -->
<!-- _paginate: false -->

---

# JPEG Operations PIPELINE

---

# Base $8 \times 8$

![bg right:60% fit](img/dct-2d-basis.png)

<!-- _footer: Image from https://www.oliviergibaru.org/courses/NA_Compress.html -->
<!-- _paginate: false -->

---
# Tabela de quantização

![](img/placeholder.png)

---

# Valores arredondados

---

# Imagem reconstruída

---

# Para pensar...

### Dá pra fazer melhor?

<!-- _backgroundColor: #ebf47a -->

---

# Referências

- 

<!-- _paginate: false -->

---

# Propriedades da DCT 

- Frequency domain
- Energy compaction

- orthogonal functions (does it makes sense?)

---

# Sanity checks

- Calcular a transformada de cosseno de um cosseno
- Mostrar como coeficientes mudam na prática

---

# Exemplo com Perlin Noise

- mostrar como coeficientes de baixa frequencia tem alta energia e de alta frequencia tem baixa energia.
- Mostrar como sinal pode ser reconstruído aos poucos com alguns coeficientes.

---

# Explicar em termos de segmentos?

- Por que faz sentido segmentar?

---

# Exemplo com Imagens

---

# Discussão

- dá pra fazer melhor?

---

# Conclusão

- Transformada de cosseno é uma forma de representar o sinal no domínio de frequencias
- Métodos de compressão exploram percepção
- Sistema visual humano é menos sensível aos detalhes de alta frequencia
- DCT concentra energia do sinal em coeficientes de baixa frequencia, facilitando o descarte dos de alta.


