import os
from flask import Blueprint, render_template, flash, url_for, redirect, current_app
from flask_login import login_required
from hashview.models import Rules
from hashview.rules.forms import RulesForm
from hashview.rules.utils import save_file, get_linecount, get_filehash
from hashview import db


rules = Blueprint('rules', __name__)

#############################################
# Rules
#############################################

@rules.route("/rules", methods=['GET'])
@login_required
def rules_list():
    rules = Rules.query.all()
    return render_template('rules.html', title='Rules', rules=rules) 

@rules.route("/rules/add", methods=['GET', 'POST'])
@login_required
def rules_add():
    form = RulesForm()
    if form.validate_on_submit():
        if form.rules.data:
            rules_path = os.path.join(current_app.root_path, save_file('control/rules', form.rules.data))
            
            rule = Rules(name=form.name.data, 
                                path=rules_path,
                                size=get_linecount(rules_path),
                                checksum=get_filehash(rules_path))
            db.session.add(rule)
            db.session.commit()
            flash(f'Rules File created!', 'success')
            return redirect(url_for('rules.rules_list'))  
    return render_template('rules_add.html', title='Rules Add', form=form)   

@rules.route("/rules/delete/<int:rule_id>", methods=['GET', 'POST'])
@login_required
def rules_delete(rule_id):
    rule = Rules.query.get_or_404(rule_id)
    # TODO
    #if post.author != current_user:  #confirm if admin
    #    abort(403)
    #if wordlist.type == 'dynamic': # prevent deltion of dynamic list
    #   abort(403)
    db.session.delete(rule)
    db.session.commit()
    flash('Rule file has been deleted!', 'success')
    return redirect(url_for('rules.rules_list'))