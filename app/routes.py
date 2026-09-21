from flask import Blueprint, redirect, render_template, request, url_for

from app import db
from app.models import Repair


main = Blueprint("main", __name__)


@main.route("/")
def index():
    repairs = Repair.query.order_by(Repair.created_at.desc()).all()

    return render_template(
        "repairs.html",
        repairs=repairs,
    )


@main.route("/repairs/new", methods=["GET", "POST"])
def new_repair():
    if request.method == "POST":
        repair = Repair(
            customer=request.form["customer"],
            item=request.form["item"],
            problem=request.form["problem"],
            status="Received",
        )

        db.session.add(repair)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("repair_form.html")

@main.route("/repairs/<int:repair_id>")
def repair_detail(repair_id):
    repair = Repair.query.get_or_404(repair_id)

    return render_template(
        "repair_detail.html",
        repair=repair,
    )