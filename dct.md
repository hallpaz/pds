---
marp: true
paginate: true
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
    <td style="border: none;"> <img src="img/uni-1024.png"  alt="1" > <p align="center">(A)</p> </td>
    <td style="border: none;"><img src="img/uni1024-50.jpg" alt="2"><p align="center">(B)</p></td>
    </p></td>
   </tr> 
</table>

---

![bg](img/same-meme.jpg)

---

# Consegue ver a diferença?


<table>
  <tr>
    <td style="border: none;"> <img src="img/uni-1024.png"  alt="1" > <p align="center"><b>(A) 1.6 MB</b></p> </td>
    <td style="border: none;"><img src="img/uni1024-50.jpg" alt="2"><p align="center"><b>(B) 157 KB</b></p></td>
    </p></td>
   </tr> 
</table>

---

# Objetivos

- Entender os fundamentos de compressão
- Compreender as propriedades da Transformada de Cossenos
- Aplicar a Transformada Discreta de Cossenos (DCT) na compressão de sinais

![bg right:10%](img/bg-impatech.jpg)


---

# Compressão


![](img/compression-fundamentals.png)

<!-- 
<table>
  <tr style="border: none;">
    <td style="border: none; bgcolor: #000000"> <img src="img/placeholder.png"  alt="1" > </td>
    <td style="border: none;"><img src="img/placeholder.png" alt="2"></td>
    </p></td>
   </tr> 
</table> -->

----

# Exemplo do JPEG

![h:500](img/jpeg-ops.png)

---

# Por que Transformada de Cossenos?

- Representação do sinal em termos de frequências
- Compactação de energia
- Computacionalmente eficiente

![bg right:10%](img/bg-impatech.jpg)

----


# Fundamentos

<!-- _backgroundColor: #ff8aef -->
![bg opacity:0.15](img/impatech.jpg)
<!-- _paginate: false -->

---

# Representação de sinal discreto


![h:500](img/discrete-signal.png)

---

![bg 90%](img/dct-video1.png)
<!-- _backgroundColor: #000000 -->

<!-- _footer: from The Unreasonable Effectiveness of JPEG: A Signal Processing Approach -->

---

![bg 90%](img/dct-video2.png)

<!-- _backgroundColor: #000000 -->
<!-- _footer: from The Unreasonable Effectiveness of JPEG: A Signal Processing Approach -->

---

![bg 90%](img/dct-matrix.png)

<!-- _backgroundColor: #000000 -->
<!-- _footer: from The Unreasonable Effectiveness of JPEG: A Signal Processing Approach -->

---

![bg 90%](img/dct-cosseno.png)

<!-- _backgroundColor: #000000 -->
<!-- _footer: from The Unreasonable Effectiveness of JPEG: A Signal Processing Approach -->

---

![bg 85%](img/dct-transpose.png)

<!-- _backgroundColor: #000000 -->
<!-- _footer: from The Unreasonable Effectiveness of JPEG: A Signal Processing Approach -->

---

![bg 90%](img/inverse-dct.png)

<!-- _backgroundColor: #000000 -->
<!-- _footer: from The Unreasonable Effectiveness of JPEG: A Signal Processing Approach -->

---

# Transformada Discreta de Cossenos

$$
F(k) = \alpha(k) \sum_{n=0}^{N-1} f(n) \cos\left[\frac{\pi (2n + 1) k}{2N}\right]
$$

Em que:
- $k = 0, 1, \dots, N-1$
- $\alpha(k)$ is the normalization factor:
  $$
  \alpha(k) =
  \begin{cases}
    \sqrt{\frac{1}{N}}, & \text{if } k = 0, \\
    \sqrt{\frac{2}{N}}, & \text{if } k > 0.
  \end{cases}
  $$

---

# Transformada Discreta Inversa de Cossenos

<br/>

$$
f(n) = \sum_{k=0}^{N-1} \alpha(k) F(k) \cos\left[\frac{\pi (2n + 1) k}{2N}\right]
$$

Em que:
- $n = 0, 1, \dots, N-1$

---

# Aplicação - Compressão de Imagens

![bg opacity:0.15](img/impatech.jpg)
<!-- _backgroundColor: #ffc556 -->
<!-- _paginate: false -->

---

# Operações na Compressão JPEG

<br/>

![h:450](img/jpeg-ops.png)

---

# DCT em 2D

