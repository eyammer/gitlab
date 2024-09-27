import click
import gitlab
from .gitlab_utils import generate_client


def target_exists(target, item_list):
    for item in item_list:
        if item.name == target:
            return True
    raise LookupError(f"The target {target} does not exist")


def get_item(target, target_type, gl):
    if target_type == "group":
        if target_exists(target, gl.groups.list(iterator=True)):
            group = gl.groups.get(target)
            return group
    if target_type == "repo":
        if target_exists(target, gl.groups.list(iterator=True)):
            repo = gl.project.get(target)
            return repo


def user_exists(username, gl):
    if target_exists(username, gl.users.list(iterator=True)):
        return True


def update_role(token, host, target, target_type, username, role):
    click.echo(f"generating gl client for host {host}")
    gl_client = generate_client(token, host)
    # gl_client.users.list()
    user_exists(username, gl_client)
    object_to_edit = get_item(target, target_type, gl_client)
    user = gl_client.users.get(username)
    print(object_to_edit)
    if target_exists(object_to_edit.member.list(), username):
        object_to_edit.member.get(user.id).access_level = gitlab.const.AccessLevel[
            role.upper()
        ]
    else:
        object_to_edit.members.create(
            {"user_id": user.id, "access_level": gitlab.const.AccessLevel[role.upper()]}
        )


@click.command(name="update-role")
@click.option("--target", "-t", required=True)
@click.option(
    "--target-type", "-a", type=click.Choice(["group", "repo"]), required=True
)
@click.option(
    "--role",
    "-r",
    type=click.Choice(["guest", "reporter", "developer", "maintainer", "owner"]),
    required=True,
)
@click.option("--username", "-u", required=True)
@click.pass_context
def cli_update_role(ctx, role, target, username, target_type):
    ctx.obj["role"] = role
    ctx.obj["target"] = target
    ctx.obj["username"] = username
    ctx.obj["target_type"] = target_type

    update_role(ctx.obj["token"], ctx.obj["host"], target, target_type, username, role)
