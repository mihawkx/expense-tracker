# 💸 Fintrack — Rastreador de Gastos Pessoais

Aplicação web fullstack de controle financeiro desenvolvida para praticar Flask, PostgreSQL e deploy em nuvem.

**🔗 [Demo ao vivo](https://web-production-c52ebd.up.railway.app/)**

---

## 🛠 Tecnologias utilizadas

- **Backend:** Python, Flask, SQLAlchemy, Flask-Login, Flask-Migrate
- **Banco de dados:** PostgreSQL
- **Frontend:** Tailwind CSS, Alpine.js, Chart.js
- **Deploy:** Railway + Gunicorn

---

## 💡 O que foi praticado

- Autenticação de usuários com hash de senha (Werkzeug)
- Modelagem relacional com SQLAlchemy (User, Category, Expense)
- CRUD completo com Flask Blueprints
- Migrations com Alembic via Flask-Migrate
- Templates Jinja2 com herança (`base.html`)
- Deploy contínuo via GitHub → Railway
- Variáveis de ambiente e configuração para produção

---
## Screenshots

**Tela de login**
<img width="1919" height="912" alt="image" src="https://github.com/user-attachments/assets/e2c4582d-ff7b-4c24-b03b-765de02bee0b" />

**Dashboard**
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/e69ee572-4065-480c-a03a-515f584ee99d" />

**Gastos**
<img width="1919" height="909" alt="image" src="https://github.com/user-attachments/assets/5ceac197-3156-481d-9572-693af428744f" />

**Novo gasto**
<img width="1919" height="914" alt="image" src="https://github.com/user-attachments/assets/fdefbf94-8228-4025-8c41-4bf1dc02582a" />


## ⚙️ Como rodar localmente

```bash
git clone https://github.com/mihawkx/expense-tracker.git
cd expense-tracker

python -m venv .venv
.venv\Scripts\activate  # Windows

pip install -r requirements.txt

# Configure o .env com sua DATABASE_URL e SECRET_KEY
flask db upgrade
python run.py
```

Acesse em `http://127.0.0.1:5000`

---

## Licenca

Projeto para estudo e uso pessoal.

Desenvolvido por **Enzo Amorim** • [github.com/mihawkx](https://github.com/mihawkx)
