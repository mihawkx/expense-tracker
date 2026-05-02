from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Expense, Category
from datetime import datetime


expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('/')
@login_required
def list():
    expenses = Expense.query.filter_by(user_id=current_user.id)\
        .order_by(Expense.date.desc()).all()
    return render_template('expenses/list.html', expenses=expenses)

@expenses_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    categories = Category.query.all()
    if request.method == 'POST':
        expense = Expense(
            description = request.form.get('description'), # type: ignore
            amount = request.form.get('amount'), # type: ignore
            date = datetime.strptime(request.form.get('date'), '%Y-%m-%d'), # type: ignore
            notes = request.form.get('notes'), # type: ignore
            category_id = request.form.get('category_id'), # type: ignore
            user_id=current_user.id # type: ignore
        )
        db.session.add(expense)
        db.session.commit()
        flash('Despesa adicionada com sucesso!', 'success')
        return redirect(url_for('expenses.list'))
    
    return render_template("expenses/form.html", categories=categories, expense=None, now=datetime.utcnow())
@expenses_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    expense = Expense.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    categories = Category.query.all()
    if request.method == 'POST':
        expense.description = request.form.get('description')
        expense.amount = request.form.get('amount')
        expense.date = datetime.strptime(request.form.get('date'), '%Y-%m-%d') # type: ignore
        expense.category_id = request.form.get('category_id')
        db.session.commit()
        flash('Despesa atualizada com sucesso!', 'success')
        return redirect(url_for('expenses.list'))
    
    return render_template("expenses/form.html", categories=categories, expense=expense, now=datetime.utcnow())

@expenses_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    expense = Expense.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(expense)
    db.session.commit()
    flash('Despesa excluída com sucesso!', 'success')
    return redirect(url_for('expenses.list'))