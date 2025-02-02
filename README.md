# Multilingual FAQ System

A Django-based FAQ management system with multilingual support, built using Django REST Framework and CKEditor 5.

## Features

- Rich text editing with CKEditor 5
- Support for 30+ languages
- Automatic translation using Google Translate
- REST API with language selection
- Efficient caching mechanism
- Clean and simple admin interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multilingual-faq.git
cd multilingual-faq
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Usage

### List FAQs
```bash
GET /api/faqs/
```

### Get FAQ in specific language
```bash
GET /api/faqs/?lang=hi  # Hindi
GET /api/faqs/?lang=es  # Spanish
GET /api/faqs/?lang=fr  # French
```

### Create FAQ
```bash
POST /api/faqs/
Content-Type: application/json

{
    "question": "How do I use this API?",
    "answer": "<p>Just make a GET request!</p>",
    "language": "en"
}
```

### Update FAQ
```bash
PUT /api/faqs/{id}/
Content-Type: application/json

{
    "question": "Updated question",
    "answer": "<p>Updated answer</p>",
    "language": "en"
}
```

## Running Tests

```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Commit Message Convention

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests
- `chore`: Changes to the build process or auxiliary tools

## License

This project is licensed under the MIT License - see the LICENSE file for details.
