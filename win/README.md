python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
  
 

Start Visual Studio: Developer Command Promt for VS2015 and check:

 C:\Program Files (x86)\Microsoft Visual Studio 14.0>echo %VSINSTALLDIR%
C:\Program Files (x86)\Microsoft Visual Studio 14.0\

C:\Program Files (x86)\Microsoft Visual Studio 14.0>set CL=/FI"%VCINSTALLDIR%\INCLUDE\stdint.h" %CL%
pip install pycrypto