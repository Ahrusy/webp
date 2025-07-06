from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    context = {
        "page_title": "Главная - Здоровый образ жизни",
        "featured_articles": [
            {
                "title": "10 принципов правильного питания",
                "excerpt": "Правильное питание - основа здоровья и долголетия...",
                "link": "#"
            },
            {
                "title": "Утренняя зарядка: 15 минут для здоровья",
                "excerpt": "Начните свой день с простых упражнений...",
                "link": "#"
            }
        ]
    }
    return render_template("home.html", **context)

@app.route("/about/")
def about():
    context = {
        "page_title": "О нас - Здоровый образ жизни",
        "team_members": [
            {
                "name": "Доктор Иванова",
                "position": "Врач-диетолог",
                "photo": "https://via.placeholder.com/150"
            },
            {
                "name": "Петр Сидоров",
                "position": "Фитнес-тренер",
                "photo": "https://via.placeholder.com/150"
            },
            {
                "name": "Анна Смирнова",
                "position": "Психолог",
                "photo": "https://via.placeholder.com/150"
            }
        ],
        "principles": [
            "Научная обоснованность информации",
            "Практическая применимость советов",
            "Индивидуальный подход к здоровью",
            "Доступность информации для всех"
        ]
    }
    return render_template("about.html", **context)

if __name__ == "__main__":
    app.run(debug=True)