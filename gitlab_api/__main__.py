import click
from .cli_mrs_issues import cli_issues
from .cli_roles import cli_update_role


@click.group(name="main")
@click.option(
    "--token", help="gitlab authentication token", show_envvar=True, required=True
)
@click.option("--host", "-h", help="gitlab host", show_envvar=True, required=True)
@click.pass_context
def main(ctx, token, host):
    ctx.ensure_object(dict)
    ctx.obj["token"] = token
    ctx.obj["host"] = host


if __name__ == "__main__":
    main.add_command(cli_update_role)
    main.add_command(cli_issues)

    main(auto_envvar_prefix="GITLAB")
