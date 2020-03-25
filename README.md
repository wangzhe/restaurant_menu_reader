# restaurant_menu_reader

[![star this repo](http://githubbadges.com/star.svg?user=wangzhe&repo=restaurant_menu_reader&style=default)](https://github.com/wangzhe/restaurant_menu_reader)
[![fork this repo](http://githubbadges.com/fork.svg?user=wangzhe&repo=restaurant_menu_reader&style=default)](https://github.com/wangzhe/restaurant_menu_reader/fork)
![python](https://upload.wikimedia.org/wikipedia/commons/f/fc/Blue_Python_3.7_Shield_Badge.svg)

### TODO List
+   infrastructure (tesseract with en+cn, docker)
+   test one case
+   open cv
+   tesseract, lang, opencv

### installation

1. Clone the repository:
    
    <code>$ git clone https://github.com/wangzhe/restaurant_menu_reader</code>
    
2. Build docker image

    <code>$ docker build -t menu_reader . </code>

3. Build docker and app
    
    <code>$ docker run -it -p 8083:8082 --name test menu_reader</code>
    
4. enjoy! 
    
