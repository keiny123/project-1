[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Source code where the main.py live
source.dir = .

# (str) python-for-android branch to use, defaults to master
p4a.branch = develop

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3.8,kivy==2.0.0,kivymd,pillow,blinker==1.7.0,cachetools==5.3.3,certifi==2024.2.2,charset-normalizer==3.3.2,click==8.1.7,colorama==0.4.6,docutils==0.20.1,Flask==3.0.2,flutter==0.1,google-auth==2.28.1,google-auth-oauthlib==1.2.0,gspread==6.0.2,httplib2==0.22.0,idna==3.6,importlib-metadata==7.0.1,itsdangerous==2.1.2,Jinja2==3.1.3,Kivy==2.3.0,kivy-deps.angle==0.4.0,kivy-deps.glew==0.3.1,kivy-deps.sdl2==0.7.0,Kivy-Garden==0.1.5,MarkupSafe==2.1.5,numpy==1.24.4,oauth2client==4.1.3,oauthlib==3.2.2,pyarrow==15.0.0,pyasn1==0.5.1,pyasn1-modules==0.3.0,Pygments==2.17.2,pylance==0.10.2,pyparsing==3.1.1,pypiwin32==223,pywin32==306,requests==2.31.0,requests-oauthlib==1.3.1,rsa==4.9,setuptools==41.2.0,six==1.16.0,StrEnum==0.4.15,typing_extensions==4.10.0,urllib3==2.2.1,Werkzeug==3.0.1,zipp==3.17.0

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (int) Android NDK API to use
android.ndk_api = 21

# (list) Android permissions
android.permissions = INTERNET

# (list) Android services
# services =

# (str) Android app theme
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (bool) Fullscreen
fullscreen = 0

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
# p4a.url =

# (str) python-for-android branch to use
# p4a.branch =

# (str) python-for-android specific commit to use
# p4a.commit =

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
# ios.kivy_ios_dir =

# (str) iOS app theme
# ios.apptheme = 
