from bottle import route, run, request, abort

from gitlab_api.cli_mrs_issues import get_issues_mrs_by_year
from gitlab_api.cli_roles import update_role
from datetime import datetime


def valid_year(year):
    if year and year.isdigit():
        if int(year) >= 1900 and int(year) <= datetime.now().year:
            return year
    abort(500, "You must provide a valid year")


@route("/issues", method="GET")
def issues():
    if not request.query.year:
        abort(500, "You must provide a valid year")
    if valid_year(request.query.year) == 1:
        abort(500, "You must provide a valid year")

    return get_issues_mrs_by_year(year)


@route("/user", method="POST")
def issues():
    if not request.query.role or not request.query.group or not request.query.user:
        abort(500, "You must provide: user, group & role")

    return update_role(request.query.role, request.query.group, request.query.user)


if __name__ == "__main__":
    run(debug=True, port=8888)
