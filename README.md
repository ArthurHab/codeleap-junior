### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/ArthurHab/codeleap-junior.git
   cd codeleap-junior
   ```
2. Create and activate the virtual environment
   ```sh
   python -m venv venv 
   ```
   - Windows
   ```sh
   venv\Scripts\activate
   ```
   - MacOS/Linux
   ```sh
	source venv/bin/activate
   ```
3. Install project dependencies
   ```sh
	pip install -r requirements.txt
   ```
4. Apply database migrations
   ```sh
	python manage.py migrate
   ```
5. Run tests to check if everything is working
   ```sh
	python manage.py test
   ```
6. Start the Django development server
   ```sh
	python manage.py runserver
   ```

Now you can access [localhost:8000/](http://localhost:8000/)  from your browser.




