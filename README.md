# Repositorio para la práctica final de la asignatura de Verificación y desarrollo de programas
Aplicación web realizada con [Django](https://www.djangoproject.com/) en [Python](https://www.python.org/).
## Autores
[Juan de Vicente](https://github.com/juanDeVicente)<br>
[Jaime Escribano](https://github.com/JaimeEscribano)<br>
[Raúl Martínez](https://github.com/Ayato27)<br>
[Paula Pascual](https://github.com/PaulaPascual)<br>
[Claudia Rodríguez](https://github.com/ClaudiaRodriguezM)<br>
## Consideraciones
Para poder ejecutar los tests de Selenium es necesario tener instalado el navegador web [Firefox](https://www.mozilla.org/firefox/new/)
así como [Geckodriver.exe](https://github.com/mozilla/geckodriver/releases)

## Instrucciones de instalación
1. Clonar el repositorio git.
2. Instalar las librerias listadas en [requirements.txt](https://github.com/juanDeVicente/textMiningUTAD/blob/master/requirements.txt).
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
 5. Añadir Geckodriver a las variables de entorno:
       1. Buscamos "Mi equipo" en búsqueda, botón derecho "Propiedades"
       
       ![N|Solid](https://66.media.tumblr.com/68f84548f7860c2f241a6ab56743d564/tumblr_ps9dkuIwib1tgpiouo5_400.png)
       
       2. Configuración avanzada de distema
       
       ![N|Solid](https://66.media.tumblr.com/aad8cc37b98764af396d78a6cce5858d/tumblr_ps9dkuIwib1tgpiouo4_400.png)
       
       3. Variables de entorno
       
       ![N|Solid](https://66.media.tumblr.com/5912bd67b7fb5fba004edf9263d429e4/tumblr_ps9dkuIwib1tgpiouo3_400.png)
       
       4. Buscamos la variable "Path" y le damos a "Editar"
       
       ![N|Solid](https://66.media.tumblr.com/c7b76c54601ae70b66f5b3508500c36b/tumblr_ps9dkuIwib1tgpiouo2_400.png)
       
       5. Buscamos el Path donde se encuentra geckodriver, lo copiamos y lo añadimos en la variable
       
       ![N|Solid](https://66.media.tumblr.com/e4fe1a0be91184313de4fe8ddc2092c1/tumblr_ps9dkuIwib1tgpiouo1_540.png)
       
       
       Para kernel Linux, seguir  [este tutorial](https://www.youtube.com/watch?v=VSmfKeTkL48).
        
## Instrucciones para realizar una prueba de word_frequency
1. Abrir la terminal
2. Seleccionar la ruta del proyecto clonado y la carpeta en la terminal:
    ```
    cd <ruta_proyecto_clonado>/word_frequency
    ```
3. Ejecutar el siguiente comando:
    ```
    python word_frequency.py
    ```
    
## Instrucciones para ejecutar los test de word_frequency
1. Abrir la terminal
2. Seleccionar la ruta del proyecto clonado y la carpeta en la terminal:
    ```
    cd <ruta_proyecto_clonado>/word_frequency/test
    ```
3. Ejecutar el siguiente comando:
    ```
    python pytest word_frequency_tests.py
    ```
    
## Instrucciones para realizar una prueba de twitter_api
1. Abrir la terminal
2. Seleccionar la ruta del proyecto clonado y la carpeta en la terminal:
    ```
    cd <ruta_proyecto_clonado>/twitter_api
    ```
3. Ejecutar el siguiente comando:
    ```
    python twittwer_api.py
    ```
    
## Instrucciones para ejecutar los test de twitter_api
1. Abrir la terminal
2. Seleccionar la ruta del proyecto clonado y la carpeta en la terminal:
    ```
    cd <ruta_proyecto_clonado>/twitter_api/test
    ```
3. Ejecutar el siguiente comando:
    ```
    python pytest twittwer_api_tests.py
    ```
    
## Instrucciones para ejecutar el servidor de Django en local
1. Abrir la terminal
2. Seleccionar la ruta del proyecto clonado en la terminal:
    ```
    cd <ruta_proyecto_clonado>/text_mining_utad_web
    ```
3. Ejecutar los siguientes comandos:
    ```
    python manage.py runserver
    ```
## Instrucciones para ejecutar los tests de bdd
1. Abrir la terminal
2. Seleccionar la ruta del proyecto clonadlo en la terminal:
    ```
    cd <ruta_proyecto_clonado>/text_mining_utad_web
    ```
3. Ejecutar los siguientes comandos:
    ```
    python manage.py behave
    ```
    
