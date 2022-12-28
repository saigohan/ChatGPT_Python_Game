# I used ChatGPT to create an entire video game with Python


![image](https://res.craft.do/user/full/7a93547b-a2a3-6209-a5e3-1a49258c4f73/doc/B34D88DD-3909-49E3-8E78-0EB06EE01EFA/E64E0FF2-2B70-44D4-A3D8-9537724A158E_2/i9toSYsMuJjNCbKD9bYUtDlUkzHzjY9SzfCkqQLtC5wz/PngItem_4394113.png)

Image from pngitem

## 🎮 What is it About?


OpenAI just released **ChatGPT** , a new language model that can chat with you, give you detailed answers to inquiries, and even help with programming.

I wanted to test the limits of this **new AI bot** and see if **chatGPT** could be a good **pair programmer** for **designing video games**. I wondered how well the AI bot can help game design learners build their own video game, I believe that with some help, anyone can build their own games.

### Description of the Project


`Pygame` is an open source `Python` programming language library for making video games. It's not a game development platform like Unity or Unreal Engine which are very popular among game designers. Pygame is easy to install lightweight, but has a lot of limitations and is better suited for light video games such as a `2D platformer.` Unlike the popular game engines, when using Pygame, every aspect of the game needs to be written in a line of code, which can quickly become tedious. That's why I wanted `chatGPT` to provide some help.

![image](https://res.craft.do/user/full/7a93547b-a2a3-6209-a5e3-1a49258c4f73/doc/B34D88DD-3909-49E3-8E78-0EB06EE01EFA/E99AA06E-B9A3-4E7F-8EC3-A8801DB1F80E_2/6r3NVyYgblqcQ3o6L1yM1u9Fqzt6CLvme7iDi0Df4S4z/PngItem_1585033.png)

Image from pngitem

### Let’s Get Started!


First of all, I checked if ChatGPT can help:

![image](https://res.craft.do/user/full/7a93547b-a2a3-6209-a5e3-1a49258c4f73/doc/B34D88DD-3909-49E3-8E78-0EB06EE01EFA/E6638BC6-2698-4A4D-B74E-E18C08E7C0CF_2/ZaIuh2Aw0jUAB1RdlwDNyzmxHlPxuAy6paP1zFBnbDwz/Screenshot%202022-12-23%20at%2012.33.15.png)

That's a good start. I then asked the bot to create the **basic structure of code for the game**. He gave me a few lines of code, importing the pygame library, setting up the game window, the game loop that starts the game; fill the screen with a colour and stops the game when you quit.

![image](https://res.craft.do/user/full/7a93547b-a2a3-6209-a5e3-1a49258c4f73/doc/B34D88DD-3909-49E3-8E78-0EB06EE01EFA/DB36FBFD-59CD-4341-979E-272A6063180D_2/PCyDomZygCpF9dxPNgamzMTGw7acAvy5aYdux161dMMz/Image.png)

### Building the background and the player


I used the code from ChatGPT with a few modifications and continued with the background. I wanted a depth effect, so I chose a parallax background (it has 4 layers that moves at different speed depending on how far they are from the player). I had to learn from *[Coding With Russ](https://www.youtube.com/@CodingWithRuss)* on YouTube.   
Then I incorporated the player that I wanted to animate, for this I used a sprite sheet. ChatGPT helped with the event handling of the game, to associate the animation frames to actual keys pressed by the player. I gradually added some of ChatGPT lines of code, then made some changes, and he helped with fixing bugs. 

![image](https://res.craft.do/user/full/7a93547b-a2a3-6209-a5e3-1a49258c4f73/doc/B34D88DD-3909-49E3-8E78-0EB06EE01EFA/09B8DF34-1A40-426A-82CD-4C23BD4081B6_2/ViivZMafHTBxqXwzj0pDT4uM6o00XpCQVKmTRy060pEz/Image.png)

### Optimising the code


When the code got a bit messy, I asked ChatGPT how to optimise it. 

## 🏗️ Built with


The libraries used


- `Pygame`

Game assets and graphic content


- Parallax background from `Luis Zuno` on [itch.io](https://itch.io)
- The player sprite sheet from `Elthen` on [itch.io](https://itch.io)
- Font from

## Contributors

- Yonah Bôle
- ChatGPT by OpenAI
