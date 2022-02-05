# chess-helper
A chrome extension + backend system to get next best move for an ongoing game in various platforms.

## **Currently Supported Platforms**
* https://lichess.org
* https://chess.com

## **Steps to set up the project**
* #### Setting up the extension:

  * Enable developer mode in chrome.
  * Click on load unpacked extension button.
  * Browse to the extension folder of this project and upload.
  
* #### Setting up the Backend Flask API:
  * Use homebrew to download stockfish engine in your system.
  * Download all the dependencies present inside backend/requirements.txt file by running 'pip install requirements.txt'.
  * Run api.py after downloading the dependencies to start backend server.

* #### Start any game in one of the supported platforms:
  * Click on extension icon to get a json response back with the next move details.

## **Tested Platorm**
* #### Macbook Air M1, Chrome full screen(screen size may cause html attributes to change due to which board state may not be parsed properly)
