# Waffer - Computer Vision

## Objetivo

Este repositório apresenta um sistema de processamento de imagem desenvolvido com OpenCV, com foco na aplicação de técnicas de **visão computacional para inspeção visual de wafers**. O objetivo principal é detectar e destacar o contorno principal de cada wafer presente em imagens obtidas do processo de fabricação ou inspeção.

## Descrição

A aplicação percorre um diretório contendo imagens de wafers, processando cada uma delas por meio de uma série de etapas que incluem:

- Conversão para escala de cinza  
- Desfoque com `blur` e `GaussianBlur`  
- Aplicação de limiar (thresholding)  
- Operações morfológicas para fechamento de contornos  
- Detecção de bordas com o algoritmo de Canny  
- Extração e desenho do maior contorno encontrado

Ao final, são salvas imagens resultantes de cada etapa do processamento, permitindo uma análise detalhada de todo o pipeline aplicado sobre os wafers.

## Pipeline de Processamento

1. **Escala de Cinza** – Conversão da imagem original para tons de cinza.
2. **Desfoque (Blur)** – Suavização da imagem para redução de ruídos.
3. **Thresholding** – Realce de áreas de interesse a partir de um valor de limiar.
4. **Morfologia** – Fechamento de pequenos buracos nos contornos usando kernel retangular.
5. **Filtro Gaussiano** – Redução adicional de ruído para contorno mais suave.
6. **Canny** – Detecção de bordas na imagem processada.
7. **Contorno Principal** – Identificação do maior contorno e marcação na imagem original.

## Tecnologias Utilizadas

- Python 3.x  
- OpenCV  
- NumPy  
- Sistema de arquivos via `os`

## Estrutura do Repositório

- `Originais/` – Imagens de entrada (wafers a serem analisados).
- `P&B/` – Imagens em tons de cinza.
- `Blur/` – Resultado do desfoque.
- `Threshold/` – Resultado do thresholding.
- `Morph/` – Resultado das transformações morfológicas.
- `Gaussian/` – Imagens suavizadas com filtro gaussiano.
- `Contornadas/` – Imagens finais com contorno principal destacado.
