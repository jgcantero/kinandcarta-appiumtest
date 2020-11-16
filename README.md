El proyecto consiste en la automatización de un tarea dentro de la aplicación móvil.
A lo largo de su desarrollo se agregarán nuevas características o funcionalidades heredadas de la aplicación en Browser y Webview.

Carpeta del proyecto:

    El proyecto está alojado en una carpeta llamada "kinandcarta-appiumtest" dentro de la carpeta Users


Herramientas:

	Android studio

	Es el IDE oficial para crear aplicaciones en todo tipo de dispositivos Android. 
	Para descargar Android Studio utilize el siguiente enlace:
   	    https://developer.android.com/studio

	Visual Studio Code

	Es un editor de código redefinido y optimizado para construir y depurar aplicaciones modernas tanto de web como cloud.
	Actualmente es el IDE por defecto utilizado en el equipo de Web Automation del producto.
	Para descargar Visual Studio Code utilize el siguiente enlace:
		https://code.visualstudio.com/download

	Java

	Para descargar Java utilize el siguiente enlace:				
		https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html
	Es necesario poseer una cuenta registrada en Oracle.
	Para crear una cuenta utilice el siguiente enlace:
		https://profile.oracle.com/myprofile/account/create-account.jspx
	Después de la instalación, es necesario establecer las variables de entorno JAVA_HOME y ANDROID_HOME en su archivo bash_profile.

	Homebrew

	Homebrew instala paquetes que no vienen por defecto en los sistemas de Apple. 
	Para instalar homebrew pegue el siguiente comando en su terminal:
		/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

	Python

	Python es un lenguaje orientado a objetos, programación imperativa y funcional.
	Actualmente es el lenguaje de programación por defecto utilizado en el equipo de Web Automation del producto.
	Para instalar Python es necesario establecer primero las variables de entorno en su archivo bash_profile:
		export PATH="/usr/local/opt/python/libexec/bin:$PATH"
	Una vez establecidas las variables de entorno, para instalar Python pegue el siguiente comando en su terminal:
		brew install python
		brew install pip
		pip install behave

	Appium

	Appium es un servidor HTTP escrito en node.js que crea y manipula varias sesiones de Drivers para distintas plataformas. 
	Para instalar Appium pegue el siguiente comando en su terminal:
    	brew install npm    #instalar appium via(source) npn(Node JS Package Manager)
		pip install appium-python-client


Configurando el entorno

	Para un funcionamiento óptimo del proyecto, asegúrese de que estas variables de entorno se encuentran presentes en su bash_profile.

	# Android
	
	export ANDROID_HOME=/Users/"your username"/Library/Android/sdk
	export PATH=$PATH:$ANDROID_HOME/platform-tools
	export PATH=$PATH:$ANDROID_HOME/tools
	export PATH=$PATH:$ANDROID_HOME/tools/bin
	export PATH=$PATH:$ANDROID_HOME/emulator

	#Java

	export JAVA_HOME=$(/usr/libexec/java_home)

	#Python

	export PATH="/usr/local/opt/python/libexec/bin:$PATH"



	Luego configuraremos el emulador:

	|	  Emulator	|			Setup					|
	|	Pixel_3a_11	| Hardware Pixel 3a Api 30 OS 11.0 CPU x86_64 with google apps  |



	Appium Desired Capabilities:

	{
	"deviceName": "Pixel_3a_11",
	"platformVersion": "11",
	"platformName": "Android",
	"app": "/Users/kinandcarta-appiumtest/support/apps/amazon_shopping.apk",
	"appPackage": "com.amazon.mShop.android.shopping",
	"appActivity": "com.amazon.mShop.home.HomeActivity",
	"automationName": "UiAutomator2"
	}
	
	Aplicación
	
	Descargar la última versión de Amazon Compras desde un mirror site y renombrar el archivo a "amazon-shopping.apk", luego copiar y pegarlo en la
	siguiente ruta: 
	kinandcarta-appiumtest/support/apps
