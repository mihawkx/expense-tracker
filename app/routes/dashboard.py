from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Expense, Category
from sqlalchemy import func, extract
from datetime import datetime
from app import db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    now = datetime.now()
    month, year = now.month, now.year

    # Total do mês
    total_month = db.session.query(func.sum(Expense.amount))\
        .filter(
            Expense.user_id == current_user.id,
            extract('month', Expense.date) == month,
            extract('year', Expense.date) == year
        ).scalar() or 0
    
    # Total por categoria no mês
    by_category = db.session.query(
        Category.name,
        func.sum(Expense.amount).label('total')
    ).join(Expense)\
    .filter(
        Expense.user_id == current_user.id,
        extract('month', Expense.date) == month,
        extract('year', Expense.date) == year
    ).group_by(Category.name).all()

    # Últimos 5 gastos
    recent = Expense.query.filter_by(user_id=current_user.id)\
        .order_by(Expense.date.desc()).limit(5).all()
    chart_data = {
    "labels": [f"{c.icon} {c.name}" for c in by_category],
    "values": [float(c.total) for c in by_category],
    }
    return render_template('dashboard/index.html',
        total_month=total_month,
        by_category=by_category,
        recent=recent,
        month_name = now.strftime('%B/%Y'),
        chart_data=chart_data
    ) 