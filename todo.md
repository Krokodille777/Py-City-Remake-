# Todo List

## Tasks
1. Preparation,  start, exit command
### Status: Done

2. Money, Inventory, Commands: 
   - balance: check your current balance;
   - inventory: check your current inventory;
   - save: save your current game progress;
   - load: load a previously saved game.
### Status: Done

3. Shopping:
    - first items and prices for then;
    Commands:
    - shoplist: view the list of available items in the shop (with their prices);
    - buy: purchase an item from the shop (if it's affordable);
    - sell: sell an item from your inventory back to the shop and earn money (if you have it);
### Status: Done

4. Work:
    - work system;
    - health, energy and happiness: check your current health, energy, and happiness levels;
    - new boost items: house and car. These items can boost your happiness and salary. 
    Commands:
    - work: perform a job to earn money (with a cooldown period);
    - sleep: rest to recover energy;
    - health: check your current health level;
    - energy: check your current energy level;
    - happiness: check your current happiness level;


5. Usable Items & Eating:
    - food items and their effects;
    - food & drink staling: food and drink items can go stale over time. Stale food and drink can have negative effects on your health, energy, and happiness;
    - sold stale food and drink brings less money than fresh food and drink;
    - more usable items: mystery boxes, gift boxes, and other special items.
    - trashing items: you can trash items from your inventory to free up space, but you won't get any money back for them.
    - luck system;
    Commands:
    - use: use an item from your inventory (if you have it);
    - eat: consume a food item to restore health or energy (if you have it);
    - sell (updated): sell an item from your inventory back to the shop and earn money. If it's stale, you'll earn less money for it;
    - trash: if you think an item is useless, you can get rid of it by trashing it. This will free up space in your inventory, but you won't get any money back for it;

6. Fish, Hunt & Mine:
    - fishing, hunting and mining physics;
    - new usable items: fishing rod, hunting rifle and mining pickaxe;
    - new sellable item types: fish, meat and ores;
    - luck system update;
    - catalog update: books, more food items, TV, movies, and more; 
    - new stats: intelligence and perception.
    Commands:
    - fish: catch fish from the water;
    - hunt: shoot an animal to get meat;
    - mine: dig up ores from the ground;
    - read: read a book to increase your knowledge and happiness (if you have it);
    - watch: watch a movie or TV show to increase your happiness (if you have it);

7. Gambling:
    - gambling system;
    - luck system update;
    - different gambling games: coin flip, slot machine, rock-paper-scissors, battle and more;
    Commands:
    - gamble: gamble your money for a chance to win more money (with a cooldown period);
    - choosegame: choose a gambling game to play (if you have enough money);


8. Cook & Craft:
    - cooking and crafting system;
    - new sellable item types: cooked food and crafted items, materials & ingredients;
    - luck system update;
    Commands:
    - cook: prepare a meal using ingredients from your inventory (if you have them);
    - craft: create a new item using materials from your inventory (if you have them);

9. Medicine & Training:
    - medicine and training system;
    - new sellable item types: medicine and training items;
    - catalog update: new catalog **pages** instead of one long catalog;
    - help system update: new help **pages** instead of one long help, descriptions for each command;
    - eat upgrade: obesity: eating too much when you're already full can lead to obesity, which can have negative effects on your health, energy, and happiness; if you are obese, you can attend a gym to lose weight and improve your health, energy, and happiness;
    Commands:
    - heal: use medicine to restore health (if you have it);
    - train: use training items to improve your skills (if you have them);

10. City & Travel:
    - city and travel system;
    - new sellable item types: travel tickets;
    - new places to visit: theater, museum, cafe, park, new cities;
    - transport: taxi, bus, train, plane, ship, chopper, spaceship;
    - having car making it possible to travel to nearby cities without a ticket;
    - travelling time depends on the distance between cities and the mode of transport used;
    - Medicine update: hospital, pharmacy and gym are now available in the city;
    - Sleep Update: hotel and motel are now available in the city;
    - Sleep update 2: if you don't have a house or the prices for hotel and motel are too high, you can sleep in the park or on the street, but this will have negative effects on your health, energy, and happiness;
    Commands:
    - travel: move to a different city or location (if you have a ticket);
    - cityinfo: view information about the current city or location;
 
11. Quests & Achievements:
    - quest and achievement system;
    - new sellable item types: quest items;
    - random quests during traveling;
    Commands:
    - quest: view available quests and their requirements;
    - completequest: complete a quest to earn rewards (if you meet the requirements);
    - achievements: view your achievements and progress;

12. Pets & Relationships:
    - pet and relationship system;
    - new sellable item types: pet items and relationship gifts;
    - City update: pet shop and relationship center are now available in the city;
    Commands:
    - adoptpet: adopt a pet to keep as a companion (if you have the required items);
    - feedpet: feed your pet to keep it healthy and happy (if you have the required food);
    - carepet: take care of your pet to keep it healthy and happy (if you have the required items);
    - petstats: view your pet's stats and progress;

13. Work Update - Jobs:
    - new jobs and work system update;
    - luck system update;
    - boost items: suitcase, fan, and briefcase. These items can boost your salary and happiness when working.
    Commands:
    - joblist: view available jobs and their requirements;
    - jobapply: apply for a job to earn money (if you meet the requirements);
    - work: perform a job to earn money (with a cooldown period and different outcomes based on luck);
    - jobquit: quit your current job (if you have one);


14. Events & Seasons:
    - event and season system;
    - new sellable item types: event items;
    - seasonal events and activities;
    Commands:
    - eventinfo: view information about the current event or season;
    - participateevent: participate in an event or activity to earn rewards (if you meet the requirements);

15. Multiplayer, Mail & Social (Optional):
    - multiplayer, mail and social system;
    - new sellable item types: social items;
    - multiplayer features: chat, trade, and compete with other players;
    - hangout allows to travel to places in Step 10 and do gambling like in Step 7, but with other players;
    - idk how i am going to implement this, but i will try to make it work;
    Commands:
    - mail: send and receive messages from other players;
    - friendlist: view your friends and their online status;
    - trade: trade items and money with other players (if you have the required items);
    - chat: communicate with other players in real-time;
    - gift: send gifts to other players to improve your relationship with them (if you have the required items);
    - confess: confess your feelings to another player to start a relationship (if you have the required items);
    - relationship: view your current relationships and their status;
    - hangout: hang out with other players to improve your relationship with them (if you have the required items);

16. Homestead & House (Optional):
    - homestead and house system;
    - new sellable item types: house items;
    - homestead features: build and customize your own home, garden, and farm;
    - house features: buy and upgrade your own house, furniture, and appliances;
    Commands:
    - build: build and customize your own home, garden, and farm (if you have the required items);
    - upgrade: upgrade your own house, furniture, and appliances (if you have the required items);
    - decorate: decorate your own home with furniture and decorations (if you have the required items);