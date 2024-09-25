import click
from datetime import datetime
from .gitlab_utils import generate_client

import json


def valid_year(ctx, self, year):
    if int(year) >= 2000 and int(year) <= datetime.now().year:
        return year
    raise click.BadParameter("You must select a year after 2000")


def make_list(iteratable_list):
    return_list = []
    for item in iteratable_list:
        click.echo(f"item: {item.id} added to list")
        return_list.append(item.id)
    return return_list


def get_issues(client, year):
    click.echo("getting list of issues")
    issues = client.issues.list(
        iterator=True,
        created_after=f"{year-1}-12-31T23:59:59.999Z",
        created_before=f"{year+1}-01-01T00:00:00.000Z",
        lazy=True,
    )
    return make_list(issues)


def get_mrs(client, year):
    click.echo("getting list of merge requests")
    mrs = client.mergerequests.list(
        iterator=True,
        created_after=f"{year-1}-12-31T23:59:59.999Z",
        created_before=f"{year+1}-01-01T00:00:00.000Z",
        lazy=True,
    )
    return make_list(mrs)


def get_issues_mrs_by_year(token, host, year, target_type):
    click.echo(f"generating gl client for host {host}")
    gl_client = generate_client(token, host)

    if target_type == "issues":
        return json.dumps({"issues": get_issues(gl_client, year)})
    elif target_type == "mr":
        return json.dumps({"merge_requests": get_mrs(gl_client, year)})
    return json.Dumps({})


@click.command("issues")
@click.option("--year", "-y", required=True, type=int, callback=valid_year)
@click.option("--target-type", "-o", type=click.Choice(["mr", "issues"]), required=True)
@click.pass_context
def cli_issues(ctx, year, target_type):
    ctx.obj["year"] = year
    ctx.obj["target_type"] = target_type
    click.echo(
        get_issues_mrs_by_year(ctx.obj["token"], ctx.obj["host"], year, target_type)
    )
