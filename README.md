# Repositorio para la práctica final de la asignatura de Verificación y desarrollo de programas
Aplicación web realizada con [Django](https://www.djangoproject.com/) en [Python](https://www.python.org/).
## Autores
[Juan de Vicente](https://github.com/juanDeVicente)<br>
[Jaime Escribano](https://github.com/JaimeEscribano)<br>
[Raúl Martínez](https://github.com/Ayato27)<br>
[Paula Pascual](https://github.com/PaulaPascual)<br>
[Claudia Rodríguez](https://github.com/ClaudiaRodriguezM)<br>
## Consideraciones
Para poder ejecutar los tests de Selenium es necesario tener instalado el navegador web [Firefox](https://www.mozilla.org/firefox/new/).
## Instrucciones de instalación
1. Clonar el repositorio git.
2. Instalar las librerias listadas en [requirements.txt](https://github.com/juanDeVicente/get_last_50_tweets/blob/master/requirements.txt).
3. Abrir la consola de Python y ejecutar los siguientes comandos:
    ```python
    >>> import nltk
    >>> nltk.download()
    ```
    En la ventana emergente seleccionar la pestaña CORPORA.
    ![N|Solid](https://jantoniomora.files.wordpress.com/2017/08/screenshot-43.png)
    
    En la pestaña seleccionar el "identifier" stopwords y hacer click en el botón de "Download".
    ![N|Solid](https://jantoniomora.files.wordpress.com/2017/08/screenshot-44.png)
4. Añadir tus creedenciales de [desarrollador de twitter](https://developer.twitter.com/en/apply-for-access) a las variables de entorno de Python.<br>
    Abrir una consola de Python y ejecutar los siguientes comandos:
    ```python
    >>> import os
    >>> os.environ['ACCESS_TOKEN_KEY'] = <tu_access_token_key> 
    >>> os.environ['ACCESS_TOKEN_SECRET'] = <tu_access_token_secret> 
    >>> os.environ['CONSUMER_KEY'] = <tu_consumer_key>
    >>> os.environ['CONSUMER_SECRET'] = <tu_consumer_secret>
    ```

