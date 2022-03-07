# Offline chess tournament program
***
The offline chess tournament program allows you to manage tournaments offline and produce reports. You can add players, create tournaments, generate pairs of players for your tournaments, and see reports of the tournaments, rounds, matches, etc. which are saved inside a database.
## How to install my project
1. Open the Terminal
2. Clone the repository:
```
$ git clone https://github.com/CeliaTois/CeliaTOIS_4_03012022.git
```
3. Go to the project folder:
```
$ cd ../path/to/the/file
```
4. Create the virtual environment:
   - On macOS and Linux:
   ```
   $ source env/bin/activate
   ```
   - On Windows:
   ```
   $ env/Scripts/activate
   ```
5. Install the packages:
```
$ pip install -r requirements.txt
```

## How to run my project
1. Open the Terminal
2. Go to the project folder:
```
$ cd ../path/to/the/file
```
3. Launch the code:
```
$ python main.py
```

## How to generate a new flake report
1. Open the Terminal
2. Go to the project folder:
```
$ cd ../path/to/the/file
```
3. Generate the report:
```
$ flake8 --format=html --htmldir=flake-report
```
