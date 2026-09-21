from flask import Blueprint, render_template

from app.models import Repair


main = Blueprint("main", __name__)


@main.route("/")
def index():
    repairs = Repair.query.order_by(Repair.created_at.desc()).all()

    return render_template(
        "repairs.html",
        repairs=repairs,
    )