import click
from .gitlab_utils import generate_client

def update_role(token, host, year):
    click.echo(f"generating gl client for host {host}")
    gl_client = generate_client(token, host)
    

@click.command(name="update-role")
@click.option("--target", "-t", required=True)
@click.option("--target-type", "-a", type=click.Choice([""]) required=True)
@click.option("--role", "-r", required=True)
@click.option("--username", "-u", required=True)
@click.pass_context
def update_role(ctx, role, target, username):
    role = ctx.obj["role"]
    target = ctx.obj["target"]
    username = ctx.obj["username"]
    return f"role: {role}\ngroup: {target}\nusername: {username}\n"