from obscurepy.obfuscator import Obfuscator
import click


@click.command()
@click.option('--filepath', help='File path to provide if you would like to obscure a single file')
@click.option('-p', '--project', is_flag=True, help='Enable this flag if you wish to obscure a multi file project')
@click.option('--project_dir', help='The directory of the project to obscure')
@click.option('--output_dir', default='.', help='The directory to output the obscured code')
@click.option('-l', '--log', is_flag=True, default=False, help='Enable this flag to turn on logging')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Enable this flag to write logging to stdout')
def obscure(filepath, project, project_dir, output_dir, log, verbose):
    """Make your Python code difficult to read"""
    check_bad_option_usage(filepath, project, project_dir, output_dir)
    Obfuscator(filepath, project, project_dir,
               output_dir, log, verbose).obscure()


def check_bad_option_usage(filepath, project, project_dir, output_dir):
    """Validates the arguments passed to the Obfuscator"""
    if filepath and project:
        raise click.BadOptionUsage('project',
                                   'You should not enable the project flag if filepath is provided')
    elif filepath and project_dir:
        raise click.BadOptionUsage('project_dir',
                                   'You should not provide both a filepath and a project directory')
    elif project and not project_dir:
        raise click.BadOptionUsage('project_dir',
                                   'If the project flag is enabled a project directory must be provided')
    elif not project and project_dir:
        raise click.BadOptionUsage('project',
                                   'If a project directory is provided the project flag must be enabled')
    elif not filepath and not project and not project_dir and (output_dir == '.'):
        raise click.MissingParameter(
            'You must provide some arguments to obscure')