$$
F(u, v) = \alpha(u) \alpha(v) \sum_{x=0}^{N-1} \sum_{y=0}^{M-1} f(x, y) \cos\left[\frac{\pi (2x + 1) u}{2N}\right] \cos\left[\frac{\pi (2y + 1) v}{2M}\right]
$$

Em que:
- $u = 0, 1, \dots, N-1$
- $v = 0, 1, \dots, M-1$
- $\alpha(u)$ e $\alpha(v)$ são fatores de normalização:
  $$
  \alpha(k) =
  \begin{cases}
    \sqrt{\frac{1}{N}}, & \text{if } k = 0, \\
    \sqrt{\frac{2}{N}}, & \text{if } k > 0.
  \end{cases}
  $$

---

# DCT inversa em 2D:

<br/>

Para reconstruir o sinal original $f(x, y)$ a partir de $F(u, v)$, usamos:

$$
f(x, y) = \sum_{u=0}^{N-1} \sum_{v=0}^{M-1} \alpha(u) \alpha(v) F(u, v) \cos\left[\frac{\pi (2x + 1) u}{2N}\right] \cos\left[\frac{\pi (2y + 1) v}{2M}\right]
$$


---

# Base $8 \times 8$

- Imagem é segmentada em retalhos $8 \times 8$.
- DCT é aplicada em cada retalho.

![bg right:57% fit](img/dct-2d-basis.png)

<!-- _footer: Image from https://www.oliviergibaru.org/courses/NA_Compress.html -->
<!-- _paginate: false -->

---

# Concentração de energia nas baixas frequencias

![h:500](img/energy-concentration.png)

---
# Quantização

- Coeficientes quantizados
- Valores pequenos $\rightarrow$ 0 (zero)

![bg right h:380](img/quantization.png)

---

## Valores quantizados

![bg left height:70%](img/quantized-heatmap.png)

<table>
    <!-- <thead>
    <tr>
        <th></th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
    </tr>
    </thead> -->
    <tbody>
    <tr>
        <!-- <th>0</th> -->
        <td>-7</td>
        <td>1</td>
        <td>-2</td>
        <td>3</td>
        <td>-2</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <!-- <th>1</th> -->
        <td>-2</td>
        <td>-4</td>
        <td>-1</td>
        <td>-3</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <!-- <th>2</th> -->
        <td>1</td>
        <td>2</td>
        <td>2</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <!-- <th>3</th> -->
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <!-- <th>4</th> -->
        <td>-2</td>
        <td>-1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <!-- <th>5</th> -->
        <td>-1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <!-- <th>6</th> -->
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <!-- <th>7</th> -->
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    </tbody>
</table>

---

# Imagem reconstruída

<table>
  <tr>
    <td style="border: none;"> <img src="img/cropped.png"  alt="1" > <p align="center">(A)</p> </td>
    <td style="border: none;"><img src="img/decompressed.png" alt="2"><p align="center">(B)</p></td>
    </p></td>
    <td style="border: none;"> <img src="img/diff.png"  alt="1" > <p align="center">(C)</p> </td>
    <td style="border: none;"><img src="img/normdiff.png" alt="2"><p align="center">(D)</p></td>
    </p></td>
   </tr> 
</table>

(A): original; 
(B): reconstruída;
(C): magnitude da diferença;
(D): magnitude da diferença normalizada.


---

# Conclusão

- Transformada de cosseno é uma forma de representar o sinal em termos de frequencias.
- Métodos de compressão exploram percepção.
  - Sistema visual humano é menos sensível aos detalhes de alta frequencia.
- DCT concentra energia do sinal em coeficientes de baixa frequencia, facilitando o descarte de informação.

![bg right:10% ](img/bg-impatech.jpg)


---

# Para pensar...

### Dá pra fazer melhor?

<!-- _backgroundColor: #ebf47a -->

---

# Referências

- 📖 LIM, J. S. Two-Dimensional Signal and Image Processing. Prentice Hall, 1990. Páginas 165 a 179.
- ▶️ Reducible. The Unreasonable Effectiveness of JPEG: A Signal Processing Approach. Disponível em: https://youtu.be/0me3guauqOU?si=xGvW6sP1Kw9DzPLK
- 🔗 Olivier Gibaru. Image Compression. Disponível em: https://www.oliviergibaru.org/courses/NA_Compress.html

<!-- _paginate: false -->


