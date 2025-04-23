Game Title: Space Invaders: OS Edition

Game Summary:
In this classic arcade-style game, players control a spaceship tasked with shooting down waves of incoming alien invaders. The game features responsive controls, 
a countdown timer, and a scoring system. Players must survive as long as possible with only 3 lives and destroy as many enemies as they can before the timer runs 
out or they are defeated.

Core Gameplay Loop:
The player moves left and right to dodge enemies and shoot bullets upward. Enemies continuously descend from the top of the screen. The player must react quickly 
to eliminate them while avoiding collisions. The game ends when the timer hits zero or the player loses all three lives.

Controls:

← and → keys: Move the spaceship

Spacebar: Shoot bullets

R: Restart after game over

Q: Quit after game over

Core Mechanics:

Shooting: Fires bullets to destroy enemies

Movement: Smooth side-to-side spaceship movement

Collision Detection: Hits between bullets and enemies, or enemies and player

Timer: 60-second countdown

Life System: Lose a life when hit by an enemy

Level Progression: The game gets harder as more enemies spawn over time, but it remains in a single looping level with continuous play.

Win/Loss Conditions:

Win: Score as high as possible before the timer ends

Loss: Game over if the player loses all lives or time runs out


OS Concepts Used


1. Process Creation:	The main game loop acts as a persistent process, initiating enemy spawn events as separate timed triggers (pygame.USEREVENT).
2. Threading/Scheduling: The game uses pygame.time.set_timer() to schedule events independently from the main game loop. This mimics periodic OS scheduling behavior.
3. Signal Handling:	The game listens for pygame.QUIT and pygame.KEYDOWN events to gracefully exit or restart—like signal catching in OS.
4. Memory Management:	Dynamic creation and destruction of sprites (Bullet, Enemy, etc.) mimic allocation and deallocation of memory for objects.
5. Resource Management / IPC (Simulated):	Sprite groups act like shared resources; collisions between groups simulate IPC-type interactions between isolated components.
