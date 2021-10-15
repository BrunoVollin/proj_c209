# Projeto de C209

<img src="src/images/running.png" style="width: 60vw">

## Como executar

1. Instalar as dependências **open cv** e **numpy** \
   <code>
   pip install --upgrade pip
   </code><br>
   <code>
   pip install opencv-python
   </code><br>
   <code>
   pip install numpy
   </code><br>
   <code>
   python -m pip install -U scikit-image
   </code><br>

2. Rodar <code>index.py</code>

## Possíveis erros

### Erro ao abrir a imagem do background

```sh
error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'
```

Caso ocorra o erro acima altere o local do arquivo <code>_bg.png_</code> no sistema para para <code>_C:\bg.png_</code> e altere a linha _50_ do arquivo <code>index.py\</code>.

```py
background_image = cv2.imread('c:/bg.png')
```
