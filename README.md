# LoveBoxer
PoC code for stealing the WiFi password of a network with a Lovebox IOT device connected. This PoC was is what I used in this [blogpost](https://www.grahamhelton.com/blog/lovebox/)

# Usage
```bash
sudo pip install wifi colorama
chmod +x loveboxer.py
sudo ./loveboxer
```
Loveboxer.py needs to be run as root in order to look for wifi interfaces.

![exploit](https://user-images.githubusercontent.com/19278569/139349398-ef0bd623-b4db-434b-81c1-3e505866d739.gif)
