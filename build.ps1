" please add *_rc.py when create  all resource files"
pyside6-rcc .\ui\resource.qrc -o .\ui\rc_resource.py; 
pyside6-uic .\ui\main_window.ui -o .\ui\ui_main_window.py --from-imports --rc-prefix

pyside6-uic .\ui\pages\dashboard.ui -o .\ui\pages\ui_dashboard.py --rc-prefix
pyside6-uic .\ui\pages\home.ui -o .\ui\pages\ui_home.py --rc-prefix
pyside6-uic .\ui\pages\lexus.ui -o .\ui\pages\ui_lexus.py --rc-prefix
pyside6-uic .\ui\pages\mazda.ui -o .\ui\pages\ui_mazda.py --rc-prefix
pyside6-uic .\ui\pages\toyota.ui -o .\ui\pages\ui_toyota.py --rc-prefix
pyside6-uic .\ui\pages\tumbr.ui -o .\ui\pages\ui_tumbr.py --rc-prefix
pyside6-uic .\ui\pages\youtube.ui -o .\ui\pages\ui_youtube.py --rc-prefix
